import customtkinter as ctk
import tkinter
from ..src.listing import listingOrder,OrderItems
from .bill import ItemListFrame
import os
from ..src.listing import listingItems, ItemData
import pandas as pd






iteem=list()
class EntryUpdate(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=400,height=800,fg_color='white',**kwargs)
        self.grid_propagate(False)
        self.grid_columnconfigure((0,1,2,3),weight=1)
        self.grid_rowconfigure((1),weight=1)

        self.finallist=FinalUpdatedList(self)

        self.e_iteam=ctk.CTkEntry(self,placeholder_text='enter iteam',font=('halvetica',13),width=180,height=30,text_color='#333')
        self.e_price=ctk.CTkEntry(self,placeholder_text='$',font=('halvetica',13),width=35,height=30,text_color='#333')
        self.e_stock=ctk.CTkEntry(self,placeholder_text='Q',font=('halvetica',13),width=40,height=30,text_color='#333')
        self.b_add=ctk.CTkButton(self,text='ADD',font=('halvatica',20),hover=True,hover_color='green',command=self.onAdd)
        self.b_done=ctk.CTkButton(self,text='DONE',font=('halvatica',20),command=self.finallist.updateList)

        self.list1=UpdateIteams(self)
        

    def show(self):

        self.e_iteam.grid(row=0,column=0,sticky='n',padx=5,pady=5)
        self.e_price.grid(row=0,column=1,padx=5,pady=5,sticky='n')
        self.e_stock.grid(row=0,column=2,padx=5,pady=5,sticky='n')
        self.b_add.grid(row=0,column=3,sticky='n',padx=2,pady=10)
        self.b_done.grid(row=2,column=0,padx=5,pady=5,sticky='n')

        self.list1.show()

        self.grid(row=1,column=0,sticky='nw',padx=(5,0),pady=(5,0))

    def onAdd(self):
        self.iteam=self.e_iteam.get()
        self.price=self.e_price.get()
        self.stock=self.e_stock.get()

        dict={'iteam':self.iteam,'price':self.price,'stock':self.stock}
        self.addIteam(dict)
        # iteem.append(dict)
        print(iteem)

        self.e_iteam.delete(0,tkinter.END)
        self.e_price.delete(0,tkinter.END)
        self.e_stock.delete(0,tkinter.END)


    def addIteam(self,product):
        _iteam=product['iteam']
        _price=product['price']
        _stock=product['stock']
        iteem.append(_iteam)
        iteem.append(_price)
        iteem.append(_stock)

        productUI= listingOrder(self.list1, order=OrderItems(id='1', product=_iteam,qunt=_stock, price=_price))

        self.list1.newIteam.append(productUI)
        productUI.grid(row=len(self.list1.newIteam)-1,column=0,padx=2)



newIteam=list()
class UpdateIteams(ctk.CTkScrollableFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=400,height=800,**kwargs)
        self.grid_columnconfigure((0,1),weight=1)

        self.newIteam=newIteam.copy()
        newIteam.clear()
    

    def show(self):
        self.grid(row=1,column=0,padx=3,pady=2,sticky='nw',columnspan=4)





class FinalUpdatedList(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=1000,fg_color='white',**kwargs)

        self.list=ItemListFrame(self)
        self.list.configure(width=1000)


    def show(self):

        # for i,iteam in enumerate(self.list.store_list):
        #     iteam.grid(row=i,column=0,pady=2)

        self.list.grid(row=0,column=0,padx=(2,0),pady=5,sticky='nw')


        self.grid(row=1,column=1,sticky='nsew',padx=(0,5),pady=5)

    def updateList(self):

        self.store_address=os.path.join(os.getcwd(),'app','data','stocks','items.csv')
        df=pd.read_csv(self.store_address)
        _lastid=df['id'].iloc[-1]
        # lastindex=len(df.index)
        # newiteam=pd.Series({'id':_lastid+1,'product':iteem[0],'price':iteem[1],'stock':iteem[2]},index=df.columns)
        # df.loc[lastindex]=newiteam
        path=os.path.join(os.getcwd(),'app','data','stocks','temp.csv')
        with open(self.store_address,'r') as source:
            with open(path,'w') as destination:
                for lines in source:
                    destination.write(lines)
                destination.write('\n'+str(_lastid+1)+','+iteem[0]+','+iteem[1]+','+iteem[2])

        self.path1=os.path.join(os.getcwd(),'app','data','stocks')
        self.realpath1=os.path.join(self.path1,'items'+'.csv')
        os.remove(self.store_address)
        os.rename(path,self.realpath1)







        # print(df.tail())
        
        for i,iteam in enumerate(self.list.store_list):
            iteam.grid(row=i,column=0,pady=2)
        # self.list.store_list.clear()
        # for i in range(df.shape[0]):
        #     item = dict(df.iloc[i])
        #     self.list.store_list.append(listingItems(self, ItemData(id=item['id'], product=item['product'], price=item['price'], stock=item['stock'])))
        # # self.list.configure(width=1000)
        # for i,iteam in enumerate(self.list.store_list):
        #     iteam.grid(row=i,column=0,pady=2)

        pass

        

class UpdateList(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)  # Use double underscores
        # self.grid_propagate(False)
        self.grid_columnconfigure((0,1),weight=1)
        self.grid_rowconfigure((1),weight=1)

        self.l_title = ctk.CTkLabel(self, text='Update', font=('Times New Roman', 20),fg_color='white')

        self.entryiteam=EntryUpdate(self)
        self.finallistupdated=FinalUpdatedList(self)

    def show(self):
        self.l_title.grid(row=0, column=0, padx=5, pady=5, sticky='nsew',columnspan=2)

        self.entryiteam.show()
        self.finallistupdated.show()


        self.grid(row=0,column=0,padx=5,pady=5,sticky='nsew')

# Create the main application window

