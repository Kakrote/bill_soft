import customtkinter as ctk
import tkinter 
import os 
import pandas as pd


store_address=os.path.join(os.getcwd(),'app','data','stocks','items.csv')
p=pd.read_csv(store_address)
no_rows=p.shape[0]
no_columns=p.shape[1]

def listingItems(master):
    return ctk.CTkFrame(master,width=200,height=50)
