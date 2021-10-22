import traceback

from __init__ import *
from bs4 import BeautifulSoup
import requests
import re

# create an web scrapper object
sample = python_sample()

# set the scrape.do api key
sample.set_api_token(api_token=API_TOKEN)

# Get Scrape.do resutl
try:
    # Get Scrape.do resutl
    resp = sample.create_request_url(url=URL, method=METHOD, payload=PAYLOAD, headers=HEADERS,
                                         render=RENDER, super_proxies=SUPER_PROXIES, geo_code=GEO_CODE)
    # Get Scrape.do resutl
    soup = BeautifulSoup(resp.text, 'html.parser')

    # title タグの文字列を取得する
    title_text = soup.find('title').get_text()
    print('-----タイトル-----')
    print(title_text)

    # ページに含まれるリンクを全て取得する
    links = [url.get('href') for url in soup.find_all('a')]
    print('-----リンク-----')
    print(links)
    
    # class が copyrightのtextを取得する
    copyright = soup.find('p', {'class': 'copyright'}).get_text(strip=True)
    print('-----コピーライト-----')
    print(copyright)

except ConnectionError as e:
    print(str(e))
    print(traceback.format_exc())

except Scrape_do_Exception as e:
    print(str(e))
    print(traceback.format_exc())
