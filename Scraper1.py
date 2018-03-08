from bs4 import BeautifulSoup
from __future__ import print_function
import urllib2

pages = set(["/wiki/Main_Page"])

dict_ref = {}
def getLinks(pageUrl, dict_ref):
    dict_ref = dict_ref
    global pages
    start_link = "https://en.wikipedia.org" + pageUrl
    html = urllib2.urlopen(start_link)
    bsObj = BeautifulSoup(html.read(), "lxml")
    head = bsObj.h1.get_text()
    
    #links = bsObj.find("div", {"id":"mw-navigation"}).findAll("a")
    target_link = "https://uk.wikipedia.org/wiki/"
    #for link in links:
    #    if ("href" in link.attrs) and (link.attrs["href"][:31] == target_link):
    #        dict_ref[head] = (start_link, link["href"])
    #        print(link)
    #        break
    link_ukr = bsObj.find("li", {"class":"interlanguage-link interwiki-uk"})
    if link_ukr:
        dict_ref[head] = (start_link, link_ukr.a["href"])
        #print(dict_ref)
    
    links = bsObj.find("div", {"id":"bodyContent"}).findAll("a")
    for link in links[5:]:
        if ("href" in link.attrs) and (link["href"][:5]=="/wiki") and (link["href"] not in pages):
            #print(pages)
            newPage = link.attrs["href"]
            pages.add(newPage)
            getLinks(newPage, dict_ref)
    if (len(pages) > 30) or (len(dict_ref.items()) > 30):
        return dict_ref
            
d = getLinks("/wiki/Main_Page", dict_ref = {})
print("""
-----------------------------------------
""")
print(d)
