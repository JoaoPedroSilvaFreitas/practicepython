
import requests
from bs4 import BeautifulSoup

URL = "https://www.nytimes.com/" 
r = requests.get(URL)
r_html = r.text

soup = BeautifulSoup(r_html, features = "lxml")
title = str(soup.find('span', 'articletitle'))#.string

for story_heading in soup.find_all(class_ = "story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())