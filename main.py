import asyncio
from playwright.async_api import async_playwright
import datetime

# List of starter URLs to branch from
seed_urls = [
    "https://example.com",
    "https://wikipedia.org",
    "https://mozilla.org"
]

# Set to track visited URLs
visited = set()

# Max number of pages to visit
MAX_VISITS = 50

async def crawl_and_test(playwright):
    browser = await playwright.chromium.launch(headless=True)
    page = await browser.new_page()

    to_visit = list(seed_urls)
    count = 0

    with open("results.txt", "w") as log_file:
        while to_visit and count < MAX_VISITS:
            url = to_visit.pop(0)
            if url in visited:
                continue
            try:
                await page.goto(url, timeout=10000)
                log_file.write(f"{datetime.datetime.now()}: SUCCESS - {url}\n")
                print(f"✅ Visited: {url}")
                visited.add(url)
                count += 1

                # Grab links to expand crawl
                links = await page.eval_on_selector_all("a", "els => els.map(e => e.href)")
                for link in links:
                    if link.startswith("http") and link not in visited:
                        to_visit.append(link)
            except Exception as e:
                log_file.write(f"{datetime.datetime.now()}: FAILED - {url} ({str(e)})\n")
                print(f"❌ Failed: {url}")
                visited.add(url)
                count += 1

    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await crawl_and_test(playwright)

asyncio.run(main())
