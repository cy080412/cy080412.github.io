from DrissionPage import ChromiumPage
import json
import pandas as pd
page=ChromiumPage()
page.get("https://www.zhaopin.com/jobs/?jl=539&kw=机械设计&order=4&el=4")
page.wait.doc_loaded()
body=page.ele('tag:body').html
print("准备爬取")
import os
from openai import OpenAI
prompt=f"""第一层，角色定位：
你是一个严谨的数据提取员，专门负责从复杂的HTML网页源码中精准提取结构化信息。

第二层，提取规则：
从用户提供的搜索页源码的body中，提取前15个岗位名称，公司名称，薪资，工作地点，学历要求。
提取要求：
1. 标题：提取完整标题文本。
2. 价格：只保留纯数字（去除“¥”、“$”等货币符号，以及“元”、“起”等中文单位，保留小数）。
3. 销量：提取商品的销量数据（如：“100人付款”、“200+人收货”等，保留原有格式或提取纯数字均可）。
4. 链接：提取商品对应的完整URL链接。
请遍历源码中所有的商品条目，确保不漏提取。

第三层，输出格式以及给出JSON范例：
以纯JSON数组格式返回结果，不要包含任何额外的解释性文字。
JSON范例：
[
  {{
    "title": "【示例】夏季纯棉短袖T恤",
    "price": 49.90,
    "sales": "500+人付款",
    "link": "https://item.taobao.com/item.htm?id=123456789"
  }}
]

第四层，容错处理：
如果在源码中未能找到某个商品的特定字段（如价格或销量），请将该字段的值设为null；如果源码中未能找到任何商品信息，请返回空数组 []，不要捏造数据。
待提取的的网页源码：{body}"""
client = OpenAI(
    api_key="",
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": prompt},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)
print("爬取完成")
print(response.choices[0].message.content)
res=response.choices[0].message.content
res_list=json.loads(res)
df=pd.DataFrame(res_list)
df.to_csv("机械本科，全江苏.csv",index=False)














