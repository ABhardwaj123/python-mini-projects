#download images
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

base_url = "https://books.toscrape.com/" #url from which we want to scrape
images_collection = "images" #directory in which we will save images

def cleaning_filename(title):    
    return re.sub(r'[^\w\-_. ]' , '' , title).replace(" ", "_")
    #the re.sub will replace [^\w\-_. ] with '' in the title
    #the replace with replace " " with "_"

def download_image(image_url , file_name):
    try:
        response = requests.get(image_url , stream=True , timeout=10)
        response.raise_for_status()

        with open(file_name , "wb") as f: #wb -> we are writing in binary mode because we are extracting images
            for chunk in response.iter_content(1024): #iter_content breaks the response into iterable chunks of 1kb each
                f.write(chunk)
    
    except requests.RequestException as e:
        print(e)
    
def scrape_image():
    url = base_url
    response = requests.get(url)

    soup = BeautifulSoup(response.text ,"html.parser")
    books = soup.select("article.product_pod")[:10]
    # will selects first ten elements with "article.product_pod"

    if not os.path.exists(images_collection): #making the image directory if it does not exists
        os.makedirs(images_collection)

    for book in books:
        title = book.h3.a['title'] #title of book is in h3 tag->a->"title"
        relative_img = book.find("img")["src"] #basically extracting the img tag from website
        img_url = urljoin(base_url , relative_img) #joins the base url and image url to a full absolute url

        filename = cleaning_filename(title) + ".jpg" 
        #its the file name, file name will include book_name.jpg

        filepath = os.path.join(images_collection , filename) 
        #filepath will then add the filename to our directory of image collection
        print(f"currently downloading {title}")
        print(f"filepath : {filepath}\n")

        download_image(img_url, filepath)

    print("all books covers downloaded")

def main():
    scrape_image()


if __name__ == "__main__":
    main()