#https://wikidocs.net/77479

'''
import sys
from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
print("블록킹 로그인 완료")
'''

from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
import sys

class MyWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.dynamicCall("CommConnect()")
        self.ocx.OnEventConnect.connect(self.OnEventConnect)
    
    def OnEventConnect(self, err_code) :
        print(err_code)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()