import requests
from bs4 import BeautifulSoup

# Swap this URL out for any site you want to test
url = 'https://example.com' 

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    print(f"--- Links extracted from {url} ---")
    # Finds all anchor tags <a> and prints their href attribute
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            print(href)
            
except Exception as e:
    print(f"Could not scrape the site: {e}")
