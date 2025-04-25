from playwright.sync_api import sync_playwright

def test_url(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            response = page.goto(url, timeout=10000)  # 10-second timeout
            if response and response.status == 200:
                print(f"{url} is accessible ✅")
            else:
                print(f"{url} is NOT accessible ❌ (Status: {response.status if response else 'No Response'})")
        except Exception as e:
            print(f"{url} failed to load ❌ (Error: {e})")
        finally:
            browser.close()

# Example URL
test_url("https://quora.com")
