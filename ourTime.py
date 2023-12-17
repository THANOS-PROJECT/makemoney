# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:00:30 2023

@author: cuu225
"""

from datetime import date, datetime, timezone, timedelta

# 휴장일인지 여부 확인
import exchange_calendars as ecals
XKRX = ecals.get_calendar("XKRX") # 한국 코드

# n일전 날짜를 "yyyymmdd"형태로 구한다
# 주어진 날을 계산했을때 토요일, 일요일이면 전주 금요일 값을 return 한다

def yyyymmdd(timedelta) :
    return str(timedelta)[:10].replace("-","")

def getGabWeedDay(from_,gapDays):
    return (from_ + timedelta(days= ( gapDays ))).weekday()
    
def ago(gap : int):
    
    #1주전, 1주 후까지만 케어한다
    if type(gap) != int :
        raise TypeError("Gap must be integer")
        return
    
    if gap < -7 or  gap == 0 or gap > 7 :
        raise IndexError("We can't provide with that gap")
        
    KST = timezone(timedelta(hours=0)) #추후 오레곤 차이로 교체
    today = datetime.now(KST)
    gapDaysAgo = today + timedelta(days= ( gap ))
    
    if today.weekday() < 5 and gapDaysAgo.weekday() < 5 :
        return yyyymmdd(gapDaysAgo)
    
    #time record랑 temp사이 주말 갯수 세기
    holidayIncludedCount  = 0
    index = 0
    if gap > 0 :
        while index < gap :
            holidayIncludedCount += 1
            if getGabWeedDay(today, holidayIncludedCount) < 5 or XKRX.is_session(today):   # 해당 날짜가 휴장일인지도 추가 확인
                index += 1
    elif gap < 0 :
        while gap < index :
            holidayIncludedCount -= 1
            if getGabWeedDay(today, holidayIncludedCount) < 5 or XKRX.is_session(today):   # 해당 날짜가 휴장일인지도 추가 확인
                index -= 1

    return yyyymmdd( today + timedelta( days = holidayIncludedCount ))