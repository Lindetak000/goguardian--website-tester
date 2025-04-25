from flask import Flask
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route('/')
def index():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        browser.close()
    return "Visited example.com successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
