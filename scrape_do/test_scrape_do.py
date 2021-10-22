import traceback

from __init__ import *

# create an web scrapper object
sample = python_sample()

# set the scrape.do api key
sample.set_api_token(api_token=API_TOKEN)

# Get Scrape.do account statistics
try:
    resp = sample.account_status()
    print("Response Type " + str(type(resp)))
    print(resp)
except ConnectionError as e:
    print(str(e))
    print(traceback.format_exc())

except Scrape_do_Exception as e:
    print(str(e))
    print(traceback.format_exc())

try:
    resp = sample.create_request_url(url=URL, method=METHOD, payload=PAYLOAD, headers=HEADERS,
                                         render=RENDER, super_proxies=SUPER_PROXIES, geo_code=GEO_CODE)
    print(resp.text)
except ConnectionError as e:
    print(str(e))
    print(traceback.format_exc())

except Scrape_do_Exception as e:
    print(str(e))
    print(traceback.format_exc())

