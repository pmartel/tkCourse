#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
# from http://sebsauvage.net/python/gui/#our_project
# this was written for Python 2.7

import Tkinter

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        pass 

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
