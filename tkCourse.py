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
        pass 

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
