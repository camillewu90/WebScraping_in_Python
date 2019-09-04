## code example for collect data across an entire wiki site:
## data gathered:
## 1. title of the page
## 2. first paragraph of the body
## 3. all edit link

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
# initiate an empty set of page
pages=set()
# create a function to get internal link from wiki page
def getLinks(pageURL):
    # to allow modify pages within function
    global pages
    # get html text from wiki page
    try: 
        html=urlopen("http://en.wikipedia.org"+pageURL)
    except HTTPError as e:
        print('This page could not be found')
    # create a soup object
    soup=BeautifulSoup(html,'lxml')
    try:
        # get the main title from page
        print(soup.h1.get_text())
        # get the first paragraph from the body content
        print(soup.find(id='mw-content-text').find_all('p')[0].get_text())
        # get the edit link for that page
        print(soup.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! No worries though!')
    #scrape the internal link and store it in pages if not exist, then crawl to
    # that link as well
    for link in soup.find_all('a',href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('------------------\n'+newPage)
                pages.add(newPage)
                getLinks(newPage)
# initiate from wiki front page
getLinks("")
     
       
    