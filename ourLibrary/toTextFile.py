# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:56:02 2023

@author: cuu225
"""
from datetime import datetime

def printDerivedLogic(txts) :
    fileName = datetime.now().strftime("Logic_%Y_%m_%d_%H")
    print(fileName)

    #fileFullPath = f'C:/Users/Admin/Desktop/makemoney_prj/{fileName}.txt'
    fileFullPath = f'C:/Users/cuu22/Desktop/private/{fileName}.txt'

    #txt 모아서 파일로 만들기
    with open('C:/Users/cuu22/Desktop/private/'+fileName+'.txt', "w",encoding='UTF-8') as f:
        for txt in txts:
            print(txt)
            f.write(f"{txt}\n")

def printToText(txts):
    # global txts
    
    fileName = datetime.now().strftime("%Y_%m_%dT%H_%M_%S")
    print(fileName)

    #fileFullPath = f'C:/Users/Admin/Desktop/makemoney_prj/{fileName}.txt'
    fileFullPath = f'C:/Users/cuu22/Desktop/private/{fileName}.txt'
    print(fileFullPath)
    
    #txt 모아서 파일로 만들기
    with open(fileFullPath, "w",encoding='UTF-8') as f:
        for txt in txts:
            print(txt)
            f.write(f"{txt}\n")
