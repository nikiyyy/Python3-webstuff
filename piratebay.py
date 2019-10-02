#webscraper for piratebay

import requests
from bs4 import BeautifulSoup as bs

siteproxy="https://pirateproxy.ch"
search_therm="shrek" #change to whatever you need
def pages(br):
    cur_br=0
    while cur_br<=br:
        print("in")
        site=requests.get(siteproxy+"/search/"+search_therm+"/"+str(cur_br)+"/")
        site_con=site.content
        soup=bs(site_con,"html.parser")
        for link in soup.findAll('a',{"class":"detLink"}):
            title = link.get('title')
            print(title)
        cur_br+=1
        print("new page")
    
pages(2)# number of pages to serch
