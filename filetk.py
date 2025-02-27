#farm chain logistic system 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql                       

win = tk.Tk()
win.geometry("1350x700+0+0")  
win.title("FarmChain  Smart Agricultural Logistics System")

def focus_next_widget(event):    #---  ,enter dabayo vani next line ma jancha @niraj
    if event.state & 0x0001: 
        event.widget.tk_focusPrev().focus() 
    else:
        event.widget.tk_focusNext().focus()  
    return "break"

# Title Label
title_label = tk.Label(
    win,
    text="Farmchain smart agriculture logistics",
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


############ variables###############
farmer_id = tk.StringVar()
farmer_name = tk.StringVar()         
crop_name = tk.StringVar()
stock = tk.StringVar()
price_per_kg = tk.StringVar()
district = tk.StringVar()
contact = tk.StringVar()
surplus_status = tk.StringVar()
search_by = tk.StringVar()



#entry  boxes

# Farmer ID
farmer_id_lbl = tk.Label(detail_frame, text="Farmer ID", font=('Arial', 15), bg="lightgrey")
farmer_id_lbl.grid(row=0, column=0, padx=2, pady=2)

farmer_id_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=farmer_id)
farmer_id_ent.grid(row=0, column=1, padx=2, pady=2)
farmer_id_ent.bind("<Return>", focus_next_widget)
farmer_id_ent.bind("<Shift-Return>", focus_next_widget)

# Farmer Name
farmer_name_lbl = tk.Label(detail_frame, text="Farmer Name", font=('Arial', 15), bg="lightgrey")
farmer_name_lbl.grid(row=1, column=0, padx=2, pady=2)

farmer_name_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=farmer_name) 
farmer_name_ent.grid(row=1, column=1, padx=2, pady=2)
farmer_name_ent.bind("<Return>", focus_next_widget)
farmer_name_ent.bind("<Shift-Return>", focus_next_widget)


# Crop Name
crop_name_lbl = tk.Label(detail_frame, text="Crop Name", font=('Arial', 15), bg="lightgrey")
crop_name_lbl.grid(row=2, column=0, padx=2, pady=2)

crop_name_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=crop_name)
crop_name_ent.grid(row=2, column=1, padx=2, pady=2)
crop_name_ent.bind("<Return>", focus_next_widget)
crop_name_ent.bind("<Shift-Return>", focus_next_widget)

# Stock Available (in kg)
stock_lbl = tk.Label(detail_frame, text="Stock Available (kg)", font=('Arial', 15), bg="lightgrey")
stock_lbl.grid(row=3, column=0, padx=2, pady=2)

stock_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=stock)
stock_ent.grid(row=3, column=1, padx=2, pady=2)
stock_ent.bind("<Return>", focus_next_widget)
stock_ent.bind("<Shift-Return>", focus_next_widget)

# Price per kg
price_lbl = tk.Label(detail_frame, text="Price per kg", font=('Arial', 15), bg="lightgrey")
price_lbl.grid(row=4, column=0, padx=2, pady=2)

price_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=price_per_kg) 
price_ent.grid(row=4, column=1, padx=2, pady=2)
price_ent.bind("<Return>", focus_next_widget)
price_ent.bind("<Shift-Return>", focus_next_widget)

# ------>District 
district_lbl = tk.Label(detail_frame, text="District", font=('Arial', 15), bg="lightgrey")
district_lbl.grid(row=5, column=0, padx=2, pady=2)

district_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=district) 
district_ent.grid(row=5, column=1, padx=2, pady=2)
district_ent.bind("<Return>", focus_next_widget)
district_ent.bind("<Shift-Return>", focus_next_widget)


# Contact
contact_lbl = tk.Label(detail_frame, text="Contact", font=('Arial', 15), bg="lightgrey")
contact_lbl.grid(row=6, column=0, padx=2, pady=2)

contact_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=contact) 
contact_ent.grid(row=6, column=1, padx=2, pady=2)
contact_ent.bind("<Return>", focus_next_widget)
contact_ent.bind("<Shift-Return>", focus_next_widget)

# Surplus Status
surplus_lbl = tk.Label(detail_frame, text="Surplus Status", font=('Arial', 15), bg="lightgrey")
surplus_lbl.grid(row=7, column=0, padx=2, pady=2)

surplus_ent = ttk.Combobox(detail_frame, font=("Arial", 15), state="readonly", textvariable=surplus_status)
surplus_ent['values'] = ("Surplus", "Shortage")
surplus_ent.grid(row=7, column=1, padx=2, pady=2)



##### functions ######
def fetch_data():
    conn=pymysql.connect(host="localhost",user="root",password="",database="ramesh")
    curr=conn.cursor()
    curr.execute("SELECT * FROM datatable")
    rows=curr.fetchall()
    if len(rows)!=0:
        farmer_table.delete(*farmer_table.get_children())
        for row in rows:
            farmer_table.insert('',tk.END,values=row)
        conn.commit()
    conn.close()

def add_func():
    if farmer_id.get() == "" or farmer_name.get() == "" or crop_name.get() == "":
        messagebox.showerror("Error!", "Please fill all the fields!")
    else:
        conn=pymysql.connect(host="localhost",user="root",password="",database="ramesh")
        curr=conn.cursor()
        curr.execute("INSERT INTO  datatable values (%s,%s,%s,%s,%s,%s,%s,%s)",(farmer_id.get(), farmer_name.get(), crop_name.get(), stock.get(), price_per_kg.get(), district.get(), contact.get(), surplus_status.get()))
        conn.commit()            
        conn.close()

        fetch_data() #------> this will fetch the data after clicking add button 

