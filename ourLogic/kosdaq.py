"""
created time: 2023-11-30
@author: jeongmoon
"""

import ourLibrary.toTextFile as toTextFile

from pykrx import stock
from pykrx import bond

from datetime import datetime, timedelta


# 이틀 떨어지고 하루 올랐으면 매수에 가중치를 준다
# 1. 오늘 기준 2일 전과 비교해서 등략률
def checkKosdaq() :
    return 0
    today = datetime.today().strftime("%Y%m%d")
    twoDaysAgo = (datetime.today() - timedelta(2)).strftime("%Y%m%d")

    df = stock.get_index_price_change(twoDaysAgo, today, "KOSDAQ")
    print(df.iloc[1].등락률)