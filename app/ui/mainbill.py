import customtkinter as ctk
import tkinter
import pandas as pd
import os
# from ..src.itembyid import enterId
from ..globals import GLOBAL

class OrderList(ctk.CTkScrollableFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=340,height=300,**kwargs)


    def show(self):

        self.grid(row=3,column=0,sticky='nsew',padx=10,pady=10)


class AddItem(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=300,height=300,**kwargs)
        self.grid_propagate(False)
        # self.grid_rowconfigure((0,1),weight=1)
        self.grid_columnconfigure((0,1,2,3),weight=0)
        self.grid_rowconfigure((2,3),weight=1)

        self.in_ids=ctk.CTkEntry(self,placeholder_text='id',width=100,height=20,font=('halvetica',12),text_color='#333')

        # This is for entering the id:


        # self.in_ids.bind("<Enter>", lambda *args: print("ENTERED"))
        self.in_ids.bind("<Return>",self.onEnter)
        

            

        self.item_name=ctk.CTkEntry(self,font=('halvetica',12),text_color='#333',width=100,height=20,placeholder_text='item')
        self.in_quntity=ctk.CTkEntry(self,font=('halvetica',12),text_color='#333',width=30,height=10)
        self.b_ok=ctk.CTkButton(self,text='ok',width=70,height=30)
        self.b_increment=ctk.CTkButton(self,text='+',width=20,height=20)
        self.b_decriment=ctk.CTkButton(self,text='-',width=20,height=20)
        self.b_add=ctk.CTkButton(self,text='ADD',width=90,height=30,text_color='#333')
        self.b_next=ctk.CTkButton(self,text='NEXT',width=90,height=30,text_color='#333')

        self.orderlist=OrderList(self)
    
    def onEnter(self,*args):
        self.id=self.in_ids.get()
        itempath=os.path.join(os.getcwd(),'app','data','stocks','items.csv')
        data=pd.read_csv(itempath)
        self.item_name.delete(0,tkinter.END)
        for x in data.index:
            if data.loc[x,'id']==int(self.id):
                print(data.loc[x,'product'])
                self.item_name.insert(0,data.loc[x,'product'])
                break
        # print(data)


    



    def show(self):

        self.in_ids.grid(row=0,column=0,sticky='nw',columnspan=2,padx=10,pady=10)
        self.item_name.grid(row=0,column=2,sticky='nw',padx=10,pady=10)
        # self.b_ok.grid(row=1,column=0,sticky='nw',columnspan=2,padx=10,pady=10)
        self.b_decriment.grid(row=1,column=1,padx=1,pady=10)
        self.in_quntity.grid(row=1,column=2,padx=1,pady=10)
        self.b_increment.grid(row=1,column=3,padx=1,pady=10)

        self.b_add.grid(row=2,column=0,padx=10,pady=10)
        self.b_next.grid(row=4,column=0,padx=10,pady=10)

        self.orderlist.show()

        self.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)




class AddedItemsInList(ctk.CTkScrollableFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=300,height=500,**kwargs)


    def show(self):

        self.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)


class CheckOutList(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.grid_columnconfigure((0),weight=1)

        self.b_checkout=ctk.CTkButton(self,text='Check Out',width=120,height=30)
        self.b_reset=ctk.CTkButton(self,text='Reset',width=100,height=30)

        self.additeminlist=AddedItemsInList(self)
    
    def show(self):
        self.b_checkout.grid(row=1,column=0,sticky='sw',padx=10,pady=10)
        self.b_reset.grid(row=1,column=1,sticky='sw',padx=10,pady=10)

        self.additeminlist.show()
        self.grid(row=0,column=1,sticky='nsew',padx=10,pady=10)