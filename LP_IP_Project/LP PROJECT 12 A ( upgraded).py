import pandas as pd
from datetime import datetime
df = pd.read_csv('F:\\LP PROJECT\\LP PROJECT.csv')
net = 0
x = 7
while x > 1:
    print("-----------------------------------------------------------------------------------------------------")
    print("                                       L.P. CAR SHOWROOM                                       ")
    print("-----------------------------------------------------------------------------------------------------")
    print('''
          1) View Inventory
          2) Purchase Car
          3) Exit
    ''')
    ch = input('Choose any of the above option: ')
    if ch in ['1','2','3']:
        if ch == '1':
            print(df)
        elif ch == '2':
            print(df)
            print(
                "-----------------------------------------------------------------------------------------------------")
            print(
                "                                             PURCHASE CAR                                            ")
            print(
                "-----------------------------------------------------------------------------------------------------")
            itemls = []
            qtyls = []
            amtls = []
            C=[]
            prc = int(input('Enter number of different Cars to purchase: '))
            for i in range(prc):
                eid = input('Enter Car ID: ')
                A = list(df['CAR_ID'])
                if eid.upper() in A:
                    itemls.append(eid)
                    qty = int(input('Enter quantity: '))
                    qtyls.append(qty)
                    B=A.index(eid.upper())
                    amt = df.iat[B,3]
                    amtls.append(amt)
                    net += amt * qty
                    t=df.iat[B,1]
                    C.append(t)
                    bill = input('Do you want the bill to be displayed? Answer in Y/N: ').lower()
                    if bill == 'y':
                        print(
                            "-----------------------------------------------------------------------------------------------------")
                        print(
                            "                                                BILL                                                 ")
                        print(datetime.now())
                        print(
                            "-----------------------------------------------------------------------------------------------------")
                        billdf = pd.DataFrame({'CAR ID': itemls ,'CAR NAME':C,'QUANTITY': qtyls, 'AMOUNT': amtls})
                        print(billdf)
                        print('Your total would be: ', net)
                    elif bill== 'n':
                        print('SUCCESSFULLY PURCHASED') 
                    else:
                        print('PLS ENTER ONLY y/n')
                else:
                    print('PLEASE ENTER VALID CAR ID')


        elif ch == '3':
            break
    else:
        print('ENTER VALID CHOICE')
print('Thank You')
