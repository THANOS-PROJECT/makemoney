"""
created time: 2023-11-30
@author: jeongmoon
@알고리즘
    1. 이틀 떨어지고 하루 올랐으면 매수에 가중치를 준다
    2. 3일 연속 떨어졌다면 매도에 가중치를 준다
"""

from pykrx import stock
from ourLibrary import ourTime, ourConstant

""" 통계치 비교 --> derivedValue 에 100을 곱할지 결정해야 함!
날짜          최대증감율       최소증감율       derivedValue
24-01-14    -0.03           -0.89           96.62959218065386   (100 곱했음)
"""

def checkKosdaq() :
    # 오늘 기준 3일전, 2일전, 1일전의 증감율 데이터를 읽어온다.
    df_2days = stock.get_index_price_change(ourTime.ago(-3), ourTime.ago(-2), "KOSDAQ") # 3일 전 ~ 2일 전 데이터 읽어오기
    df_1days = stock.get_index_price_change(ourTime.ago(-2), ourTime.ago(-1), "KOSDAQ") # 2일 전 ~ 1일 전 데이터 읽어오기

    print(df_1days)
    print(df_2days.iloc[1])

    return 1

    등락률_2days = df_2days.iloc[1].등락률
    등락률_1days = df_1days.iloc[1].등락률

    # 소수점 자리가 길어서 3번째 자리까지 반올림 처리 해줌
    최대증감율 = round(max(등락률_2days, 등락률_1days), 4)
    최소증감율 = round(min(등락률_2days, 등락률_1days), 4)


    derivedValue = (abs(최대증감율 - 최소증감율) / abs(최소증감율)) * 100
    print("checkKosdaq.derivedValue : ", derivedValue)

    return 1 if derivedValue > ourConstant.__kosdaq_bond_standard__ else 0