from ourLogic import bond,kosdaq
from ourLibrary import ourConstant, toTextFile, ourKiwoom

#오늘 코스닥, 채권 정보를 가지고 온다 (내용 추후 추가)
corporateBond = bond.checkCorporateBond()
nationalBond = bond.checkNationalBond()
kosDaq = kosdaq.checkKosdaq()

txts = []
txts.append('회사채 증감율 : ' + str(corporateBond))
txts.append('국채 증감율 : ' + str(nationalBond))
txts.append('코스닥 증감율 : ' + str(kosDaq))


todayIndexCalResult = corporateBond*ourConstant.__corporate_bond_weight__ 
todayIndexCalResult += nationalBond*ourConstant.__national_bond_weight__ 
todayIndexCalResult += kosDaq*ourConstant.__kosdaq_weight__

if todayIndexCalResult > ourConstant.__buying_criteria__ :
    #do buy
    print("We are going to buy top 100 kosdqp etf")
    ourKiwoom.startVersionCheck("cuu2252", "ch0509")
    ourKiwoom.buyMarketOrder("005930",1,1)

else :
    print("I am sorry. It seems like today is not a good time to buy")
    ourKiwoom.startVersionCheck("cuu2252", "ch0509")
    ourKiwoom.buyMarketOrder("005930",1,2)





    
