import tkinter as tk
from tkinter import ttk
from customtkinter import CTkLabel, CTkEntry, CTkComboBox, CTkButton
from tkinter import messagebox
import sqlite3

# SQLite Database Initialization
conn = sqlite3.connect('hardware_data.db')
cursor = conn.cursor()

# Create the 'entries' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        contact TEXT,
        product_name TEXT,
        category TEXT,
        price REAL,
        quantity INTEGER,
        date TEXT,
        payment_method TEXT
    )
''')
conn.commit()

def enter_data():
    # Customer info
    customer_name = customer_name_entry.get()
    contact = contact_entry.get()

    # Product info
    product_name = product_name_entry.get()
    category = category_combobox.get()
    price = price_entry.get()
    quantity = Quantity_entry.get()

    # Sales info
    date = date_entry.get()
    payment_method = payment_method_combobox.get()

    if product_name and category and price and quantity and customer_name and contact and date and payment_method:
        # Insert data into SQLite database
        cursor.execute('''
            INSERT INTO entries (customer_name, contact, product_name, category, price, quantity, date, payment_method)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (customer_name, contact, product_name, category, price, quantity, date, payment_method))
        conn.commit()

        print("Data inserted into SQLite database.")
        clear_entry_fields()
    else:
        messagebox.showwarning(title="Error", message="All fields are required.")

def clear_entry_fields():
    # Clear all entry fields after successful data entry
    customer_name_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    product_name_entry.delete(0, tk.END)
    category_combobox.set('')
    price_entry.delete(0, tk.END)
    Quantity_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    payment_method_combobox.set('')

window = tk.Tk()
window.title("Data Entry Form")

label = CTkLabel(window, text="US.Hardware")
label.pack(pady=20)

frame = tk.Frame(master=window)
frame.pack()

# Customer Info
customer_info_frame = tk.LabelFrame(frame, text="Customer Information")
customer_info_frame.grid(row=0, column=0, padx=20, pady=10)

customer_name_label = CTkLabel(customer_info_frame, text="Customer Name")
customer_name_label.grid(row=0, column=0)
customer_name_entry = CTkEntry(customer_info_frame)
customer_name_entry.grid(row=1, column=0)

contact_label = CTkLabel(customer_info_frame, text="Contact")
contact_entry = CTkEntry(customer_info_frame)
contact_label.grid(row=0, column=1)
contact_entry.grid(row=1, column=1)

for widget in customer_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Product Info
product_info_frame = tk.LabelFrame(frame, text="Product Information")
product_info_frame.grid(row=1, column=0, padx=20, pady=10)

product_name_label = CTkLabel(product_info_frame, text="Product Name")
product_name_label.grid(row=0, column=0)
product_name_entry = CTkEntry(product_info_frame)
product_name_entry.grid(row=1, column=0)

category_label = CTkLabel(product_info_frame, text="Category")
category_combobox = CTkComboBox(product_info_frame, values=["Tools", "Hardware", "Electronics", "Paint", "Plumbing"])
category_label.grid(row=0, column=1)
category_combobox.grid(row=1, column=1)

price_label = CTkLabel(product_info_frame, text="Price")
price_entry = CTkEntry(product_info_frame)
price_label.grid(row=2, column=0)
price_entry.grid(row=3, column=0)

quantity_label = CTkLabel(product_info_frame, text="Quantity")
quantity_label.grid(row=2, column=1)
Quantity_entry = CTkEntry(product_info_frame)
Quantity_entry.grid(row=3, column=1)

for widget in product_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Sales Info
sales_info_frame = tk.LabelFrame(frame, text="Sales Information")
sales_info_frame.grid(row=2, column=0, padx=20, pady=10)

date_label = CTkLabel(sales_info_frame, text="Date")
date_entry = CTkEntry(sales_info_frame)
date_label.grid(row=0, column=0)
date_entry.grid(row=1, column=0)

payment_method_label = CTkLabel(sales_info_frame, text="Payment Method")
payment_method_combobox = CTkComboBox(sales_info_frame, values=["Cheque", "Cash"])
payment_method_label.grid(row=0, column=1)
payment_method_combobox.grid(row=1, column=1)

for widget in sales_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Button
button = CTkButton(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()

# Close the SQLite connection when the Tkinter window is closed
conn.close()
