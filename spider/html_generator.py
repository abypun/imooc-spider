# -*- coding: utf-8 -*-
'''
generate a instruction.html for every cource
'''
import shutil
import os
from bs4 import BeautifulSoup
import re
class HtmlGenerator(object):
    def __init__(self, raw, ):
        self.data = {}

    def distill(self):
        soup = BeautifulSoup(self.raw, 'html.parser')

        a = soup.find_all('div', class_="path")
        data = a[0].get_text().replace('\\', ' ')
        self.path = data.split()
        self.name = self.path[3]

        self.intro = soup.find_all('p', class_="auto-wrap")[0].get_text()

        for i in soup.find_all('div', class_=re.compile('chapter (chapter-active)?')):
            name =  ' '.join(i.strong.get_text().split()[0:2])
            videos = []
            for j in i.find_all('a'):
                videos.append(' '.join(j.get_text().split()[0:3]))    
            self.chapters.append({
                'name': name,
                'video': videos
            })

        self.teacher_name, self.teacher_job = soup.find_all('div', class_="teacher-info")[0].get_text().split()
        tips = soup.find_all('dd', class_="autowrap")
        self.tip1 = tips[0].get_text()
        self.tip2 = tips[1].get_text()

    def generate(self):

        # need change
        srcPath = 'templates' + os.sep + 'imooc.html'
        destPath = self.name + os.sep + 'instruction.html'
        try:
            shutil.copy(srcPath,destPath)
        except:
            return

        with open(destPath, 'w') as f:
            ins = f.read()
            ins.replace('{{title}}', self.name)
            ins.replace('{{location1}}', self.path[1])
            ins.replace('{{location2}}', self.path[2])
            ins.replace('{{intro}}', self.intro)
            ins.replace('{{intro}}', self.intro)

            





            f.write(raw)