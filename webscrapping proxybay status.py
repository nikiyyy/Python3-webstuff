import requests
from bs4 import BeautifulSoup as bs

site=requests.get("https://proxybay.app/")
site_con=site.content

soup=bs(site_con,"html.parser")
"""
find_id=soup.find_all("table",{"id":"proxyList"})
find_id2=soup.find_all("tr")

print(find_id2.prettyfy())

"""
for link in soup.findAll('a',{"class":"t1"}):
    href = link.get('href')
    print(href)