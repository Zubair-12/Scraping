!pip3 install requests requests selectorlib

!pip install requests

url = 'https://www.amazon.com/High-Back-Chair-Office-Ergonomic-Executive/dp/B07KJYY9BD/ref=sr_1_1_sspa?keywords=gaming%2Bchairs&pd_rd_r=b2fd28ae-7a32-41aa-8d1d-c09126e2bbed&pd_rd_w=Eua7a&pd_rd_wg=RTbkn&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=H9BJYPS8TFT1B0TPD1F3&qid=1680844110&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFGVUQyRFlUMFJYNU4mZW5jcnlwdGVkSWQ9QTA5OTczMzcxM1pFOFRNTUU0T1Y1JmVuY3J5cHRlZEFkSWQ9QTA5NzIwMjc5RTVXRVZTWExUR00md2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1'

import requests

response = requests.get(url)

response

custom_headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54",
'accept-language': 'en-GB,en;q=0.9',
}

response = requests.get(url,headers=custom_headers)

soup = BeautifulSoup(response.content, "lxml")

response.text

!pip install BeautifulSoup4

from bs4 import BeautifulSoup

title = soup.find_all('h1',{'id':'title'})

title

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
title = soup1.find_all('span',{'class':'a-size-large product-title-word-break'})

title






!pip install amazoncaptcha

from amazoncaptcha import AmazonCaptcha


page

title = soup1.find(id='productTitle')

title.text

price = soup2.find('span',{'class':"a-offscreen"}) 

price
