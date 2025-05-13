import requests
from bs4 import BeautifulSoup
from functools import lru_cache

@lru_cache(maxsize=10)
def scrape_website(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=5)  
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')

        text_content = " ".join(p.get_text(separator=' ', strip=True) for p in paragraphs if p.get_text())
        return text_content if text_content else "No readable text found on this page."
    
    except requests.exceptions.Timeout:
        return "Error: The request timed out. Try a different website."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
