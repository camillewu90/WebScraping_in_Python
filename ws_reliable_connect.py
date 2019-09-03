from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup 
# get the title of the webpage
def getTitle(url): 
    #open the webpage
    try:
        html = urlopen(url)
    #the webpage is not found on the server
    except HTTPError as e: 
        return None
    try:
        #pass the content of the page to a BeautifulSoup object
        bsObj = BeautifulSoup(html,features="lxml") 
        #get the title content of the h1 tag
        title = bsObj.body.h1
    #guard if the body tag does not exist
    except AttributeError as e: 
        return None
    return title
title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print ("title could not be found")
else:
    print(title)
        
     