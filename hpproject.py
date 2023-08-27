import pandas as pd
from datetime import datetime 
df = pd.read_csv('C:\\Users\\Asus\\lakshya ok\\hp.csv',index_col=0)
net = 0
x = 7
while x>1:
    print("-----------------------------------------------------------------------------------------------------")
    print ("                                      H.P. FLIGHT MANAGEMENT                                ")
    print("-----------------------------------------------------------------------------------------------------")
    print('''
          1) View FLIGHT
          2) Purchase TICKET
          3) Exit
    ''')
    ch = int(input('Choose any of the above option: '))
    if ch == 1:
        print(df)
    elif ch == 2:
        print(df)
        print("-----------------------------------------------------------------------------------------------------")
        print("                                             PURCHASE TICKET                                         ")
        print("-----------------------------------------------------------------------------------------------------")
        itemls = []
        qtyls = []
        amtls=[]
        ab=[]
        fi=[]
        tq=[]
        dq=[]
        aq=[]
        prc = int(input('Enter number of different flights ticket you want to purchase'))
        for i in range(prc):
            eid = input('Enter flightid: ')
            itemls.append(eid)
            qty = int(input('Enter no. of tickets : '))
            qtyls.append(qty)
            amt = df.loc[eid]['price']
            amtls.append(amt)
            net +=amt*qty 
            t=df.loc[eid]['Airline']
            ab.append(t)
            zx=df.loc[eid]['from']
            fi.append(zx)
            wq=df.loc[eid]['to']
            tq.append(wq)
            evc=df.loc[eid]['departure time']
            dq.append(evc)
            yu=df.loc[eid]['arrival time']
            aq.append(yu)

        bill = input('Do you want the bill to be displayed? Answer in Y/N: ').lower()
        if bill == 'y':
            print("-----------------------------------------------------------------------------------------------------")
            print("                                                BILL                                                 ")
            print(datetime.now())
            print("-----------------------------------------------------------------------------------------------------")
            billdf = pd.DataFrame({'Flightid':itemls,'Airline':ab,'From':fi,'To':tq,'Departure time':dq,'arrival time':aq,'No. of ticket':qtyls,'AMOUNT':amtls})
            print(billdf)
            print('Your total would be: ',net)
    elif ch == 3:
        break
print('Thank You')
     