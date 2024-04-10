
import ourLibrary.ourTime as ourTime
import ourLibrary.ourConstant as ourConstant

from pykrx import bond
        
def checkNationalBond() :
    #국채 10년물의 3일치를 보고 3일치가 하락 중이라면 매도에 가중치를 준다
    #1일전 YYYYMMDD
    #3일전 YYYYMMDD
    df = bond.get_otc_treasury_yields(ourTime.ago(-3), ourTime.ago(-1), "국고채10년")

    #제일큰 하락율 - 제일 작은 하락율 / 제일 큰 하락율 * 100 * 0.4 (채권 가중치)
    #print(df)
    #print(df.iloc)
    #print(df.iloc[1].대비)
    증감율 = df['대비'].to_numpy()
    최대증감율 = max(증감율, key=abs)
    최소증감율 = min(증감율, key=abs)
    derivedValue = ( abs( 최대증감율 - 최소증감율 ) / abs(최소증감율) )

    print("checkNationalBond.derivedValue : ", derivedValue)

    return 1 if derivedValue > ourConstant.__bond_standard__ else 0

def checkCorporateBond():
    #회사채 AA( 회사채 AA-(무보증 3년) )의 지수가 떨어지면 매수의 가중치를 준다
    ratios = []
    
    for i in range(1,4) :
        df = bond.get_otc_treasury_yields(ourTime.ago(-1 * i))
        ratios.append(df.loc['회사채 AA-(무보증 3년)']['대비'])
    
    
        
    최대증감율 = max(ratios, key=abs)
    최소증감율 = min(ratios, key=abs)
    
    derivedValue = ( abs( 최대증감율 - 최소증감율 ) / abs(최대증감율) ) * 100

    print("checkCorporateBond.derivedValue : ", derivedValue)

    return 1 if derivedValue > ourConstant.__corporate_bond_standard__ else 0