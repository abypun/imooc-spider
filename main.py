#!D:\Python27\python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from file_downloader import File_Downloader

main_url = 'http://www.imooc.com'
# user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) "
#               "AppleWebKit/537.36 (KHTML, like Gecko) "
#               "Chrome/36.0.1985.143 Safari/537.36")
# headers = {
#     'User-Agent': user_agent,
#     'Referer': main_url,
# }
data = []

def get_content(course_id):
    # 通过课程ID获取所有视频和教学页面的完整地址和相应名称
    course_url = 'http://www.imooc.com/learn/' + course_id
    cont = requests.get(course_url).content
    # cont = requests.get(course_url, headers=login_headers).content
    soup = BeautifulSoup(cont, 'html.parser')
    links = soup.find_all('a', class_="J-media-item")
    for link in links:
        media_url = main_url + link['href']
        media_type, media_id = link['href'].split('/')[1:3]
        text = link.get_text().split()
        media_name = ' '.join(text[:2])
        # print media_url
        # print media_name
        data.append({'media_url': media_url, 'media_name': media_name, 'media_type': media_type, 'media_id': media_id})

def get_source():
    for content in data:
        if content['media_type'] == 'video':
            json_url = 'http://www.imooc.com/course/ajaxmediainfo/?mid={mid}&mode=flash'.replace('{mid}', content['media_id'])
            json = requests.get(json_url).content
            content['media_path'] = eval(json)['data']['result']['mpath']


if __name__ == '__main__':
    get_content('747')
    get_source()
    for i in data:
        print i
    course_name = u'Python-面向对象'
    course = {'course_name': course_name, 'chapter': data}
    downloader = File_Downloader(course)