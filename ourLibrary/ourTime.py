# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:00:30 2023

@author: cuu225
"""

from datetime import date, datetime, timezone, timedelta
import exchange_calendars as ecals# 휴장일인지 여부 확인

XKRX = ecals.get_calendar("XKRX") # 한국 코드

def extractDate(timedelta, removeDash : bool = True) : # n일전 날짜를 "yyyymmdd"형태로 구한다
    return str(timedelta)[:10].replace("-","") if removeDash else str(timedelta)[:10]

def getGapDate(from_,gapDays):
    return (from_ + timedelta(days= ( gapDays )))

'''
#time record랑 temp사이 주말 갯수 세기
#우리 프로그램은 주말은 날짜로 고려하지 않는다
'''
def getHolidayIncludedCount(gap, today) :
    holidayIncludedCount  = 0
    index = 0
    isTryingToGetDayAfter = gap > 0 


    if isTryingToGetDayAfter :
        while index < gap :
            holidayIncludedCount += 1
            gapDate = getGapDate(today, holidayIncludedCount)
            extractedDate = extractDate(gapDate, removeDash=False)
            if gapDate.weekday() < 5 or XKRX.is_session(extractedDate):   # 해당 날짜가 휴장일인지도 추가 확인
                index += 1
    else :
        while gap < index :
            holidayIncludedCount -= 1
            gapDate = getGapDate(today, holidayIncludedCount)
            extractedDate = extractDate(gapDate, removeDash=False)
            if  gapDate.weekday()  < 5 or XKRX.is_session(extractedDate):   # 해당 날짜가 휴장일인지도 추가 확인
                index -= 1
    
    return holidayIncludedCount
                
def ago(gap : int):
    KST = timezone(timedelta(hours=0)) #추후 오레곤으로 서버시간 수정필요
    today = datetime.now(KST)

    if type(gap) != int : #-1일전, 1일전 등 숫자 형태가 아니면 throw error
        raise TypeError("Gap must be integer")
        return
    
    if gap < -7 or  gap == 0 or gap > 7 :  #1주전, 1주 후까지만 케어한다
        raise IndexError("We can't provide with that gap")

    gapDaysAgo = getGapDate(today,gap)
    
    if today.weekday() < 5 and gapDaysAgo.weekday() < 5 : #오늘이 주말이 아니고, 계산한 값도 주말이 아니면 리턴
        return extractDate(gapDaysAgo)
    else:
         return extractDate( today + timedelta( days = getHolidayIncludedCount(gap, today) ))