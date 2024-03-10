from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

accounts = kiwoom.GetLoginInfo("ACCNO")
print(accounts[0])

kiwoom.SendOrder(
    "시장가매수", #name
    "0101", #키움 screen no
    accounts[0], # account number
    2, # 1: 매수, 2: 매도
    "005930", #종목코드
    10, #10주
    0, #주문단가
    "00", #00->지정가, 03-> 시장가
    "" #원주문번호로 주문 정정시 사용합니다
)

kiwoom.SendOrder(
    "지정가매수", #name
    "0101", #키움 screen no
    accounts[0], # account number
    1, # 1: 매수, 2: 매도
    "005930", #종목코드
    1, #10주
    74000, #주문단가
    "00", #00->지정가, 03-> 시장가
    "" #원주문번호로 주문 정정시 사용합니다
)