import requests
from lxml import etree
import json
import time

sousuo_url = 'https://www.gequbao.com/s/周杰伦'
music_headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'
}
sousuo_resp = requests.get(url=sousuo_url,headers=music_headers)
tree = etree.HTML(sousuo_resp.text)
a_tags = tree.xpath('//a[@class="hover-zoom d-block text-decoration-none"]')
for a in a_tags:
    detail_url = a.xpath('./@href')[0]
    detail_url = 'https://www.gequbao.com' + detail_url
    music_name = a.xpath('./@title')[0]
    print(f'开始下载{music_name}...')
    detail_resp = requests.get(url=detail_url, headers=music_headers)
    detail_result = detail_resp.text
    print(detail_result)
    str1 = detail_result.split('\\u0022play_id\\u0022:\\u0022')[1]
    # print(str1)
    play_id = str1.split('\\u0022')[0]
    # print(play_id)
    play_data = {
        "id": play_id
    }
    # 请求网址
    play_url = 'https://www.gequbao.com/member/common-play-url'
    # 携带参数发送post请求
    play_resp = requests.post(url=play_url, data=play_data, headers=music_headers)
    print(play_resp.text) # 得到的是json字符串