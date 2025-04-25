import asyncio
import playwright
from playwright.async_api import async_playwright
import time
import os

# Function to check websites
async def check_websites():
    websites = ["https://www.google.com", "https://www.bing.com", "https://quora.com"]  # Add more websites here
    results = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for website in websites:
            page = await browser.new_page()
            try:
                await page.goto(website, timeout=60000)  # Timeout after 60 seconds if page doesn't load
                result = f"Website: {website}, Status: Online"
            except Exception as e:
                result = f"Website: {website}, Status: Offline, Error: {str(e)}"
            results.append(result)
            await page.close()
        
        await browser.close()

    # Log results to txt file
    with open("website_results.txt", "a") as file:
        for result in results:
            file.write(result + "\n")
        file.write("\n")  # Add a newline after each run for separation


# Function to run the loop periodically
async def main():
    while True:
        await check_websites()
        print("Checked websites, sleeping for 1 hour...")
        time.sleep(3600)  # Sleep for 1 hour before checking again

if __name__ == "__main__":
    asyncio.run(main())
