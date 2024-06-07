import customtkinter as ctk
import tkinter 
import os 
import pandas as pd
import csv
from dataclasses import dataclass


@dataclass
class ItemData:
    id:str
    product:str
    price:str
    stock:str

store_address=os.path.join(os.getcwd(),'app','data','stocks','items.csv')
p=pd.read_csv(store_address)
no_rows=p.shape[0]
no_columns=p.shape[1]

def listingItems(master, data:ItemData= ItemData(id=1, product="Kurkure", price="23", stock="10")):
    f_item = ctk.CTkFrame(master,width=500,height=50)

    l_id = ctk.CTkLabel(f_item, text=data.id,padx=2)
    l_product = ctk.CTkLabel(f_item, text=data.product, anchor="center")
    l_price = ctk.CTkLabel(f_item, text=data.price,padx=8)
    l_stock = ctk.CTkLabel(f_item, text=data.stock,padx=2)

    f_item.grid_columnconfigure(1, weight=1)
    f_item.grid_propagate(False)
    
    l_id.grid(row=0, column=0, sticky='w')
    l_product.grid(row=0, column=1, sticky='we')
    l_price.grid(row=0, column=2, sticky='w')
    l_stock.grid(row=0, column=3, sticky='w')

    return f_item

@dataclass
class OrderItems:
    id:str
    product:str
    qunt:str
    price:str

def listingOrder(master, order:OrderItems):
    f_order=ctk.CTkFrame(master,width=500,height=50)

    l_id = ctk.CTkLabel(f_order,padx=2, text=order.id)
    l_product = ctk.CTkLabel(f_order, anchor="center", text=order.product)
    l_price = ctk.CTkLabel(f_order, padx=8, text=order.price)
    l_qunt = ctk.CTkLabel(f_order,text=order.qunt,padx=2)

    f_order.grid_columnconfigure((0,1,2), weight=1)
    f_order.grid_propagate(False)
    
    l_id.grid(row=0, column=0, sticky='w')
    l_product.grid(row=0, column=1, sticky='we')
    l_qunt.grid(row=0, column=2, sticky='e')
    l_price.grid(row=0, column=3, sticky='w')

    return f_order