def get_cursor(event):#event pass na gare function lai thaha nai hudaina ki hami button dabayau 
    ''' this function will fetch selected data '''
    cursor_row = farmer_table.focus()
    content = farmer_table.item(cursor_row)
    row = content['values']
    farmer_id.set(row[0])
    farmer_name.set(row[1])
    crop_name.set(row[2])
    stock.set(row[3])
    price_per_kg.set(row[4])
    district.set(row[5])
    contact.set(row[6])
    surplus_status.set(row[7])

def clear():
    ''' this function will clear the entry boxes'''
    farmer_id.set("")
    farmer_name.set("")
    crop_name.set("")
    stock.set("")
    price_per_kg.set("")
    district.set("")
    contact.set("")
    surplus_status.set("")



def update_func():
    '''this function will update data as per user in the database'''
    conn = pymysql.connect(host="localhost", user="root", password="", database="ramesh")
    curr = conn.cursor()

    curr.execute("""UPDATE datatable SET farmer_name=%s, crop_name=%s, stock=%s, price_per_kg=%s, district=%s, contact=%s, surplus_status=%s WHERE farmer_id=%s""",
                 (farmer_name.get(), crop_name.get(), stock.get(), price_per_kg.get(), district.get(), contact.get(), surplus_status.get(), farmer_id.get()))
    conn.commit()
    fetch_data()
    conn.close()
    clear()

def delete_func():
    '''This function will delete the selected record from the database'''
    if farmer_id.get() == "":
        messagebox.showerror("Error!", "Please select a data to delete")
    else:
        conn = pymysql.connect(host="localhost", user="root", password="", database="ramesh")
        curr = conn.cursor()
        curr.execute("DELETE FROM datatable WHERE farmer_id=%s", farmer_id.get(),)
        conn.commit()
        fetch_data()
        conn.close()
        clear()

def search_func():
    search_category = search_by.get()  # -----> Combobox bata search value jancha 
    search_value = farmer_name_ent.get()  # ----> Get the value to search (you can change it based on user input)
    
    if search_value == "":
        messagebox.showerror("Error", "Please enter a value to search!")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="ramesh")
            curr = conn.cursor()

            query = f"SELECT * FROM datatable WHERE {search_category} LIKE %s"
            curr.execute(query, ('%' + search_value + '%',))

            rows = curr.fetchall()
            if len(rows) != 0:
                farmer_table.delete(*farmer_table.get_children())
                for row in rows:
                    farmer_table.insert('', tk.END, values=row)
                conn.commit()
            else:
                messagebox.showinfo("Info", "No matching records found!")

            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")

###########
#""""""""buttons"""""""""
btn_frame=tk.Frame(detail_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
btn_frame.place(x=18,y=390,width=340,height=120)

add_btn=tk.Button(btn_frame,bg="lightgrey",text="Add",bd=7,font=("Arial",13),width=15,command=add_func)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn=tk.Button(btn_frame,bg="lightgrey",text="update",bd=7,font=("Arial",13),width=15,command=update_func)
update_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn=tk.Button(btn_frame,bg="lightgrey",text="Delete",bd=7,font=("Arial",13),width=15,command=delete_func)
delete_btn.grid(row=1,column=0,padx=2,pady=2)

clear_btn=tk.Button(btn_frame,bg="lightgrey",text="clear",bd=7,font=("Arial",13),width=15,command=clear)
clear_btn.grid(row=1,column=1,padx=3,pady=2)




#""''' search """''''"

search_frame=tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_label=tk.Label(search_frame,text="search",bg="lightgrey",font=("Arial",14))
search_label.grid(row=0,column=0,padx=12,pady=2)

search_in=ttk.Combobox(search_frame,font=("Arial",14),state="readonly",textvariable=search_by)
search_in['values']=("farmer_name", "crop_name", "district", "contact", "surplus_status")
search_in.grid(row=0,column=1,padx=12,pady=2)

search_btn=tk.Button(search_frame,text='search',font=('arial',13),bd=9,width=14,bg="lightgrey",command=search_func)
search_btn.grid(row=0,column=2,padx=12,pady=2)

showall_btn=tk.Button(search_frame,text="show all",font=('arial',13),bd=9,width=14,bg="lightgrey",command=fetch_data)
showall_btn.grid(row=0,column=3,padx=12,pady=2)

##### database frame #######
main_frame=tk.Frame(data_frame,bg="lightgrey",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll=tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

''' farmer_id,farmer_name ,crop_name,stock,price_per_kg,district,contact,surplus_status'''

farmer_table = ttk.Treeview(main_frame, columns=("farmer_id", "farmer_name", "crop_name", "stock", "price_per_kg","district","contact","surplus_status"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=farmer_table.yview)
x_scroll.config(command=farmer_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

farmer_table.heading("farmer_id",text="farmer_id")
farmer_table.heading("farmer_name",text="farmer_name")
farmer_table.heading("crop_name",text="crop_name")
farmer_table.heading("stock",text="stock")
farmer_table.heading("price_per_kg",text="price_per_kg")
farmer_table.heading("district",text="district")
farmer_table.heading("contact",text="contact")
farmer_table.heading("surplus_status",text="surplus_status")

farmer_table['show']='headings'

farmer_table.column("farmer_id",width=100)
farmer_table.column("farmer_name",width=100)
farmer_table.column("crop_name",width=100)
farmer_table.column("stock",width=100)
farmer_table.column("price_per_kg",width=100)
farmer_table.column("district",width=100)
farmer_table.column("contact",width=100)
farmer_table.column("surplus_status",width=100)

farmer_table.pack(fill=tk.BOTH,expand=True)  


fetch_data()

farmer_table.bind("<ButtonRelease-1>",get_cursor)


win.mainloop()
