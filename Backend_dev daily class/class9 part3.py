import tkinter as tk
from tkinter import ttk
#------- tkinter gui/window  -------

window = tk.Tk()

window.title("Product Management System")

window.geometry("700x500")

#-------Labels -------

tk.Label(window,text="Product Name:").grid(row=0,column=0)
tk.Label(window,text="Product Price:").grid(row=1,column=0)
tk.Label(window,text="Product Quantity:").grid(row=2,column=0)

#-------Entry Fields -------       

product_name = tk.Entry(window)
product_name.grid(row=0,column=1)

product_price = tk.Entry(window)
product_price.grid(row=1,column=1)

product_quantity = tk.Entry(window)
product_quantity.grid(row=2,column=1)

#-------Functions -------

def add_product():
    name = product_name.get()
    price = product_price.get()
    quantity = product_quantity.get()

    if name and price and quantity:
        table.insert("", "end", values=(name, price, quantity))
        product_name.delete(0, tk.END)
        product_price.delete(0, tk.END)
        product_quantity.delete(0, tk.END)

def update_product():
    selected = table.selection()
    if selected:
        item = selected[0]
        name = product_name.get()
        price = product_price.get()
        quantity = product_quantity.get()

        if name and price and quantity:
            table.item(item, values=(name, price, quantity))
            product_name.delete(0, tk.END)
            product_price.delete(0, tk.END)
            product_quantity.delete(0, tk.END)

def delete_product():
    selected = table.selection()
    if selected:
        item = selected[0]
        table.delete(item)

def on_table_select(event):
    selected = table.selection()
    if selected:
        item = selected[0]
        values = table.item(item)["values"]
        product_name.delete(0, tk.END)
        product_price.delete(0, tk.END)
        product_quantity.delete(0, tk.END)
        product_name.insert(0, values[0])
        product_price.insert(0, values[1])
        product_quantity.insert(0, values[2])

#-------Buttons -------

add_button = tk.Button(window,text="Add Product",command=add_product)
add_button.grid(row=3,column=0)

update_button = tk.Button(window,text="Update Product",command=update_product)
update_button.grid(row=3,column=1)

delete_button = tk.Button(window,text="Delete Product",command=delete_product)
delete_button.grid(row=3,column=2)

#-------Table -------

table = ttk.Treeview(window, columns=("Name", "Price", "Quantity"), height=15)
table.column("#0", width=0, stretch=tk.NO)
table.column("Name", anchor=tk.W, width=200)
table.column("Price", anchor=tk.CENTER, width=150)
table.column("Quantity", anchor=tk.CENTER, width=150)

table.heading("#0", text="", anchor=tk.W)
table.heading("Name", text="Product Name", anchor=tk.W)
table.heading("Price", text="Price", anchor=tk.CENTER)
table.heading("Quantity", text="Quantity", anchor=tk.CENTER)

table.grid(row=4,column=0,columnspan=3)
table.bind("<<TreeviewSelect>>", on_table_select)

#-------Main Loop -------

window.mainloop()

