## this is an example code for web crawling and 
## scraping internal link on a webpage
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
#set the random generator seed with the current system time
random.seed(datetime.datetime.now())

def getLinks(articleURL):
        # open a handle of the html page
    try:
        html=urlopen("http://en.wikipedia.org"+articleURL)
    #the webpage is not found on the server
    except HTTPError as e: 
        return None
    try:
        # feed the html text to a soup object
        soup=BeautifulSoup(html,'lxml')
        # get all the a tags for wiki articles on the page
        links=soup.find('div',{'id':'bodyContent'}).find_all('a',
                        href=re.compile('^(/wiki/)((?!:).)*$'))
        return links
    #guard if the div tag does not exist
    except AttributeError as e: 
        return None
        
# use Kevin Bacon link as an example
links = getLinks('/wiki/Kevin_Bacon')

if links is None:
    print('links could not be found')
else:
    print(links)
    
# randomly get an article links on kevin bacon wiki page 
while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)


   
