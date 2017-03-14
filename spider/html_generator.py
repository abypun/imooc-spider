# -*- coding: utf-8 -*-
'''
generate a instruction.html for every cource
'''
import shutil
import os
class HtmlGenerator(object):
    def __init__(self, ):
        pass

    def generate(self, source_html, name):

        # need change
        srcPath = 'templates' + os.sep + 'imooc.html'
        destPath = name + os.sep + 'instruction.html'
        try:
            shutil.copy(srcPath,destPath)
        except:
            return

        with open(destPath, 'w') as f:
            raw = f.read()
            raw.replace('{{title}}', name)

            





            f.write(raw)