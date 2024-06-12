import customtkinter as ctk
import tkinter
from .ui.login import LogIn
from .ui.bill import Bill
from .ui.updatelist import UpdateList
# from .globals import GLOBAL

ctk.set_appearance_mode('light')

class MainFrame(ctk.CTkFrame):
    activepanel=None
    def setActiveFrame(self,frame):
        self.activeframe.destroy()
        self.activeframe=frame
        self.activeframe.show()
        
    def __init__(self,master,**kwargs):
        super().__init__(master,border_width=2,**kwargs)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.login=LogIn(self)
        self.bill=Bill(self)
        self.updatelist=UpdateList(self)


        # GLOBAL['mainframe']=self

        # self.activeframe=self.login
        self.activeframe=self.updatelist
        # self.activeframe=self.bill
    def show(self):
        self.activeframe.show()
        self.pack(fill=tkinter.BOTH,expand=True,padx=10,pady=10)

class App(ctk.CTk):
    width,height=800,800
    def __init__(self,**kwargs):
        super().__init__(*kwargs)
        self.geometry(f'{self.width}x{self.height}')
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.mainframe=MainFrame(self)
        self.after(10,lambda:self.state('zoomed'))


    def show(self):
        self.mainframe.show()
        self.mainloop()

app=None
def main():
    app=App()
    app.show()
