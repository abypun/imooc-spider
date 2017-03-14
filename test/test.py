# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

f = open("old/data.html", 'r') #　待处理文件
g = open("haha.html", 'w') # 目标文件
soup = BeautifulSoup(f.read(), 'html.parser')

# a = soup.find_all('div', class_="path")
# data = a[0].get_text().replace('\\', ' ')
# path = data.split()

# jianjie = soup.find_all('p', class_="auto-wrap")[0].get_text()

# chapters = []
# for i in soup.find_all('div', class_=re.compile('chapter (chapter-active)?')):
#     name =  ' '.join(i.strong.get_text().split()[0:2])
#     videos = []
#     for j in i.find_all('a'):
#         videos.append(' '.join(j.get_text().split()[0:3]))    
#     chapters.append({
#         'name': name,
#         'video': videos
#     })

teacher_name, teacher_job = soup.find_all('div', class_="teacher-info")[0].get_text().split()
tips = soup.find_all('dd', class_="autowrap")
tip1 = tips[0].get_text()
tip2 = tips[1].get_text()


f.close()
g.close()