import pandas as pd
import tkinter as tk
from datetime import datetime

class SportsShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("A.S SPORTS SHOP")

        self.df = pd.read_csv('C:\\Users\\user\\OneDrive\\Desktop\\Aditya\\Aditya_Arpit_Project.csv', index_col=0)
        self.net = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="A.S SPORTS SHOP", font=('bold', 16))
        self.label.pack()

        self.view_button = tk.Button(self.root, text="View Inventory", command=self.view_inventory)
        self.view_button.pack()

        self.purchase_button = tk.Button(self.root, text="Purchase Item", command=self.purchase_item)
        self.purchase_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack()

    def view_inventory(self):
        inventory_window = tk.Toplevel(self.root)
        inventory_window.title("Inventory")

        self.text = tk.Text(inventory_window)
        self.text.insert(tk.END, str(self.df))
        self.text.pack()

    def purchase_item(self):
        purchase_window = tk.Toplevel(self.root)
        purchase_window.title("Purchase Items")

        self.text = tk.Text(purchase_window)
        self.text.insert(tk.END, "Enter number of different items to purchase: ")
        self.text.pack()

        self.entry = tk.Entry(purchase_window)
        self.entry.pack()

        self.submit_button = tk.Button(purchase_window, text="Submit", command=self.show_bill)
        self.submit_button.pack()

    def show_bill(self):
        bill_window = tk.Toplevel(self.root)
        bill_window.title("Bill")

        prc = int(self.entry.get())
        itemls = []
        qtyls = []
        amtls = []

        for i in range(prc):
            item_id = input('Enter item ID: ')
            itemls.append(item_id)
            qty = int(input('Enter quantity: '))
            qtyls.append(qty)
            amt = self.df.loc[item_id]['Rate']
            amtls.append(amt)
            self.net += amt * qty

        bill_text = f"{'PRODUCT':<10}{'QUANTITY':<10}{'AMOUNT':<10}\n"
        for i in range(prc):
            bill_text += f"{itemls[i]:<10}{qtyls[i]:<10}{amtls[i]:<10}\n"

        bill_text += f"Total: {self.net}"

        self.text = tk.Text(bill_window)
        self.text.insert(tk.END, bill_text)
        self.text.pack()

root = tk.Tk()
app = SportsShopApp(root)
root.mainloop()

print('Thank You')
