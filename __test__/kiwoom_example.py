from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()

accounts = kiwoom.GetLoginInfo("ACCNO")
print(f"Starts transaction with account number {accounts[0]}")

# kiwoom.SendOrder(
#     "시장가매수", #name
#     "0101", #키움 screen no
#     accounts[0], # account number
#     2, # 1: 매수, 2: 매도
#     "005930", #종목코드
#     10, #10주
#     0, #주문단가
#     "00", #00->지정가, 03-> 시장가
#     "" #원주문번호로 주문 정정시 사용합니다
# )

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

# while True:
#                 time.sleep(5)
#                 print("find open login window")
#                 caption = "Open API Login"
#                 hwnd = find_window(caption)
                
#                 if hwnd != 0 :
#                     time.sleep(2)
#                     edit_id = win32gui.GetDlgItem(hwnd, 0x3E8)
#                     edit_pass = win32gui.GetDlgItem(hwnd, 0x3E9)
#                     edit_cert = win32gui.GetDlgItem(hwnd, 0x3EA)
#                     btn_login = win32gui.GetDlgItem(hwnd, 0x1)

#                     double_click(15, 15, edit_id)
#                     enter_keys(edit_id, "cuu2252") 
#                     time.sleep(0.5)

#                     double_click(15, 15, edit_pass)
#                     enter_keys(edit_pass, "ch0509") 
#                     time.sleep(0.5)

#                     double_click(15, 15, edit_cert)
#                     enter_keys(edit_cert, "bydawn198627!") 
#                     time.sleep(1)

#                     click_button(btn_login)
#                     break