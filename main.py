import time
import os
import logging
import threading
from flask import Flask
from playwright.sync_api import sync_playwright

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='website_test_log.txt', level=logging.INFO)

# Function to test websites
def test_website(url):
    result = "Success"
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)
            result = "Website loaded successfully"
            browser.close()
    except Exception as e:
        result = f"Failed to load website: {e}"

    # Log the website and its result
    logging.info(f"Website: {url} - Result: {result}")
    print(f"Website: {url} - Result: {result}")

# Dummy route to make the app a web service
@app.route('/')
def hello_world():
    return 'Hello, world!'

def run_flask():
    # Run the Flask app (it will listen on port 5000 by default)
    app.run(host="0.0.0.0", port=5000)

def test_websites_continuously():
    # The directory where your website URLs (text files) are located
    urls_directory = "/path/to/your/websites"
    
    while True:
        # List all text files in the directory
        for filename in os.listdir(urls_directory):
            if filename.endswith('.txt'):
                # Read URLs from the text file
                with open(os.path.join(urls_directory, filename), 'r') as file:
                    urls = file.readlines()
                    for url in urls:
                        url = url.strip()  # Clean up the URL
                        if url:  # Skip empty lines
                            test_website(url)
        time.sleep(3600)  # Sleep for an hour before testing again

if __name__ == '__main__':
    # Start Flask server in a separate thread
    thread = threading.Thread(target=run_flask)
    thread.start()

    # Start the continuous website testing
    test_websites_continuously()
