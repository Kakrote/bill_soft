import customtkinter as ctk
import tkinter

class EntryLogin(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=400,height=400,border_width=2,**kwargs)
        self.grid_propagate(False)
        self.grid_rowconfigure((0),weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.l_logo=ctk.CTkLabel(self,text='LOGO',width=100,height=100,fg_color='white')
        self.l_userid=ctk.CTkLabel(self,text='USER-ID',font=('helvetica',28),text_color='#171F66')
        self.i_userid=ctk.CTkEntry(self,placeholder_text='Enter the id',font=('helvetica',12),text_color='#171f66',width=150,height=30)
        self.b_login=ctk.CTkButton(self,text='LOGIN',font=('helvetica',12),text_color='#9AD199',command=lambda:print("ckickd login"))

    def show(self):
        self.l_logo.grid(row=0,column=0,padx=10,pady=10,sticky='nsew')
        self.l_userid.grid(row=1,column=0,padx=10,pady=10)
        self.i_userid.grid(row=2,column=0,padx=10,pady=10)
        self.b_login.grid(row=3,column=0,padx=10,pady=10)

        self.grid(row=1,column=0,padx=100,pady=10)

class LogIn(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,border_width=2,**kwargs)
        # self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.l_title=ctk.CTkLabel(self,text='LOGIN',font=('Helvetica',31),text_color='#31D662',fg_color='white')

        self.entries=EntryLogin(self)

    def show(self):
        self.l_title.grid(row=0,column=0,columnspan=2,sticky='nsew',padx=20,pady=20)

        self.entries.show()

        self.grid(row=0,column=0,sticky='nsew',padx=20,pady=20)