from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()

accounts = kiwoom.GetLoginInfo("ACCNO")

kiwoom.SendOrder(
    "시장가매도", #name
    "0101", #키움 screen no
    accounts[0], # account number
    2, # 1: 매수, 2: 매도
    "069500", #종목코드 kodex 200
    1, #10주
    0, #주문단가
    "03", #00->지정가, 03-> 시장가
    "" #원주문번호로 주문 정정시 사용합니다
)