import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import json
import wget

MAIN_URL = "https://books.toscrape.com"

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_\-\.]', '_', name).replace(' ', '_')

def scrape_image(url, fileName, folder="images"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        with open(os.path.join(folder, fileName), "wb") as f:
            for chunk in response.iter_content(8192):
                f.write(chunk)
        return os.path.join(os.getcwd(), folder, fileName)
    except Exception as e:
        print("An Error Occured", e)
        return None

def scrape_image_title_and_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("An Error Ocured", e)
        return [], None

    soup = BeautifulSoup(response.text, "html.parser")
    items = []

    for article in soup.select("article.product_pod"):
        titleTag = article.select_one("h3 > a")
        title = titleTag.get("title").strip()
        imgTag = article.select_one("div.image_container > a > img")
        imgURL = imgTag.get("src")
        # imgPath = scrape_image(urljoin(MAIN_URL, imgURL), sanitize_filename(title)+".jpg")
        # items.append({"title" : sanitize_filename(title), "imgURL": urljoin(MAIN_URL, imgURL), "imgPath": imgPath})
        '''
         Alternative method using wget
        '''
        if not os.path.exists("images"):
            os.makedirs("images")
        wget.download(urljoin(MAIN_URL, imgURL), out= os.path.join("images", sanitize_filename(title)+".jpg"))
        items.append({"title" : sanitize_filename(title), "imgURL": urljoin(MAIN_URL, imgURL), "imgPath": "images/"+sanitize_filename(title)+".jpg"})
    
    nextTag = soup.select_one("li.next > a")
    nextURL = urljoin(url, nextTag.get("href")) if nextTag else None

    return items, nextURL

if __name__ == "__main__":
    START_URL = urljoin(MAIN_URL, "/catalogue/page-1.html")
    booksToScrape = 10
    books = []
    NEXT_URL = START_URL

    while len(books) < booksToScrape and NEXT_URL:
        print("Scraping:", NEXT_URL)
        items, URL = scrape_image_title_and_url(NEXT_URL)
        books.extend(items)
        NEXT_URL = URL
    
    books = books[:booksToScrape]
    print(f"Scraped {len(books)} books")

    with open("books.json", "w") as f:
        json.dump(books, f, indent=2)
    print("Data saved to books.json")