# -*- coding: utf-8 -*-
'''
将整节课程封装成一个Course类
name: 课程名字
id: 课程id
url: 课程链接
html:课程页面html源码
media:每节课的信息组成的字典列表
videos:待下载的视频字典列表
'''

import requests
from bs4 import BeautifulSoup
from conf import *


class Course(object):
    def __init__(self, cid):
        self.name = ''
        self.cid = cid
        self.url = "http://www.imooc.com/learn/" + str(cid)
        self.html = ""
        self.media = []
        self.videos = []

        self.get_media_info()

    def get_media_info(self):
        self.html = requests.get(self.url).content

        soup = BeautifulSoup(self.html, 'html.parser')
        self.name = soup.find_all('h2', class_="l")[0].get_text()
        links = soup.find_all('a', class_="J-media-item")
        for link in links:
            media_url = main_url + link['href']
            media_type, media_id = link['href'].split('/')[1:3]
            text = link.get_text().split()
            media_name = ' '.join(text[:2])
            # print media_url
            # print media_name

            if media_type == 'video':
                url = video_url.replace('{mid}', media_id)
                json = eval(requests.get(url).content)
                media_path = json['data']['result']['mpath']
                # need update
                l_mp4 = media_path[0].replace('\\', '')
                m_mp4 = media_path[1].replace('\\', '')
                h_mp4 = media_path[2].replace('\\', '')
                self.videos.append({
                    'name': media_name + '.mp4',
                    'L': l_mp4,
                    'M': m_mp4,
                    'H': h_mp4})

            self.media.append({
                'media_url': media_url,
                'media_name': media_name,
                'media_type': media_type,
                'media_id': media_id})



