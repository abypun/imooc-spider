# -*- coding: utf-8 -*-
import os
import threading
import sys
import conf
import requests


class File_Downloader(threading.Thread):
    def __init__(self,fileInfo):
        threading.Thread.__init__(self)
        self.filedir = fileInfo['course_name']
        self.chapter = fileInfo['chapter']
        self.createdir()
        self.run()

    def createdir(self):
        if not os.path.exists(self.filedir):
            os.mkdir(self.filedir)

    def run(self):
        os.chdir(self.filedir)
        for media in self.chapter:
            if media['media_type'] == 'video':
                filepath = media['media_name'] + '.mp4'
                print filepath
                for url in media['media_path']:
                    if url.find('H.mp4'):
                        mp4 = requests.get(url.replace('\\', ''), stream=True).content
                        with open(filepath, 'wb') as file:
                            file.write(mp4)



    #下载任务
    def Schedule(self,blocknum,blocksize,totalsize):
        '''''
        blocknum:已经下载的数据块
        blocksize:数据块的大小
        totalsize:远程文件的大小
        '''
        per = 100.0 * blocknum * blocksize / totalsize
        if per > 100 :
            per = 100
        conf.LOCK.acquire()
        conf.PERLIST[self.__id]= per # 记录每个线程的下载百分比，用于计算整个的进度状况
        nowsum = 0 # 当前的进度
        for item in conf.PERLIST:
            nowsum+=item
        str = u'当前下载进度:---------------->>>>>>>> %.2f%%' % (100*nowsum/conf.PERSUM)
        sys.stdout.write(str+"\r")
        sys.stdout.flush()
        conf.LOCK.release()










