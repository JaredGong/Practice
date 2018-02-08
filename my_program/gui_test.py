# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.messagebox import showinfo

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
#        self.hellolabel=Label(self,text='hello world')
#        self.hellolabel.pack()
        self.nameinput=Entry(self)
        self.nameinput.pack()
        self.alterbutton=Button(self,text='hello',command=self.hello)
        self.alterbutton.pack()

    def hello(self):
        name=self.nameinput.get() or 'world'
        showinfo('message','hello, %s'% name)

app=Application()
app.master.title('hello world')
app.mainloop()