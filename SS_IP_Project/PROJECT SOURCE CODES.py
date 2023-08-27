import pandas as pd
from tabulate import tabulate
import datetime
data = pd.read_csv("D:\STATIONARY PROJECT .csv")
df = pd.DataFrame(data)
df.index += 1
df.drop(columns=['Serial Number'],inplace=True)
print(" 📚📚📚📚📚📚📚📚📚📚📚📚📚📚📚📚 SS STATIONARY 📚📚📚📚📚📚📚📚📚📚📚📚📚📚📚📚📚📚📚")
print(df)
print("🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏Welcome to SS STATIONARY🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏")
name=input("Please Enter Your Respected Name       :")
while True:
    phone_no=input("Please Enter Your Phone Number         :")
    if not phone_no.isdigit():
        print("Invalid input for name . Please enter valid phone number ")
    else:
        phone_no=int(phone_no)
    if len(str(phone_no))!=10:
        print("phone number must be exactly 10-digit.Please enter a valid number")
    else:
        break
print()
print("-------------------------------------------------------------------------")
print("")
phone_no = int(phone_no)
selected_products = []
while True:
    print("Please Enter The Serial Number of The Product You Want to Purchase")
    serial_number = input("Serial Number:")
    if serial_number.isdigit():
        serial_number = int(serial_number)
        print("-------------------------------------------------------------------------")
        print("")
        if 1 <= serial_number <= len(df):
            selected_product = df.loc[serial_number]
            print("Selected Product:\n",selected_product.to_string())
            print("-------------------------------------------------------------------------")
            print("")
            quantity = input("Enter Quantity Of Selected Product: ")
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0:
                    total_cost = selected_product['Price']*quantity
                    selected_products.append((selected_product, quantity, total_cost))
                    print("Total Cost For This Product: ₹", total_cost)
                else:
                    print("Invalid Quantity. Please Enter a Valid Quantity.")
            else:
                print("Invalid input for Quantity. Please enter a valid number.")
        else:
            print("Product Not Avaiable.Please Enter a valid Serial Number.")
    else:
        print("Invalid Input For Serial Number.Please Enter A Valid Number.")
    print("-------------------------------------------------------------------------")
    print("")
    print("Enter y To Add More Products")
    print("Enter n TO Start Billing")
    user_choice = input("Your Choice: ")
    if user_choice == 'y' or user_choice == 'Y':
        continue
    elif user_choice == 'n'or user_choice == 'N':
        print("Billing will Start From Here...")
        break
    else:
        print("Invaild Choice. EXITING The Program...")
        break
    print("-------------------------------------------------------------------------")
    print("")
if selected_products :
    print("-------------------------------------------------------------------------")
    print("📚📚📚📚📚📚📚📚📚📚📚📚📚📚📚📚 𝑺𝑺 𝑺𝑻𝑨𝑻𝑰𝑶𝑵𝑨𝑹𝒀 📚📚📚📚📚📚📚📚📚📚📚📚📚📚📚📚  ")
    print("\n                       𝟏/𝟔𝟎𝟓, 𝑺𝒆𝒄𝒕𝒐𝒓-𝑭 , 𝑱𝒂𝒏𝒌𝒊𝒑𝒖𝒓𝒂𝒎                     ")
    print("                          𝒏𝒆𝒂𝒓 𝑺𝒂𝒉𝒂𝒓𝒂 𝑺𝒕𝒂𝒕𝒆,𝑳𝒖𝒄𝒌𝒏𝒐𝒘                        ")
    print("                             𝑷𝑰𝑵 𝒄𝒐𝒅𝒆 - 𝟐𝟐𝟔𝟎𝟐𝟏                          ")
    print("                          𝙋𝙝𝙤𝙣𝙚 𝙉𝙪𝙢𝙗𝙚𝙧 - 𝟵𝟰𝟱𝟮𝟵𝟵𝟬𝟰𝟴𝟵                       ")
    total_bill = 0
    bill_data = []
    current_datetime = datetime.datetime.now()
    print("")
    print("𝒀𝒐𝒖𝒓 𝑹𝒆𝒔𝒑𝒆𝒄𝒕𝒆𝒅 𝑵𝒂𝒎𝒆             :",name)
    print("𝒀𝒐𝒖𝒓 𝑷𝒉𝒐𝒏𝒆 𝑵𝒖𝒎𝒃𝒆𝒓              :",phone_no)
    print("𝑫𝒂𝒕𝒆                         :",current_datetime.strftime("%Y-%m-%d"))
    print("𝑻𝒊𝒎𝒆                         :",current_datetime.strftime("%H:%M:%S"))
    print("")
    for product, quantity, cost in selected_products:
        total_bill += cost
        bill_data.append([product['Product'],quantity,f"₹{cost:.2f}"])
    headers=["Product","Quantity","Total Cost"]
    print(tabulate(bill_data,headers=headers,tablefmt="grid"))
    print("")
    print("Sub Total                   :₹",total_bill)
    print("GST                         :₹",total_bill*12/100)
    print("Payment you have to pay     :₹",total_bill+total_bill*12/100)
    print("")
    
    print("🙏🏻🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏 𝑻𝑯𝑨𝑵𝑲𝑺 𝑭𝑶𝑹 𝑽𝑰𝑺𝑰𝑻𝑰𝑵𝑮 🙏🏻🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏")
    print("----------------------------𝑯𝑨𝑽𝑬 𝑨 𝑮𝑶𝑶𝑫 𝑫𝑨𝒀-----------------------------")
else:
    print("𝑻𝑯𝑨𝑵𝑲 𝒀𝑶𝑼. 𝑬𝒙𝒊𝒕𝒊𝒏𝒈 𝒕𝒉𝒆 𝒑𝒓𝒐𝒈𝒓𝒂𝒎...")
    
    
        
