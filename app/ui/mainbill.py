import customtkinter as ctk
import tkinter
import pandas as pd
import os
# import csv
from ..src.listing import listingOrder,OrderItems
# from ..src.itembyid import enterId
from ..globals import GLOBAL

iteem=list()

itempath=os.path.join(os.getcwd(),'app','data','stocks','items.csv')
data=pd.read_csv(itempath)

class AddItem(ctk.CTkFrame):
    me=None
    orderlist = None
    def __init__(self,master,**kwargs):
        GLOBAL['AddItem']=self
        super().__init__(master,width=300,height=300,**kwargs)
        AddItem.me=self
        self.grid_propagate(False)
        # self.grid_rowconfigure((0,1),weight=1)
        self.grid_columnconfigure((0,1,2,3),weight=0)
        self.grid_rowconfigure((2,3),weight=1)

        self.in_ids=ctk.CTkEntry(self,placeholder_text='id',width=100,height=20,font=('halvetica',12),text_color='#333')

        # This is for entering the id:


        # self.in_ids.bind("<Enter>", lambda *args: print("ENTERED"))
        # funlist=[self.onEnter,self.on_ClickAdd]
        self.in_ids.bind("<Return>",self.onEnter)
        # self.in_ids.bind("<Return>",self.on_ClickAdd)
        self.item_name=ctk.CTkEntry(self,font=('halvetica',12),text_color='#333',width=100,height=20,placeholder_text='item')
        self.in_quntity=ctk.CTkEntry(self,placeholder_text='Q',font=('halvetica',12),text_color='#333',width=30,height=10)


        self.in_quntity.bind("<Return>",self.onQunt)

        self.b_ok=ctk.CTkButton(self,text='ok',width=70,height=30)
        self.b_increment=ctk.CTkButton(self,text='+',width=20,height=20)
        self.b_decriment=ctk.CTkButton(self,text='-',width=20,height=20)
        self.l_name=ctk.CTkLabel(self,text='name of customer',font=('halvetica',20),text_color='#333')
        self.e_name=ctk.CTkEntry(self,placeholder_text='name',width=200,height=30,text_color='#333',font=('halvetica',12))

        self.b_next=ctk.CTkButton(self,text='NEXT',width=90,height=30,text_color='#333',command=self.orderBill)

        self.orderlist=OrderList(self)
        self.checkoutlist=AddedItemsInList(self, fg_color="red")
    
    
    def onEnter(self,*args):
        self.id=self.in_ids.get()
        # self.qunt=self.in_quntity.get() or 1
        # self.qunt= 1
        self.item_name.delete(0,tkinter.END)
        # self.in_quntity.delete(0,tkinter.END)
        for x in data.index:
            if data.loc[x,'id']==int(self.id):
                # print(data.loc[x,'product'])
                self.item_name.insert(0,data.loc[x,'product'])
                break
        # print(data)
        # if not hasattr(self,'itemlist'):
        #  self.itemlist=[]
        # self.id1=self.in_ids.get()
    

    def onQunt(self,*args):
        self.price=None
        self.qunt=self.in_quntity.get()
        self.in_ids.delete(0,tkinter.END)
        self.in_quntity.delete(0,tkinter.END)
        for x in data.index:
            if data.loc[x,'id']==int(self.id):
                self.price=data.loc[x,'price']
                break
        self.item_name1=self.item_name.get()
        self.item_name.delete(0,tkinter.END)    
        dict={'id':self.id, 'name':self.item_name1,'qunt':self.qunt,'price':(int(self.qunt)*(self.price))}

        self.addOrder(dict)
        # self.itemlist.append(dict)
        # iteem=self.itemlist.copy()
        # for i in iteem:
        #     print(i)


    def addOrder(self, order):
        _id = order['id']
        _name = order['name']
        _qunt=order['qunt']
        _price=order['price']
        # price=None
        iteem.append(order)

        orderUI = listingOrder(self.orderlist, order=OrderItems(id=_id, product=_name,qunt=_qunt, price=_price))
        # self.orderlist
        self.orderlist.orders.append(orderUI)
        orderUI.grid(row=len(self.orderlist.orders)-1,column=0,pady=2)
        # print(iteem)
    

    def orderBill(self):
        self.bill_list=list()
        for i in iteem:
            data={
                'id':i['id'],
                'iteam':i['name'],
                'qunt':i['qunt'],
                'price':i['price']
            }
            self.bill_list.append(data)
        print(self.bill_list)
        # for j in self.bill_list:
        #     print(j['id']+","+j['iteam'])
        iteem.clear()
        self.name=self.e_name.get()
        path=os.path.join(os.getcwd(),'app','bills',)
        # fillname=path+name+'.csv'
        filename= os.path.join(path, self.name+".csv")
        # fillename=filename
        with open(filename,'w',newline='') as csvfile:
            csvfile.write('id'+','+'iteam'+','+'quntity'+','+'price'+'\n')
            for j in self.bill_list:
                csvfile.write(j['id']+','+j['iteam']+','+j['qunt']+','+str(j['price'])+'\n')

        # print(iteem)
        df=pd.read_csv(filename)
        # print(df.head())
        # _qunt = 0
        for i in range(df.shape[0]):
            item=dict(df.iloc[i])
            AddedItemsInList.me.checklist.append(
                listingOrder(
                    # self.checkoutlist,
                    AddedItemsInList.me,
                    order=OrderItems(
                        id=item['id'],
                        product=item['iteam'],
                        qunt=item['quntity'],
                        price=item['price']
                    )
                )
            )

        AddedItemsInList.me.checklist.append(
            listingOrder(
                AddedItemsInList.me,
                order=OrderItems(
                    id="Total", 
                    product="Iteam",
                    qunt=df['quntity'].sum(),
                    price=df['price'].sum()
                )
            )
        )
        AddedItemsInList.me.show()
        self.e_name.delete(0,tkinter.END)
    
    def deleteFile(self):
        path_=os.path.join(os.getcwd(),'app','bills')
        filepath=os.path.join(path_,self.name+'.csv')
        self.e_name.delete(0,tkinter.END)
        os.remove(filepath)



        
        

        

    def show(self):

        self.in_ids.grid(row=0,column=0,sticky='nw',columnspan=2,padx=10,pady=10)
        self.item_name.grid(row=0,column=1,sticky='nw',columnspan=2,padx=10,pady=10)
        # self.b_ok.grid(row=1,column=0,sticky='nw',columnspan=2,padx=10,pady=10)
        # self.b_decriment.grid(row=1,column=1,padx=1,pady=10)
        self.in_quntity.grid(row=1,column=1,padx=1,pady=10)
        # self.b_increment.grid(row=1,column=3,padx=1,pady=10)

        self.l_name.grid(row=2,column=0,padx=10,pady=10)
        self.e_name.grid(row=2,column=1,padx=10,pady=10)
        self.b_next.grid(row=4,column=0,padx=10,pady=10)

        self.orderlist.show()

        self.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)

