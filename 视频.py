import requests
import re
from moviepy import VideoClip, VideoFileClip
from lxml import etree





cyurl="https://www.bilibili.com/video/BV1HytN6dEqG/?spm_id_from=333.1007.tianma.3-2-6.click"
cyheaders={"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 SLBrowser/9.0.8.7271 SLBChan/115 SLBVPV/64-bit",
         "Referer":"https://www.bilibili.com/video/BV1Psui6NELL/?spm_id_from=333.1007.tianma.1-1-1.click",
"Cookie":"buvid3=326FF997-A559-D6D6-76D5-02D1231E239102123infoc; b_nut=1786972502; _uuid=6639E9B2-71C6-63A6-91010F-83108862EDFF202651infoc; CURRENT_QUALITY=0; buvid_fp=180e8e009b223aa2e14f39b15ce5f139; buvid4=89564B9D-CEF8-03E4-1BE8-100A6C29D85210743-026070119-5qKvtI0ksp+HAr0dDClKcfIDKQVcSymYkYfBu7EWJDX4aBI/0/0x5sTnGiEHWG47; rpdid=0zbfAHHg7D|Yg0xz5Hq|4cT|3w1WVXbb; bsource=search_baidu; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODgxODM4OTksImlhdCI6MTc4NzkyNDYzOSwicGx0IjotMX0.JYF_2loaakcohrwzX5XFTm7TZ-6-HgqpjLUwyjnlOcU; bili_ticket_expires=1788183839; sid=821pq7r6; home_feed_column=5; browser_resolution=1658-914; CURRENT_FNVAL=4048; b_lsid=3983FD2D_1A048A5FECC"

}
response=requests.get(cyurl,headers=cyheaders)
tree=etree.HTML(response.text)
name=tree.xpath('//div[@class="video-info-title-inner"]//@title')




gz=r'"baseUrl":"(.+?)"'
result=re.findall(gz,response.text)
#print(result)
videourl=result[0]
print(videourl)
audiourl=result[-1]
print(audiourl)
videofile=requests.get(url=videourl)
audiofile=requests.get(url=audiourl)
with open("video.mp4","wb") as f:
    f.write(videofile.content)
    print("视频下载完成")
with open("audio.mp3","wb") as f:
    f.write(audiofile.content)
    print("音频下载完成")
video=VideoFileClip("video.mp4")
video.write_videofile(f"{name[0]}.mp4",audio="audio.mp3")

