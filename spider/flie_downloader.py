# -*- coding: utf-8 -*-
import requests
import os
from conf import *
from time import sleep

class FileDownloader(object):
    def __init__(self, course_name, video_urls, quality='H'):
        self.name = course_name
        self.urls = video_urls
        self.quality = quality
        self.flag = True

        self.createdir()
        self.download()

    def createdir(self):
        if not os.path.exists(self.name):
            os.mkdir(self.name)
        # os.chdir(self.name)

    def download(self):
        for video in self.urls:
            video_path = self.name + os.sep + video['name']
            if os.path.exists(video_path):
                continue

            # print video[self.quality]
            print u'downloading ' + video['name']
            try:
                mp4 = requests.get(video[self.quality],stream=True, headers=headers, timeout=5).content
            except requests.exceptions.ConnectionError:
                print "Our Spider is probably being blocked by the IMOOC..."
                print "Mission [" + self.name + " - " + video['name'] + "] failed."
                print "Please try again!"
                self.flag = False
                return
            with open(video_path, 'wb') as mfile:
                mfile.write(mp4)
            sleep(5)


