from DrissionPage import ChromiumPage
import time
from lxml import etree
page = ChromiumPage()
page.get("https://www.baidu.com")
textarea=page.ele("#kw").input("无名干员")
button=page.ele("#chat-submit-button").click()
time.sleep(2)
newpage=page.latest_tab
buttons=newpage.ele('xpath://div[@id="s_tab_inner"]/a[2]').click()
for i in range(3):
    page.scroll.to_bottom()
    newpage=page.latest_tab
    imgs=newpage.eles('xpath://div[@class="main-img-box-Eu2gv  "]//img')
    print(imgs)
    print(len(imgs))
    for img in imgs:
        img.save("无名")