import requests
import re
from bs4 import BeautifulSoup
import datetime
import random
#set the random generator seed with the current system time
random.seed(datetime.datetime.now())

def getLinks(articleURL):
    # set the starting wiki article page
    url="http://en.wikipedia.org"+articleURL
    # get the html text from the url
    html=requests.get(url).text
    # feed the html text to a soup object
    soup=BeautifulSoup(html,features='lxml')
    # get all the a tags for wiki articles on the page
    return soup.find('div',{'id':'bodyContent'}).find_all('a',
                    href=re.compile('^(/wiki/)((?!:).)*$'))
# use Kevin Bacon link as an example
links = getLinks('/wiki/Kevin_Bacon')

while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