# this is the order list
orders=list()

class OrderList(ctk.CTkScrollableFrame): 
    def __init__(self,master,**kwargs):
        super().__init__(master,width=340,height=300,**kwargs)
        self.grid_columnconfigure((0,1), weight=1)
        # self.additemcls=GLOBAL['AddItem']
        self.orders=orders
        # self.orders.append(listingOrder(self))
        # self.orders.append(listingOrder(self))
        # self.orders.append(listingOrder(self))
        # self.orders.append(listingOrder(self))


    def show(self):
        for i,item in enumerate(self.orders):
            item.grid(row=i,column=0,pady=2)

        self.grid(row=3,column=0,sticky='nsew',padx=10,pady=10)
    
    def clearlists(self):
        for i,item in enumerate(self.orders):
            item.grid_forget()


checklist=list()

class AddedItemsInList(ctk.CTkScrollableFrame):
    me=None
    def __init__(self,master,**kwargs):
        super().__init__(master,width=300,height=500,**kwargs)
        self.grid_columnconfigure((0,1),weight=1)
        self.checklist=checklist
        AddedItemsInList.me = self


    def show(self):

        for i,item in enumerate(self.checklist):
            item.grid(row=i,column=0,pady=2)

        self.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)

    def clearlists(self):
        for i,item in enumerate(self.checklist):
            item.grid_forget()
        self.checklist.clear()

class CheckOutList(ctk.CTkFrame):
    me = None
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        CheckOutList.me = self
        self.grid_columnconfigure((0),weight=1)

        self.additeminlist=AddedItemsInList(self)
        self.orderlist=OrderList(self)
        # self.additem=AddItem(self)

        self.b_checkout=ctk.CTkButton(self,text='Check Out',width=120,height=30,command=self.reSet)
        self.b_reset=ctk.CTkButton(self,text='Reset',width=100,height=30,command=self.clearAll)

    def clearAll(self):
        self.orderlist.clearlists()
        self.additeminlist.clearlists()
        AddItem.me.deleteFile()

    def reSet(self):
        self.orderlist.clearlists()
        self.additeminlist.clearlists()
        # AddItem.me.deleteFile()


        

    
    def show(self):
        self.b_checkout.grid(row=1,column=0,sticky='sw',padx=10,pady=10)
        self.b_reset.grid(row=1,column=1,sticky='sw',padx=10,pady=10)

        self.additeminlist.show()
        self.grid(row=0,column=1,sticky='nsew',padx=10,pady=10)