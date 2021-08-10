
import requests
from bs4 import BeautifulSoup
from typing import Counter

url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find('citations needed')

#print(soup)

citations = soup.find_all(class_ = 'Template-Fact')

#1 
def get_citations_needed(url):
  print(len(citations))
get_citations_needed(url)

#2 

def get_citations_needed_report(url):
  for cite in citations:
    print(cite.parent.text)
get_citations_needed_report(url)

