#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import tkinter,threading,time

class MyProcess(threading.Thread):
 def __init__(self,startValue):
     threading.Thread.__init__(self)
     self._stop = False
     self._value = startValue
     
 def run(self):
     while self._value>0 and not self._stop:
         self._value = self._value - 1
         print( u"Thread: I'm working... (value=%d)" % self._value)
         time.sleep(1)
     print( u"Thread: I have finished.")
         
 def stop(self):
     self._stop = True

 def result(self):
     return self._value

class MyGUI(tkinter.Tk):
 def __init__(self,parent):
     tkinter.Tk.__init__(self,parent)
     self.parent = parent
     self.initialize()
     self.worker = MyProcess(15)
     self.worker.start()  # Start the worker thread

 def initialize(self):
     ''' Create the GUI. '''
     self.grid()
     button = tkinter.Button(self,text=u"Click me to stop",command=self.OnButtonClick)
     button.grid(column=1,row=0)
     self.labelVariable = tkinter.StringVar()
     label = tkinter.Label(self,textvariable=self.labelVariable)
     label.grid(column=0,row=0)
     self.labelVariable.set(u"Hello !")

 def OnButtonClick(self):
     '''' Called when button is clicked. '''
     self.labelVariable.set( u"Button clicked" )
     self.worker.stop()  # We ask the worker to stop (it may not stop immediately)
     while self.worker.isAlive(): # We wait for the worker to stop.
         time.sleep(0.2)
     # We display the result:
     self.labelVariable.set( u"Result: %d" % self.worker.result() )

if __name__ == "__main__":
 app = MyGUI(None)
 app.title('my application')
 app.mainloop()
