from DrissionPage import ChromiumPage
import pandas
import time
from lxml import etree
page = ChromiumPage()
page.get("https://bj.ke.com/ershoufang/")
time.sleep(2)
lists=page.eles('xpath://ul[@class="sellListContent"]/li[@class="clear"]')
alldata=[]
for list in lists:
    info={"标题" :list.ele('xpath://div[@class="title"]').text,
   "地点":list.ele('xpath://div[@class="flood"]').text,
          "信息":list.ele('xpath://div[@class="houseInfo"]').text,
          "总价":list.ele('xpath://div[@class="totalPrice totalPrice2"]/span').text,
          "单价":list.ele('xpath://div[@class="unitPrice"]/span').text,
          "照片":list.ele('xpath://img[@class="lj-lazy"]').attr("src"),}
    print(info)
    alldata.append(info)
    df = pandas.DataFrame(alldata)
    df.to_excel("房价", index=False)

