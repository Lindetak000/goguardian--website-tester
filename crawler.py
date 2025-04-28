from flask import Flask
import threading
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

app = Flask(__name__)

visited = set()  # Websites we've already visited

# Crawler task
def crawl_web(start_urls):
    to_visit = list(start_urls)
    
    while to_visit:
        url = to_visit.pop(0)
        if url in visited:
            continue
        visited.add(url)
        
        try:
            print(f"Crawling {url}")
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                continue
            
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                href = link['href']
                full_url = urljoin(url, href)
                parsed = urlparse(full_url)
                
                # Only crawl http or https links
                if parsed.scheme in ('http', 'https'):
                    if full_url not in visited:
                        to_visit.append(full_url)
        
        except Exception as e:
            print(f"Error crawling {url}: {e}")
        
        time.sleep(1)  # Be polite: 1 second between requests

@app.route('/')
def home():
    return f'Crawler is running! Visited {len(visited)} sites.'

if __name__ == '__main__':
    # Start crawler in background
    start_urls = ['https://google.com']  # You must pick a starting point!
    thread = threading.Thread(target=crawl_web, args=(start_urls,), daemon=True)
    thread.start()
    
    # Start Flask app
    app.run(host='0.0.0.0', port=8080)
