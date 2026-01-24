import json
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch url: {e}")
        return [], None
    soup = BeautifulSoup(response.text, "html.parser")
    books = []
    for article in soup.select("article.product_pod"):
        title_tag = article.select_one("h3 > a")
        title: str = title_tag.get("title")
        price: str = article.select_one("div.product_price > p.price_color").get_text().strip().removeprefix("\u00c2\u00a3") + " euros"
        books.append({"title": title, "price": price})

    next_link = soup.select_one("li.next > a")
    next_url = urljoin(url, next_link.get("href")) if next_link else None
    
    return books, next_url

if __name__ == "__main__":
    collected_books = []
    total_books_to_scrape = 10
    base_url = "https://books.toscrape.com/catalogue/page-1.html"
    current_url = base_url

    while len(collected_books) < total_books_to_scrape and current_url:
        print(f"Scraping: {current_url}")
        books, next_url = scrape_page(current_url)
        collected_books.extend(books)
        current_url = next_url
    
    collected_books = collected_books[:total_books_to_scrape]
    print(f"Scraped {len(collected_books)} books")

    with open("books_data.json", "w", encoding="utf-8") as f:
        json.dump(collected_books, f, indent=2)
    
    print("Data saved to books_data.json")