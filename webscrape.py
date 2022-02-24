from bs4 import BeautifulSoup
import requests
from pprint import pprint
from urllib.parse import urljoin
import re

def export(data, export_filename):
    with open(export_filename, "w") as text_file:
        for x in data:
            text_file.write("%s" % x)

def extract_data(url):
	html=requests.get(url).content
	soup=BeautifulSoup(html,"lxml")
	bodycontent=soup.find("div", {"id": "bodyContent"})

	# grab all sub-links on page within the main body text and join with url
	links=[a['href'] for i,a in enumerate(bodycontent.find_all('a',href=True)) if a['href'].startswith('/wiki')][1:]
	url_links=[urljoin(url,link) for link in links]

	# for each url grab clinical question and bottom line
	for i,url_link in enumerate(url_links): 
		print(url_link)
		html=requests.get(url_link).content
		soup=BeautifulSoup(html,"lxml")
		paragraphs=soup.find_all("p")
		clinical_question=re.sub(",|\n","",paragraphs[0].getText()) # get 1st column of paragraphs, removing all commas and carraige returns
		bottom_line=re.sub(",|\n","",paragraphs[2].getText())

		data.append(clinical_question+","+bottom_line+","+links[i]+"\n") # data lines


page_urls=["https://www.wikijournalclub.org/w/index.php?title=Category:Usable_articles&fbclid=IwAR1NIBhuyP0phDXsIhNcRtdvMV1h5V43bgbBlii5WyONdturImVMq8KPZ7s&pageuntil=HEARTMATE+II#mw-pages",
	"https://www.wikijournalclub.org/w/index.php?title=Category:Usable_articles&fbclid=IwAR1NIBhuyP0phDXsIhNcRtdvMV1h5V43bgbBlii5WyONdturImVMq8KPZ7s&pagefrom=HEARTMATE+II#mw-pages",
	"https://www.wikijournalclub.org/w/index.php?title=Category:Usable_articles&fbclid=IwAR1NIBhuyP0phDXsIhNcRtdvMV1h5V43bgbBlii5WyONdturImVMq8KPZ7s&pagefrom=StiL#mw-pages"]
data=[]
data.append("clinical_question,bottom_line,link_name\n") # add header line
for url in page_urls:
	extract_data(url)

export(data,"scrape.csv")