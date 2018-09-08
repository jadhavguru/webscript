import re
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url='https://timesofindia.indiatimes.com/news'

uClient=uReq(my_url)

page_html=uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"main-content"})

print(len(containers))

#print(soup.prettify(containers[0]))


container=containers[0]
#print(soup.prettify(containers[0]))

print(container.div.ul.li.a.img ["alt"])
main_content=page_soup.find_all(class_='w_desc')
print(main_content[0].text)

filename="output.csv"
f =open(filename,"w")
headers="Tiles,Description"




#print(container)
#print(container.div.img["alt"])
#price=containers.findall("div", {"class":"col col-5-12 _2o7WAb"})
#print(price[0].text)

#price=container.findall("div", {"class":"_1vC4OE _2rQ-NK"})
#print(price[0].text)

