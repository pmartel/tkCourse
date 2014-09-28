#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
# from http://sebsauvage.net/python/gui/#our_project
# this was written for Python 2.7

import tkinter

class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid() 
        self.entry = tkinter.Entry(self)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)

        button = tkinter.Button(self,text=u"Click me !",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVar = tkinter.StringVar()
        label = tkinter.Label(self, textvariable = self.labelVar,
                              anchor="w",fg="white",bg="blue")
        #label will cover column 0 and 1
        label.grid(column=0,row=1,columnspan=2,sticky='EW') 
        self.grid_columnconfigure(0,weight=1) #resize column 0
        #only resize columns
        self.resizable(True,False)

    def OnButtonClick(self):
        self.labelVar.set( "You clicked the button!")
        
    def OnPressEnter(self,event):
        self.labelVar.set( "You pressed enter !" )
        
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
