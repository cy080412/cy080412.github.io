import requests

from lxml import etree



cyurl="https://www.diandingnnn.cc/ddk92482/73219338.html"
cyheaders={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 SLBrowser/9.0.8.7271 SLBChan/115 SLBVPV/64-bit"}
response=requests.get(url=cyurl,headers=cyheaders)

data=etree.HTML(response.text)


biaoti=data.xpath("//h1/text()")
print(biaoti[0])
zhengwen=data.xpath("//div[@id='content']/text()")



for hang in zhengwen:
    print(hang)
    print("\n")
    with open("小说.txt","a",encoding="utf-8") as f:
        f.write(hang+"\n")