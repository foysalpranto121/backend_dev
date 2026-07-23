import tkinter as tk
from tkinter import ttk, messagebox
root = tk.Tk()
root.title("Product Entry")
root.geometry("700x450")


def add_product():
    messagebox.showinfo("Success", "Product added successfully")

tk.Label(root, text="Product Name").grid(row=0, column=0)

entry_name = tk.Entry(root).grid(row=0,column=1)

tk.Label(root, text="Price").grid(row=1, column=0)

entry_price = tk.Entry(root)

entry_price.grid(row=1, column=1)

tk.Label(root, text="Quantity").grid(row=2, column=0)

entry_quantity = tk.Entry(root)

entry_quantity.grid(row=2, column=1)

tk.Label(root, text="Category").grid(row=3, column=0)

entry_category = tk.Entry(root)

entry_category.grid(row=3, column=1)

tk.Button(root, text="Add Product",command=add_product).grid(row=4, column=0)

tk.Button(root, text="Export").grid(row=4, column=1)

columns = ("Name", "Price", "Quantity", "Category")

tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.grid(row=5, column=0, columnspan=4, pady=20)
root.configure(bg="lightblue")

root.mainloop()


