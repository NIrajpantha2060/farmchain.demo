import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("1350x700+0+0")  
win.title("FarmChain Smart Agricultural Logistics System")

# Title Label
title_label = tk.Label(
    win,
    text="Farmchain Smart Agriculture Logistics",
    font=('Arial', 20,"bold"),  
    border=12,               
    relief=tk.GROOVE,
    bg="lightgrey"
)
title_label.pack(side=tk.TOP, fill=tk.X)  

# Detail Frame
detail_frame = tk.LabelFrame(
    win,
    text='Enter Details',
    font=('Arial', 20),
    bd=12,
    relief=tk.GROOVE,
    bg='lightgrey'
)
detail_frame.place(x=20, y=90, width=420, height=575)

# Data Frame
data_frame = tk.Frame(
    win,
    bd=12,
    bg='lightgrey',
    relief=tk.GROOVE
)
data_frame.place(x=450, y=90, width=810, height=575) 

# Entry Boxes and Labels for Farmer Details
farmer_id_lbl = tk.Label(detail_frame, text="Farmer ID", font=('Arial', 15), bg="lightgrey")
farmer_id_lbl.grid(row=0, column=0, padx=2, pady=2)

farmer_id_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
farmer_id_ent.grid(row=0, column=1, padx=2, pady=2)

farmer_name_lbl = tk.Label(detail_frame, text="Farmer Name", font=('Arial', 15), bg="lightgrey")
farmer_name_lbl.grid(row=1, column=0, padx=2, pady=2)

farmer_name_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
farmer_name_ent.grid(row=1, column=1, padx=2, pady=2)

crop_name_lbl = tk.Label(detail_frame, text="Crop Name", font=('Arial', 15), bg="lightgrey")
crop_name_lbl.grid(row=2, column=0, padx=2, pady=2)

crop_name_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
crop_name_ent.grid(row=2, column=1, padx=2, pady=2)

stock_lbl = tk.Label(detail_frame, text="Stock Available (kg)", font=('Arial', 15), bg="lightgrey")
stock_lbl.grid(row=3, column=0, padx=2, pady=2)

stock_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
stock_ent.grid(row=3, column=1, padx=2, pady=2)

price_lbl = tk.Label(detail_frame, text="Price per kg", font=('Arial', 15), bg="lightgrey")
price_lbl.grid(row=4, column=0, padx=2, pady=2)

price_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
price_ent.grid(row=4, column=1, padx=2, pady=2)

district_lbl = tk.Label(detail_frame, text="District", font=('Arial', 15), bg="lightgrey")
district_lbl.grid(row=5, column=0, padx=2, pady=2)

district_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
district_ent.grid(row=5, column=1, padx=2, pady=2)

contact_lbl = tk.Label(detail_frame, text="Contact", font=('Arial', 15), bg="lightgrey")
contact_lbl.grid(row=6, column=0, padx=2, pady=2)

contact_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
contact_ent.grid(row=6, column=1, padx=2, pady=2)

surplus_lbl = tk.Label(detail_frame, text="Surplus Status", font=('Arial', 15), bg="lightgrey")
surplus_lbl.grid(row=7, column=0, padx=2, pady=2)

surplus_ent = ttk.Combobox(detail_frame, font=("Arial", 15), state="readonly")
surplus_ent['values'] = ("Surplus", "Shortage")
surplus_ent.grid(row=7, column=1, padx=2, pady=2)

# Button Frame
btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=18, y=390, width=340, height=120)

add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("Arial", 13), width=15)
add_btn.grid(row=0, column=0, padx=2, pady=2)

update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("Arial", 13), width=15)
update_btn.grid(row=0, column=1, padx=3, pady=2)

delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("Arial", 13), width=15)
delete_btn.grid(row=1, column=0, padx=2, pady=2)

clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear", bd=7, font=("Arial", 13), width=15)
clear_btn.grid(row=1, column=1, padx=3, pady=2)

# Search Frame
search_frame = tk.Frame(data_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_label = tk.Label(search_frame, text="Search", bg="lightgrey", font=("Arial", 14))
search_label.grid(row=0, column=0, padx=12, pady=2)

search_in = ttk.Combobox(search_frame, font=("Arial", 14), state="readonly")
search_in['values'] = ("farmer_name", "crop_name", "district", "contact", "surplus_status")
search_in.grid(row=0, column=1, padx=12, pady=2)

search_btn = tk.Button(search_frame, text='Search', font=('Arial', 13), bd=9, width=14, bg="lightgrey")
search_btn.grid(row=0, column=2, padx=12, pady=2)

showall_btn = tk.Button(search_frame, text="Show All", font=('Arial', 13), bd=9, width=14, bg="lightgrey")
showall_btn.grid(row=0, column=3, padx=12, pady=2)

# Farmer Data Table (Treeview)
main_frame = tk.Frame(data_frame, bg="lightgrey", bd=11, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

farmer_table = ttk.Treeview(main_frame, columns=("farmer_id", "farmer_name", "crop_name", "stock", "price_per_kg", "district", "contact", "surplus_status"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=farmer_table.yview)
x_scroll.config(command=farmer_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

farmer_table.heading("farmer_id", text="farmer_id")
farmer_table.heading("farmer_name", text="farmer_name")
farmer_table.heading("crop_name", text="crop_name")
farmer_table.heading("stock", text="stock")
farmer_table.heading("price_per_kg", text="price_per_kg")
farmer_table.heading("district", text="district")
farmer_table.heading("contact", text="contact")
farmer_table.heading("surplus_status", text="surplus_status")

farmer_table['show'] = 'headings'

farmer_table.column("farmer_id", width=100)
farmer_table.column("farmer_name", width=100)
farmer_table.column("crop_name", width=100)
farmer_table.column("stock", width=100)
farmer_table.column("price_per_kg", width=100)
farmer_table.column("district", width=100)
farmer_table.column("contact", width=100)
farmer_table.column("surplus_status", width=100)

farmer_table.pack(fill=tk.BOTH, expand=True)

win.mainloop()
