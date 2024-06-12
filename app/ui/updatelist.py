import customtkinter as ctk
from .bill import ItemListFrame

class UpdateIteams(ctk.CTkScrollableFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=400,height=800,**kwargs)
    

    def show(self):
        self.grid(row=1,column=0,padx=3,pady=2,sticky='nw',columnspan=4)





class EntryUpdate(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=400,height=800,fg_color='white',**kwargs)
        self.grid_propagate(False)
        self.grid_columnconfigure((0,1,2,3),weight=1)
        self.grid_rowconfigure((1),weight=1)

        self.e_iteam=ctk.CTkEntry(self,placeholder_text='enter iteam',font=('halvetica',13),width=180,height=30,text_color='#333')
        self.e_stock=ctk.CTkEntry(self,placeholder_text='Q',font=('halvetica',13),width=40,height=30,text_color='#333')
        self.e_price=ctk.CTkEntry(self,placeholder_text='$',font=('halvetica',13),width=35,height=30,text_color='#333')
        self.b_add=ctk.CTkButton(self,text='ADD',font=('halvatica',20),hover=True,hover_color='green')
        self.b_done=ctk.CTkButton(self,text='DONE',font=('halvatica',20))

        self.list=UpdateIteams(self)

    def show(self):

        self.e_iteam.grid(row=0,column=0,sticky='n',padx=5,pady=5)
        self.e_stock.grid(row=0,column=1,padx=5,pady=5,sticky='n')
        self.e_price.grid(row=0,column=2,padx=5,pady=5,sticky='n')
        self.b_add.grid(row=0,column=3,sticky='n',padx=2,pady=10)
        self.b_done.grid(row=2,column=0,padx=5,pady=5,sticky='n')

        self.list.show()

        self.grid(row=1,column=0,sticky='nw',padx=(5,0),pady=(5,0))

class FinalUpdatedList(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=1000,fg_color='white',**kwargs)

        self.list=ItemListFrame(self)
        self.list.configure(width=1000)


    def show(self):

        self.list.grid(row=0,column=0,padx=(2,0),pady=5,sticky='nw')


        self.grid(row=1,column=1,sticky='nsew',padx=(0,5),pady=5)

        

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

