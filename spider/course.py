# -*- coding: utf-8 -*-
'''
将整节课程封装成一个Course类
'''

import requests
from bs4 import BeautifulSoup
main_url = 'http://www.imooc.com'


class Course(object):
    def __init__(self, id):
        self.name = ''
        self.id = id
        self.url = "http://www.imooc.com/learn/" + str(id)
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
                json_url = 'http://www.imooc.com/course/ajaxmediainfo/?mid={mid}&mode=flash'.replace('{mid}', media_id)
                json = eval(requests.get(json_url).content)
                media_path = json['data']['result']['mpath']
                # need update
                l = media_path[0].replace('\\', '')
                m = media_path[1].replace('\\', '')
                h = media_path[2].replace('\\', '')
                self.videos.append({'name': media_name + '.mp4', 'L_mp4': l, 'M_mp4': m, 'H_mp4': h})
            self.media.append({'media_url': media_url, 'media_name': media_name, 'media_type': media_type, 'media_id': media_id})



