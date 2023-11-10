import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import ToTextFile

txts = []

def extractTxts(source) :
    global txts
    
    #많은 타이틀이 news-tit아래 태그로 씌워져 있음
    tits = source.find_all("h2",class_="news-tit");

    for tit in tits:
        txt = tit.find("a").text
        txts.append(txt)

def extractLeadTxts(source) :
    global txts
    
    #많은 타이틀이 news-tit아래 태그로 씌워져 있음
    tits = source.find_all("p",class_="lead");
    for tit in tits:
        txts.append(tit.get_text())
        
def hankyong() :
    
    URL = "https://www.hankyung.com/"
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, "html.parser")
    
    
    '''
    한경닷컴 대문 정보들
    '''
    #위쪽 주제들
    results = soup.find("div",class_="main-top-wrap")
    extractTxts(results)
    
    #중간 메인 주제
    results = soup.find("article",class_="major-thumb-news")
    extractTxts(results)
    
    results = soup.find("section",class_=["main-component","series"]);
    extractTxts(results)
    
    results = soup.find("section",class_=["main-component","thepen"]);
    extractTxts(results)
    
    #major-news
    results = soup.find_all("article",class_="major-news");
    
    for result in results :
        extractTxts(result)
        
    #hkgroup-news
    results = soup.find_all("div",class_="hkgroup-news");
    
    for result in results :
        extractTxts(result)
    
def naver() :

    '''
    네이버 금융 속보
    '''
    URL = "https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258"
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, "html.parser")
    
    results = soup.find_all("dd",class_="articleSubject")
    
    for tit in results:
        txt = tit.find("a")
        txts.append(txt['title'])
        
def naverCurrentCurrency() :
    

hankyong()
naver()


#텍스트 파일로 추출한다
ToTextFile.printToText()

    
