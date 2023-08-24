import pandas as pd
from datetime import datetime
df = pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\Aditya\\Aditya_Arpit_Project.csv",index_col=0)
net = 0
x = 7
print("-------------------------------------------------------------------------------------------")
print ("                                       𝐀.𝐒 𝐒𝐏𝐎𝐑𝐓𝐒 𝐒𝐇𝐎𝐏                                        ")
print("----------------------------------------------------------------------------------------------")
name=input("𝙋𝙡𝙚𝙖𝙨𝙚 𝙀𝙣𝙩𝙚𝙧 𝙔𝙤𝙪𝙧 𝙍𝙚𝙨𝙥𝙚𝙘𝙩𝙚𝙙 𝙉𝙖𝙢𝙚       :")
phone_no = int(input("phone_no"))
while not name.isalpha():
    print("Invalid Name. Please Enter Alphabetic Characters Only")
    name=input("𝙋𝙡𝙚𝙖𝙨𝙚 𝙀𝙣𝙩𝙚𝙧 𝙔𝙤𝙪𝙧 𝙍𝙚𝙨𝙥𝙚𝙘𝙩𝙚𝙙 𝙉𝙖𝙢𝙚     :")
    phone_no=input("𝙋𝙡𝙚𝙖𝙨𝙚 𝙀𝙣𝙩𝙚𝙧 𝙔𝙤𝙪𝙧 𝙋𝙝𝙤𝙣𝙚 𝙉𝙪𝙢𝙗𝙚𝙧         :")
while not phone_no.isdigit() or len(phone_no) !=10:
        print("Invalid Phone Number. Please Enter A 10-Digit Numeric Value ")
        break
print()
print("-------------------------------------------------------------------------")
print("")
phone_no = int(phone_no)
selected_products = []
while True:
    print()
    print('''
          1) view PRODUCTS
          2) Purchase Item
          3) Exit''')
    print("-------------------------------------------------------------------------")
    ch = int(input('Choose any of the above option: '))
    if ch == 1:
        print(df)
    elif ch == 2:
        print(df)
        print("-----------------------------------------------------------------------------------------------------")
        print("                                             PURCHASE ITEMS                                          ")
        print("-----------------------------------------------------------------------------------------------------")
        itemls = []
        qtyls = []
        amtls=[]
        prc = int(input('Enter number of different items to purchase: '))
        for i in range(prc):
            eid = input('Enter item ID: ')
            itemls.append(eid)
            qty = int(input('Enter quantity: '))
            qtyls.append(qty)
            amt = df.loc[eid]['Rate']
            amtls.append(amt)
            net +=amt*qty
            bill = input('Do you want the bill to be displayed? Answer in Y/N: ').lower()
        if bill == 'y':
            print("🏏🏏🏏🏏🏏🏏🏏🏏🏏🏏🏏🏏🏏🏏 𝑨.𝑺 𝑺𝑷𝑶𝑹𝑻𝑺 𝑺𝑯𝑶𝑷 🏏🏏🏏🏏🏏🏏🏏🏏🏏🏏🏏🏏🏏🏏  ")
            print("\n                       𝟔𝟒𝟕𝑭/𝑫-𝟓𝟔, 𝑺𝑬𝑪𝑻𝑶𝑹-𝑯 , 𝑱𝒂𝒏𝒌𝒊𝒑𝒖𝒓𝒂𝒎                     ")
            print("                          𝒏𝒆𝒂𝒓 𝑺𝒂𝒉𝒂𝒓𝒂 𝑺𝒕𝒂𝒕𝒆,𝑳𝒖𝒄𝒌𝒏𝒐𝒘                        ")
            print("                             𝑷𝑰𝑵 𝒄𝒐𝒅𝒆 - 𝟐𝟐𝟔𝟎𝟐𝟏                          ")
            print("                          𝙋𝙝𝙤𝙣𝙚 𝙉𝙪𝙢𝙗𝙚𝙧 - 𝟗𝟖𝟓𝟔𝟒𝟑𝟗𝟎𝟐𝟔                       ")
            total_bill = 0
            bill_data = []
            current_datetime = datetime.now()
            print("")
            print("𝒀𝒐𝒖𝒓 𝑹𝒆𝒔𝒑𝒆𝒄𝒕𝒆𝒅 𝑵𝒂𝒎𝒆:",name)
            print("𝒀𝒐𝒖𝒓 𝑷𝒉𝒐𝒏𝒆 𝑵𝒖𝒎𝒃𝒆𝒓 :",phone_no)
            print("𝑫𝒂𝒕𝒆            :",current_datetime.strftime("%Y-%m-%d"))
            print("𝑻𝒊𝒎𝒆            :",current_datetime.strftime("%H:%M:%S"))
            print("")
            print("-----------------------------------------------------------------------------------------------------")
            billdf = pd.DataFrame({'𝐏𝐑𝐎𝐃𝐔𝐂𝐓':itemls,'𝙌𝙐𝘼𝙉𝙏𝙄𝙏𝙔':qtyls,'𝘼𝙈𝙊𝙐𝙉𝙏':amtls})
            print(billdf)
            print('Your total would be: ',net)
    elif ch == 3:
        break 
print('Thank You')