import customtkinter as ctk
import tkinter

class AddItem(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=300,height=300,**kwargs)
        self.grid_propagate(False)
        # self.grid_rowconfigure((0,1),weight=1)
        self.grid_columnconfigure((0),weight=0)
        # self.grid_rowconfigure((0,1),weight=1)

        self.in_ids=ctk.CTkEntry(self,placeholder_text='id',width=100,height=20,font=('halvetica',12),text_color='#333')
        self.item_name=ctk.CTkEntry(self,font=('halvetica',12),text_color='#333',width=100,height=20)
        self.in_quntity=ctk.CTkEntry(self,font=('halvetica',12),text_color='#333',width=30,height=10)
        self.b_ok=ctk.CTkButton(self,text='ok',width=70,height=30)
        self.b_increment=ctk.CTkButton(self,text='+',width=20,height=20)
        self.b_decriment=ctk.CTkButton(self,text='-',width=20,height=20)
        self.b_add=ctk.CTkButton(self,text='ADD',width=90,height=30,text_color='#333')
        self.b_next=ctk.CTkButton(self,text='NEXT',width=90,height=30,text_color='#333')
    
    def show(self):

        self.in_ids.grid(row=0,column=0,sticky='nw',columnspan=2,padx=10,pady=10)
        self.item_name.grid(row=0,column=2,sticky='nw',padx=10,pady=10)
        self.b_ok.grid(row=1,column=0,sticky='nw',columnspan=2,padx=10,pady=10)
        self.b_decriment.grid(row=1,column=1,padx=1,pady=10)
        self.in_quntity.grid(row=1,column=2,padx=1,pady=10)
        self.b_increment.grid(row=1,column=3,padx=1,pady=10)

        self.b_add.grid(row=2,column=0,padx=10,pady=10)
        self.b_next.grid(row=2,column=1,padx=10,pady=10)


        self.grid(row=0,column=0,sticky='nsew',padx=20,pady=20)