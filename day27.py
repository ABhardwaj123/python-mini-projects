import os
import requests
import textwrap
from bs4 import BeautifulSoup
from PIL import Image , ImageDraw , ImageFont

base_url = "https://quotes.toscrape.com/"
output_dir = "quotes"

def collect_quotes():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text , "html.parser")

    quotes = soup.select("div.quote")

    quote_data = []

    for q in quotes[:5]:
        text = q.find("span", class_ = "text").text.strip()
        author = q.find("small" , class_= "author").text

        quote_data.append((text , author))

    return quote_data

#creating an image
def make_image(text , author , index):
    width ,height = 800 , 400
    bg_color = "#fdecf3"
    text_color = "#33333326"

    image = Image.new("RGB", (width ,height) , bg_color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()
    wrapped = textwrap.fill(text , width = 60)
    author_text = f"- {author}"

    draw.text((40 , 60) , wrapped , font=font , fill = text_color)
    draw.text((500 , 100 + wrapped.count('\n')* 15) , author_text , font = font , fill = text_color)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = os.path.join(output_dir , f"{index+1}.png")
    image.save(filename)

    print(f"file saved: {filename}")

def main():
    quotes = collect_quotes()
    for idx , (text , author) in enumerate(quotes):
        make_image(text , author , idx)

    
if __name__ == "__main__":
    main()
