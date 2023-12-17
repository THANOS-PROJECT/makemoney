# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:00:30 2023

@author: cuu225
"""

from datetime import date, datetime, timezone, timedelta

# import sys
# sys.path.append(r'c:\users\admin\appdata\local\programs\python\python310\lib')

# import exchange_calendars as ecals

# XKRX = ecals.get_calendar("XKRX") # 한국 코드
# print(XKRX.is_session("2021-09-20")) # 2021-09-20 은 개장일인지 확인


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
    
    if gap < -7 or gap == 0 or gap > 7 :
        raise IndexError("We can't provide with that gap")
        
    KST = timezone(timedelta(hours=0)) #추후 오레곤 차이로 교체
    time_record = datetime.now(KST)
    temp_time_result = time_record + timedelta(days= ( gap ))
    
    if time_record.weekday() < 5 and temp_time_result.weekday() < 5 :
        return yyyymmdd(temp_time_result)
    
    #time record랑 temp사이 주말 갯수 세기
    count  = 0
    gapCount = 0
    if gap > 0 :
        while gapCount < gap :
            count += 1
            if getGabWeedDay(time_record, count) < 5:
                gapCount += 1
    elif gap < 0 :
        while gap < gapCount :
            count -= 1
            if getGabWeedDay(time_record, count) < 5:
                gapCount -= 1

    return yyyymmdd( time_record + timedelta( days = count ))