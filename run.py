from ourLogic import bond,kosdaq
from ourLibrary import ourConstant

#오늘 코스닥, 채권 정보를 가지고 온다 (내용 추후 추가)
corporateBond = bond.checkCorporateBond()
nationalBond = bond.checkNationalBond()
kosDaq = kosdaq.checkKosdaq()

todayIndexCalResult = corporateBond*ourConstant.__corporate_bond_weight__ 
todayIndexCalResult += nationalBond*ourConstant.__national_bond_weight__ 
todayIndexCalResult += kosDaq*ourConstant.__kosdaq_weight__

if todayIndexCalResult > ourConstant.__buying_criteria__ :
    #do buy
    print("We are going to buy top 100 kosdqp etf")
else :
    print("I am sorry. It seems like today is not a good time to buy")





    
