# -*- coding: utf-8 -*-
import requests
import os
class File_Downloader(object):
    def __init__(self, course_name, video_urls):
        self.name = course_name
        self.urls = video_urls
        self.quality = 'H_mp4'

        self.download()

    def download(self):
        if not os.path.exists(self.name):
            os.mkdir(self.name)
        os.chdir(self.name)

        for video in self.urls:
            print u'downloading ' + video['name']

            mp4 = requests.get(video[self.quality], stream=True).content
            with open(video['name'], 'wb') as mfile:
                mfile.write(mp4)



