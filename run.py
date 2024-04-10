from ourLogic import bond,kosdaq
from ourLibrary import ourConstant, toTextFile
import subprocess
import time


corporateBond = bond.checkCorporateBond()
nationalBond = bond.checkNationalBond()
kosDaq = kosdaq.checkKosdaq()

txts = []
txts.append('회사채 증감율 : ' + str(corporateBond))
txts.append('국채 증감율 : ' + str(nationalBond))
txts.append('코스닥 증감율 : ' + str(kosDaq))

print(txts)

# todayIndexCalResult = corporateBond*ourConstant.__corporate_bond_weight__ 
# todayIndexCalResult += nationalBond*ourConstant.__national_bond_weight__ 
# todayIndexCalResult += kosDaq*ourConstant.__kosdaq_weight__

# subprocess.run(["C:/Users/Administrator/AppData/Local/Programs/Python/Python37-32/python.exe", "c:/Users/Administrator/Desktop/makemoney-main/ourLibrary/__kiwoom__/version_check.py"])
# time.sleep(20)

# if todayIndexCalResult > ourConstant.__buying_criteria__ :
#     #do buy
#     print("We are going to buy top 100 kosdqp etf")
#     subprocess.run(["C:/Users/Administrator/AppData/Local/Programs/Python/Python37-32/python.exe","c:/Users/Administrator/Desktop/makemoney-main/ourLibrary/__kiwoom__/buy.py"])

# else :
#     print("I am sorry. It seems like today is not a good time to buy")
#     subprocess.run(["C:/Users/Administrator/AppData/Local/Programs/Python/Python37-32/python.exe","c:/Users/Administrator/Desktop/makemoney-main/ourLibrary/__kiwoom__/sell.py"])





    
