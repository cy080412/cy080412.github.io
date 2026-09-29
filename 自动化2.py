from DrissionPage import ChromiumPage
import time
from lxml import etree

import os
page = ChromiumPage()
page.listen.start("https://so.xiaohongshu.com/api/sns/web/v2/search/notes",method="POST")
page.get("https://www.xiaohongshu.com/search_result_ai?keyword=足球推荐&source=web_explore_feed&type=51")
#https://www.xiaohongshu.com/search_result_ai?keyword=%25E8%25B6%25B3%25E7%2590%2583%25E9%259E%258B%25E6%258E%25A8%25E8%258D%2590&source=web_explore_feed
#https://www.xiaohongshu.com/search_result_ai?keyword=%25E8%25B6%25B3%25E7%2590%2583%25E9%259E%258B&source=web_explore_feed
#page.listen.start("https://so.xiaohongshu.com/api/sns/web/v2/search/notes",method="POST")
alldata=[]
for i in range(3):
    print(i)
    time.sleep(3)
    #page.listen.start("https://so.xiaohongshu.com/api/sns/web/v2/search/notes", method="POST")


    page.scroll.to_bottom()

    response=page.listen.wait()
    print(response.response.body)
    result=response.response.body
    items=result['data']['items']
    for item in items:
        try:
            title=item['note_card']["display_title"]
            nickname=item['note_card']["interact_info"]["liked_count"]
            print(title,nickname)
        except Exception as e:
            print(e)

