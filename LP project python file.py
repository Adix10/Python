import pandas as pd
from datetime import datetime 
df = pd.read_csv('D:\\LP PROJECT FOLDER\\LP PROJECT.csv',index_col=0)
net = 0
x = 7
while x>1:
    print("-----------------------------------------------------------------------------------------------------")
    print ("                                       L.P. CAR SHOWROOM                                       ")
    print("-----------------------------------------------------------------------------------------------------")
    print('''
          1) View Inventory
          2) Purchase Car
          3) Exit
    ''')
    ch = int(input('Choose any of the above option: '))
    if ch == 1:
        print(df)
    elif ch == 2:
        print(df)
        print("-----------------------------------------------------------------------------------------------------")
        print("                                             PURCHASE CAR                                            ")
        print("-----------------------------------------------------------------------------------------------------")
        itemls = []
        qtyls = []
        amtls=[]
        prc = int(input('Enter number of different Cars to purchase: '))
        for i in range(prc):
            eid = input('Enter Car ID: ')
            itemls.append(eid)
            qty = int(input('Enter quantity: '))
            qtyls.append(qty)
            amt = df.loc[eid]['Rate']
            amtls.append(amt)
            net +=amt*qty
        bill = input('Do you want the bill to be displayed? Answer in Y/N: ').lower()
        if bill == 'y':
            print("-----------------------------------------------------------------------------------------------------")
            print("                                                BILL                                                 ")
            print(datetime.now())
            print("-----------------------------------------------------------------------------------------------------")
            billdf = pd.DataFrame({'CAR':itemls,'QUANTITY':qtyls,'AMOUNT':amtls})
            print(billdf)
            print('Your total would be: ',net)
    elif ch == 3:
        break
print('Thank You')
     