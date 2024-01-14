"""
created time: 2023-11-30
@author: jeongmoon
"""

from pykrx import stock
from ourLibrary import ourTime, ourConstant

""" 통계치 비교 --> derivedValue 에 100을 곱할지 결정해야 함!
날짜          최대증감율       최소증감율       derivedValue
24-01-14    -0.03           -0.89           96.62959218065386
"""

# 이틀 떨어지고 하루 올랐으면 매수에 가중치를 준다
# 1. 오늘 기준 2일 전과 비교해서 등략률
def checkKosdaq() :
    # 오늘 기준 2일 전과 비교
    df_2days = stock.get_index_price_change(ourTime.ago(-3), ourTime.ago(-2), "KOSDAQ")
    df_1days = stock.get_index_price_change(ourTime.ago(-2), ourTime.ago(-1), "KOSDAQ")

    등락률_2days = df_2days.iloc[1].등락률
    등락률_1days = df_1days.iloc[1].등락률

    최대증감율 = round(max(등락률_2days, 등락률_1days), 4)
    최소증감율 = round(min(등락률_2days, 등락률_1days), 4)

    derivedValue = (abs(최대증감율 - 최소증감율) / abs(최소증감율)) * 100
    return 1 if derivedValue > ourConstant.__kosdaq_bond_standard__ else 0

    # if df_2days < 0:    # 2일 연속 떨어졌을 때
    #     if df_1days > 0:  # 하루 올랐으면
    #         return 1   # 매수 ourConstant.__kosdaq_weight__
    #     else:   # 3일 연속 떨어졌으므로 매도
    #         return 0
