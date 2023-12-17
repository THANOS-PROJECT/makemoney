import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import toTextFile
import ourTime

from pykrx import stock
from pykrx import bond


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
    URL = ''
    page = ''
        
def checkBond() :
    #국채 10년물의 3일치를 보고 3일치가 하락 중이라면 매도에 가중치를 준다
    #1일전 YYYYMMDD
    #3일전 YYYYMMDD
    df = bond.get_otc_treasury_yields(ourTime.ago(-3), ourTime.ago(-1), "국고채10년")
    #print(df.head())
    
    #제일큰 하락율 - 제일 작은 하락율 / 제일 큰 하락율 * 100 * 0.4 (채권 가중치)
    print(df)
    print(df.iloc)
    print(df.iloc[1].수익률)

#hankyong()
#naver()

checkBond()

#toTextFile.printToText(txts)


    
