# -*- coding: utf-8 -*-
from time import sleep
from spider.course import Course
from spider.flie_downloader import FileDownloader

if __name__ == '__main__':
    # id = int(raw_input('Input your course id:'))
    for cid in [475, 397]:
        course = Course(cid)
        print "You are about to download [" + course.name + "]"
        print "The following are the videos you will download:"
        for video in course.videos:
            print video['name']
        print "---------------------------------"
        file_downloader = FileDownloader(course.name, course.videos)
        if file_downloader.flag:
            print "Mission completed"
        sleep(60)
