from bs4 import BeautifulSoup
import urllib.request as req
import requests
import datetime

url = "https://finance.naver.com/marketindex/"
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

########## 방법 1 ##########
res1 = req.urlopen(url).read()
soup1 = BeautifulSoup(res1, 'html.parser')
raw_currency = soup1.select_one("#exchangeList > li.on > a.head.usd > div > span.value")
# currency = raw_currency.string

print(f'Date : {now} USD : {raw_currency.string} ')

########## 방법 2 ##########
res2 = requests.get(url)
soup2 = BeautifulSoup(res2.text, 'html.parser')
raw_currency2 = soup2.select_one("#exchangeList > li.on > a.head.usd > div > span.value")

print(f'Date : {now} USD : {raw_currency2.string} ')
