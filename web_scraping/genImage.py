import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

def get_quotes(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error fetching the URL:", e)
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []

    for quote_div in soup.select("div.quote"):
        text = quote_div.select_one("span.text").get_text().strip("“”")
        author = quote_div.select_one("span > small.author").get_text().strip()
        quotes.append({"Quote": text, "Author": author})

    return quotes

def create_image(quote, author, index):
    width, height = 800, 400
    backgroud_color = "#f8d77f"
    text_color = "#262626"

    image = Image.new("RGB", (width, height), backgroud_color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()
    author_font = ImageFont.load_default()

    wrapped = textwrap.fill(quote, width=60)
    author_text = f"- {author}"

    y_text = 60
    draw.text((40, y_text), wrapped, font=font, fill=text_color)
    y_text += wrapped.count('\n') * 15 + 40
    draw.text((500, y_text), author_text, font=font, fill=text_color)

    # save image
    if not os.path.exists("images"):
        os.makedirs("images")

    filename = os.path.join("images", f"quote_{index+1}.png")
    image.save(filename)
    print(f"✅ saved: {filename}")

if __name__ == "__main__":
    URL = "https://quotes.toscrape.com"
    quotes = get_quotes(URL)

    for idx, item in enumerate(quotes, start=0):
        print(f"Processing quote {idx + 1}: {item['Quote']} - {item['Author']}")
        create_image(item["Quote"], item["Author"], idx)
    
