from bs4 import BeautifulSoup
import requests


URL = "https://renyicasting.en.made-in-china.com/productList?username=&pageNumber=1&pageSize=48&viewType=0&isByGroup=1&pageUrlFrom=1&productGroupOrCatId=noiJrQaOTYkU&searchKeyword=&searchKeywordSide=&searchKeywordList=&selectedFeaturedType=&selectedSpotlightId=&viewPageSize=48"
html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
product = soup.find_all('a', {"class": "J-enlarge-link"})

for a in product:
	URL = a['href']
	html = requests.get(URL).text
	soup = BeautifulSoup(html, 'lxml')
	img_link = soup.find_all('meta', {"property": "og:image"})
	for link in img_link:
		url = link['content']
		r = requests.get(url, stream=True)
		image_name = url.split('/')[-1]
		with open('E:\downloads\%s' % image_name, 'wb') as f:
			for chunk in r.iter_content(chunk_size=128):
				f.write(chunk)
		print('Saved %s' % image_name)
		


