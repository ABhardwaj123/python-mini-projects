import csv
import requests
from bs4 import BeautifulSoup

hn_url = "https://news.ycombinator.com/"
csv_file = "hn_top20.csv"

def fetch_data():
    try:
        response = requests.get(hn_url , timeout=10)
        response.raise_for_status() #raises errors if any

    except requests.RequestException as e:
        print(e)
        return []
    
    soup = BeautifulSoup(response.text , "html.parser")

    links = soup.select("span.titleline > a")
    #print(links)

    posts = []

    for link in links[:20]: #we only want top 20
        title = link.text.strip()
        url = link.get("href").strip()

        posts.append({"title": title, "url": url})
       

    return posts
    

def save_to_csv(posts):
    if not posts:
        print("no data found!")
        return
    
    with open(csv_file , "w" , newline="" , encoding="utf-8") as f:
        writer = csv.DictWriter(f , fieldnames=["title" , "url"])

        writer.writeheader()
        writer.writerows(posts)

        print("data saved to csv file!")


def main():
    print("scraping the HackerNews site")
    posts = fetch_data()

    save_to_csv(posts)



if __name__== "__main__":
    main()   
