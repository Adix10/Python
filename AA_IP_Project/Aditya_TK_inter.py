import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

def validate_name(name):
    return name.isalpha()

def validate_phone_number(phone_number):
    return phone_number.isnumeric() and len(phone_number) == 10

def show_products():
    products_text.config(state=tk.NORMAL)
    products_text.delete("1.0", tk.END)
    products_text.insert(tk.END, str(df))
    products_text.config(state=tk.DISABLED)

def purchase_items():
    purchase_window = tk.Toplevel(root)
    purchase_window.title("Purchase Items")
    purchase_frame = tk.Frame(purchase_window)
    purchase_frame.pack()

    itemls = []
    qtyls = []
    amtls = []
    net = 0

    prc = simpledialog.askinteger("Purchase Items", "Enter number of different items to purchase:")
    
    if prc is not None:
        if prc > 6:
            messagebox.showinfo("Purchase Items", "There Are Only 6 Products In Our Inventory.")
        else:
            for i in range(prc):
                eid = simpledialog.askstring("Purchase Items", "Enter item ID:").upper()
                qty = simpledialog.askinteger("Purchase Items", "Enter quantity:")
                amt = df.loc[eid]['Rate']
                itemls.append(eid)
                qtyls.append(qty)
                amtls.append(amt)
                net += amt * qty
            
            bill = messagebox.askyesno("Purchase Items", "Do you want the bill to be displayed?")
            if bill:
                show_bill(itemls, qtyls, amtls, net)

def show_bill(itemls, qtyls, amtls, net):
    bill_window = tk.Toplevel(root)
    bill_window.title("Bill")
    bill_frame = tk.Frame(bill_window)
    bill_frame.pack()

    bill_text = tk.Text(bill_frame)
    bill_text.insert(tk.END, "A.S SPORTS SHOP\n")
    bill_text.insert(tk.END, "------------------------------------\n")
    bill_text.insert(tk.END, "Product   Quantity   Amount\n")
    bill_text.insert(tk.END, "------------------------------------\n")
    for i in range(len(itemls)):
        bill_text.insert(tk.END, f"{itemls[i]}   {qtyls[i]}   {amtls[i]}\n")
    bill_text.insert(tk.END, "------------------------------------\n")
    bill_text.insert(tk.END, f"Total: {net}\n")
    bill_text.config(state=tk.DISABLED)
    bill_text.pack()

def submit_rating():
    rating = rating_var.get()
    if rating >= 1 and rating <= 5:
        if rating >= 4:
            messagebox.showinfo("Thank You", "Thank you for your rating! Visit Us Again.")
        else:
            feedback = simpledialog.askstring("Feedback", "We're sorry for any inconvenience you faced. Please tell us the reason:")
            messagebox.showinfo("Thank You", "Thank you for your feedback. We'll work to improve.")
    else:
        messagebox.showerror("Invalid Rating", "Please enter a rating between 1 and 5.")

def exit_application():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

df = pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\Aditya\\Aditya_Arpit_Project.csv", index_col=0)

root = tk.Tk()
root.title("A.S Sports Shop")
root.attributes('-fullscreen', True)  # Open in full screen mode

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

name = ""
phone_number = ""
rating_var = tk.IntVar()

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

notebook.add(tab1, text="View Products")
notebook.add(tab2, text="Purchase Items")
notebook.add(tab3, text="Submit Rating")

name_valid = False
phone_number_valid = False

while not name_valid:
    name = simpledialog.askstring("Enter Your Name", "Please enter your name:")
    if validate_name(name):
        name_valid = True
    else:
        messagebox.showerror("Invalid Name", "Invalid name! Please enter alphabetic characters only.")

while not phone_number_valid:
    phone_number = simpledialog.askstring("Enter Your Phone Number", "Please enter your phone number:")
    if validate_phone_number(phone_number):
        phone_number_valid = True
        phone_number = int(phone_number)
    else:
        messagebox.showerror("Invalid Phone Number", "Invalid phone number! Please enter numeric characters and use 10 digits.")

title_label = tk.Label(tab1, text="A.S Sports Shop", font=("Helvetica", 18, "bold"))
title_label.pack(pady=20)

view_products_button = tk.Button(tab1, text="View Products", command=show_products)
view_products_button.pack(pady=10)

purchase_items_button = tk.Button(tab2, text="Purchase Items", command=purchase_items)
purchase_items_button.pack(pady=10)

exit_button1 = tk.Button(tab1, text="Exit", command=exit_application)
exit_button1.pack(pady=10)

exit_button2 = tk.Button(tab2, text="Exit", command=exit_application)
exit_button2.pack(pady=10)

rating_label = tk.Label(tab3, text="Please rate us out of 5:", font=("Helvetica", 14))
rating_label.pack(pady=20)

rating_entry = tk.Entry(tab3, textvariable=rating_var)
rating_entry.pack(pady=10)

submit_rating_button = tk.Button(tab3, text="Submit Rating", command=submit_rating)
submit_rating_button.pack(pady=10)

exit_button3 = tk.Button(tab3, text="Exit", command=exit_application)
exit_button3.pack(pady=10)

products_text = tk.Text(tab1, wrap="none")
products_text.pack()
products_text.config(state=tk.DISABLED)

root.mainloop()
