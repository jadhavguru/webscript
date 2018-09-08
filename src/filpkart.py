from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

my_url="https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_0_3&otracker1=AS_QueryStore_HistoryAutoSuggest_0_3&as-pos=0&as-type=HISTORY&as-backfill=on"

uclient=ureq(my_url)
page_html=uclient.read()
uclient.close()

page_soup=soup(page_html, "html.parser")

containers=page_soup.find_all(class_='_1UoZlX')
print(len(containers))

container=containers[3]
#print(soup.prettify(container))

#print(container.div.a.div.img['alt'])

#Title=page_soup.find_all(class_=)
price=container.find_all(class_='col col-5-12 _2o7WAb')
print(price[0].text)

rating=container.find_all(class_='hGSR34 _2beYZw')
print(rating[0].text)