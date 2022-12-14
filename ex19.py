
import requests
from bs4 import BeautifulSoup
URL = " https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture" 
r = requests.get(URL)
r_html = r.text

soup = BeautifulSoup(r_html)
title = soup.find('span', 'articletitle').string


def print_to_text(base_url):
    """
    :param base_url: URL of article to scrape
    :return: naked content to text file
    """
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text)
    with open("work less.txt", "w") as textfile:
        for paragraph in soup.find_all(dir="ltr"):
            textfile.write(paragraph.text.replace("<span>",""))

if __name__ == "__main__":
    #Chose my own article
    base_url = "http://www.theatlantic.com/business/archive/2014/08/to-work-better-work-less/375763/"
    base_url2 = "http://www.theatlantic.com/business/archive/2014/08/to-work-better-work-less/375763/2/"
    print_to_text(base_url)
    print_to_text(base_url2)