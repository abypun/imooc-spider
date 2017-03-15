# -*- coding: utf-8 -*-
'''
generate a instruction.html for every cource
'''
import os
from bs4 import BeautifulSoup
import re
class HtmlGenerator(object):
    def __init__(self, raw):
        self.raw = raw
        self.data = {}
        self.chapters = []
        self.distill()

    def distill(self):
        soup = BeautifulSoup(self.raw, 'html.parser')

        a = soup.find_all('div', class_="path")
        data = a[0].get_text().replace('\\', ' ')
        path = data.split()
        self.data['{{location1}}'] = path[1]
        self.data['{{location2}}'] = path[2]
        self.data['{{name}}'] = path[3]

        self.data['{{intro}}'] = soup.find_all('p', class_="auto-wrap")[0].get_text()

        for i in soup.find_all('div', class_=re.compile('chapter (chapter-active)?')):
            name =  ' '.join(i.strong.get_text().split()[0:2])
            videos = []
            for j in i.find_all('a'):
                videos.append(' '.join(j.get_text().split()[0:3]).replace(u' 开始学习', u' (code页面，前往慕课网进行练习)'))
            self.chapters.append({
                'name': name,
                'video': videos
            })

        self.data['{{teacher_name}}'], self.data['{{teacher_job}}'] = soup.find_all('div', class_="teacher-info")[0].get_text().split()
        tips = soup.find_all('dd', class_="autowrap")
        self.data['{{tip1}}'] = tips[0].get_text()
        self.data['{{tip2}}'] = tips[1].get_text()

    def generate(self):

        srcPath = 'templates' + os.sep + 'imooc.html'
        destPath = self.data['{{name}}'] + os.sep + 'instruction.html'
        if not os.path.exists(self.data['{{name}}']):
            os.mkdir(self.data['{{name}}'])

        with open(srcPath, 'r') as f:
            ins = f.read()
            for key, value in self.data.iteritems():
                ins = ins.replace(key, value.encode('UTF-8'))
        
            content = ''
            for chapter in self.chapters:
                source1 = '''
                <div class="chapter chapter-active">
                    <h3>
                        <strong>
                            {{name}}
                        </strong>
                    </h3>
                    {{video}}
                </div>
                '''
                source1 = source1.replace('{{name}}', chapter['name'])
                unit = ''
                for video_name in chapter['video']:
                    source2 = '''
                    <ul class="video">
                        <li data-media-id="00000">
                            <a href='#' class="J-media-item">
                                {{video_name}}
                            </a>
                        </li>
                    </ul>
                    '''
                    source2 = source2.replace('{{video_name}}', video_name)
                    unit = unit + source2
                source1 = source1.replace('{{video}}', unit)
                content = content + source1
            ins = ins.replace('{{content}}', content.encode('UTF-8'))
            with open(destPath, 'w') as g:
                g.write(ins)