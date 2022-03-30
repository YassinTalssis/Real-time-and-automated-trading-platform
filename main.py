
#import pandas as pd
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

def web_content_div(web_content, class_path):
    web_content_div = web_content.find_all('div', {'class': class_path})
    #print(web_content_div)
    try:
        spans = web_content_div[0].find_all('span')
        texts =[span.get_text() for span in spans]
    except IndexError:
        texts=[]
    return texts


def real_time_price(stock_code):
    url= 'https://finance.yahoo.com/quote/' + stock_code
    try:
        r = requests.get(url)
        page_content = BeautifulSoup(r.text,'lxml')
        price= page_content.find_all('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})[0].get_text()
        texts = web_content_div(page_content,"My(6px) Pos(r) smartphone_Mt(6px) W(100%)")
        if texts!=[]:
           change1, change2 = texts[0], texts[1]
        else:
            change1,change2 = [],[]
    except ConnectionError:
        price=0
        change1, change2 = [],[]
    return price, change1, change2

stocks = ['GOOG', 'AAPL', 'MSFT', 'GME']
for i in stocks:
    print(real_time_price(i))


#url= 'https://finance.yahoo.com/quote/' + stocks[0]
#r = requests.get(url)
#page_content = BeautifulSoup(r.text,'lxml')



