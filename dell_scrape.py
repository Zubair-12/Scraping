HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
            'Accept-Language': 'en-US, en;q=0.5'})

!pip install requests

import requests

URL = 'https://www.dell.com/en-pk/shop/scc/sc/laptops'
webpage = requests.get(URL)

webpage

!pip install BeautifulSoup4

from bs4 import BeautifulSoup

soup = BeautifulSoup(webpage.text, 'html.parser')

title = soup.find_all('a',{"class":"cat-fran-link"})

len(title)

title[0]['title']

title_list = []
for tag in title:
  title_list.append(tag['title'].strip())

title_list

url_list = []
for tag in title:
  url_list.append(tag['href'].strip())

url_list

dic = {
    'Title':title_list,
    'URLs':url_list
}
dic

import pandas as pd
data = pd.DataFrame(dic)

data

XPS = 'https://www.dell.com/en-pk/shop/laptops-2-in-1-pcs/sf/xps-laptops'

xps = requests.get(XPS)

xps_spec = BeautifulSoup(xps.text, 'html.parser')

desc_title = xps_spec.find_all('h2')

desc[0].text

desc_title_list = []
for tag in desc_title:
  desc_title_list.append(tag.text)

desc_title_list

desc = xps_spec.find_all('p')

desc_list =[]
for tag in desc:
  desc_list.append(tag.text)

desc_list

xps_info = {
    'Title':desc_title_list,
    'Description':desc_list
}
xps_info

xps_df = pd.DataFrame.from_dict(xps_info, orient='index')


xps_df
