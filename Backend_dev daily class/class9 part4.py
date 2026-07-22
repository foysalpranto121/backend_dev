import tkinter as tk
root = tk.Tk()
root.title("Product Management System")
root.geometry("700x500")

tk.Label(root,text="Product Name:").grid(row=0,column=0)
tk.Label(root,text="Product Price:").grid(row=1,column=0)
tk.Label(root,text="Product Quantity:").grid(row=2,column=0)

root.mainloop()