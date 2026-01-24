import csv
import requests
from bs4 import BeautifulSoup


def scrape_to_csv(url, csv_filename):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("An Error Occured:", e)
    
    soup = BeautifulSoup(response.text, "html.parser")
    html_tags = soup.select("span.titleline > a")

    tags = []
    for tag in html_tags:
        title: str = tag.text.strip()
        url = tag.get("href").strip()
        tags.append({"title": title, "url": url})
    with open(f"{csv_filename}.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "url"])
        writer.writeheader()
        writer.writerows(tags)


scrape_to_csv("https://news.ycombinator.com","links")