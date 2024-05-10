import customtkinter as ctk
import tkinter
from app.ui.mainbill import AddItem,CheckOutList
import os
from ..src.listing import listingItems, ItemData
import pandas as pd

store_list=list()


class ItemListFrame(ctk.CTkScrollableFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=278,height=600,**kwargs)
        self.grid_columnconfigure((0,1),weight=1)
        
        self.store_list=store_list

        itemspath=os.path.join(os.getcwd(),'app','data','stocks','items.csv')
        df = pd.read_csv(itemspath)
        for i in range(df.shape[0]):
            item = dict(df.iloc[i])
            self.store_list.append(listingItems(self, ItemData(id=item['id'], product=item['product'], price=item['price'], stock=item['stock'])))
        # self.store_list.append(listingItems(self))
        # self.store_list.append(listingItems(self))
        # self.store_list.append(listingItems(self))
        # self.store_list.append(listingItems(self))
    def show(self):

        for i,item in enumerate(self.store_list):
            item.grid(row=i,column=0,pady=2)

        self.grid(row=1,column=0,columnspan=2,sticky='nsew',padx=5,pady=5)



class LeftSide(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=300,height=600,**kwargs)
        # self.grid_propagate(False)
        self.grid_columnconfigure((0,1),weight=1)

        self.searchbar=ctk.CTkEntry(self,placeholder_text='Search item',font=('halvetica',13),width=200,height=20)
        self.b_search=ctk.CTkButton(self,text='Search',font=('halvetica',13),width=50,height=20,text_color='#171F66',command=lambda: print("searching"))


        self.itemslist=ItemListFrame(self)
    

    def show(self):
        self.searchbar.grid(row=0,column=0,padx=5,sticky='n')
        self.b_search.grid(row=0,column=1,padx=5,sticky='n')


        self.itemslist.show()


        self.grid(row=1,column=0,sticky='nw',padx=(5,10),pady=(10,0))



class RightSideFrame(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=1100,height=600,**kwargs)
        self.grid_propagate(False)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure((0,1),weight=1)

        self.l_title=ctk.CTkLabel(self,text='Billing section',font=('halvetica',20),text_color='#171F66',fg_color='white')
        self.additem=AddItem(self)
        self.checkout=CheckOutList(self)

    def show(self):

        # self.l_title.grid(row=0,column=0,sticky='nsew',padx=0,pady=0)

        self.additem.show()
        self.checkout.show()

        self.grid(row=1,column=1,sticky='nsew',padx=(0,10),pady=(10,5))


class Bill(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.grid_columnconfigure((0,1),weight=1)
        self.grid_rowconfigure(1,weight=1)

        self.l_title=ctk.CTkLabel(self,text='BILL NOW',font=('halvetica',20),text_color='#171F66',fg_color='white')

        self.leftside=LeftSide(self)
        self.rightside=RightSideFrame(self)


    def show(self):
        self.l_title.grid(row=0,column=0,columnspan=2,sticky='nsew',padx=0,pady=0)
        self.leftside.show()
        self.rightside.show()


        self.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)