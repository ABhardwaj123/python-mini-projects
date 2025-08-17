#web scraping
#beautifulsoup4 is a library helpful in web scraping

import requests
from bs4 import BeautifulSoup

url ="https://en.wikipedia.org/wiki/Nvidia"

def get_h2_header(url):
    try:
        response = requests.get(url , timeout=10) #get response under 10seconds else show error
        response.raise_for_status() #will raise error if it doesn't get response

    except requests.RequestException as e:
        print("failed to fetch a response\n")
        print(e)
        return []
    
    #parser->converts text to designated parser(maybe html parser , json parser etc)
    soup = BeautifulSoup(response.text , "html.parser") #response.text contains all the html content of web page
    h2_tags = soup.find_all("h2")

    #printing all tags
    print(h2_tags)

    headers = []

    for tag in h2_tags:
        header_text = tag.get_text(strip = True) #.get_text used to get text inside the html tag(h2 tag in this case)

        if header_text and header_text.lower() != "contents": #we are trying to ignore the contents header
            headers.append(header_text)


    #printing first 10 h2 tags
    for i in range(0,10):
        print(headers[i])


get_h2_header(url)