#!python
from tkinter import *
import time
import datetime as dt

class App(Toplevel):
	def __init__(self, master, *args, **kwargs):
		Toplevel.__init__(self, master, *args, **kwargs)
		Frame.__init__(self, master, *args, **kwargs)
		self.master = master
		self.setup()
		
	def setup(self):
		self.label = Label(self.master, text="Hello, World")
		self.label.pack()
		self.timerVar = StringVar()
		self.timer = Label(self.master, textvariable=self.timerVar)
		self.timer.pack()
		self.closeButton = Button(self.master, text="Close", command=quit)
		self.closeButton.pack()
		self.closeButton.focus()
		self.lasttime = ''
		self.zero = dt.timedelta(seconds=1)
		self.tick()
		
	def tick(self):
		now = time.strftime("%H:%M:%S")
#		print(now, time)
		if not now == self.lasttime:
			self.lasttime = now
			self.timerVar.set(now)
#			self.label.configure(text=now)
		self.master.after(200, self.tick)

def main():
	root = Tk()
	app = App(master=root)
	app.mainloop()

if __name__ == '__main__':
	main()