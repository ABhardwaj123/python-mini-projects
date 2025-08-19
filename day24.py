#scraping data

import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin 

base_url = "https://books.toscrape.com/"
start_page = "catalogue/page-1.html"
output = "books_data.json"
target_count = 20 #say we want to scrape 20 books

def scrap_page(url):
    try:
        response = requests.get(url , timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(e)
        return [], None #none is returned at end of scraping, no further scraping
    
    soup = BeautifulSoup(response.text , "html.parser")

    books = []

    for article in soup.select("article.product_pod"):
        title_tag = article.select_one("h3 > a")
        title = title_tag.get("title")

        price = article.select_one("p.price_color").text.strip()
        books.append({"title": title , "price": price})

    next_link = soup.select_one("li.next > a")    
    
    next_url = urljoin(url , next_link.get("href")) if next_link else None

    return books , next_url


def main():

    collection = []

    current_url = urljoin(base_url , start_page)

    while len(collection) < target_count and current_url:
        print(f"currently scraping {current_url}")
        books , next_url = scrap_page(current_url)

        collection.extend(books)
        current_url = next_url

    collection = collection[:target_count] # to ensure that we only save the defined number of targets
    print(f"scapred {len(collection)} books")

    #add the final collection list to json
    with open(output , "w" , encoding="utf-8") as f:
        json.dump(collection , f , indent = 2)

    print(f"data saved to your json file {output}")


if __name__ == "__main__":
    main()

