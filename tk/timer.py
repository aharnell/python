#!python
import datetime as dt
import time
from sys import version

if version[0] == '3':
	from tkinter import *
elif version[0] == '2':
	from Tkinter import *
else:
	print('Python version incompatible with Tkinter')

class App(Frame):
	def __init__(self, master=None, *args, **kwargs):
		Frame.__init__(self, master, *args, **kwargs)
		self.master = master
		self.grid()

		self.done = self.stopgo = self.counter = self.roll = 0
		self.startvalue = 30

		self.texts = ("Start Timer", "Stop Timer")
		self.working = ("|", "\\", "-", "/")
		self.bgs=(self.cget('bg'), 'red')

		self.varButton  = StringVar()
		self.varWorking = StringVar()
		self.varUptime  = StringVar()
		self.varTimer   = IntVar()
		self.varTimer.set(self.startvalue)
		self.varButton.set(self.texts[self.stopgo])

		self.labelWLeft = Label(self, textvariable=self.varWorking)
		self.labelWLeft.grid(row=0, column=0)

		self.labelTitle = Label(self, text="Countdown Timer")
		self.labelTitle.grid(row=0, column=1, sticky=EW)

		self.labelWRight= Label(self, textvariable=self.varWorking)
		self.labelWRight.grid(row=0, column=2)

		self.buttonStart = Button(self, textvariable=self.varButton, command=self.timer)
		self.buttonStart.bind("<Return>", lambda e: self.timer(e))
		self.buttonStart.grid(row=1, column=1)
		self.buttonStart.focus()

		self.buttonMinus = Button(self, text="-5", command=lambda: self.updateVar(self.varTimer, self.varTimer.get()-5))
		self.buttonMinus.bind("<Return>", lambda e: self.updateVar(self.varTimer, self.varTimer.get()-5, e))
		self.buttonMinus.grid(row=2, column=0, sticky=W)

		self.scaleTimer = Scale(self, variable=self.varTimer, from_=0, to=self.startvalue*2, border=0, orient=HORIZONTAL)
		self.scaleTimer.configure(command=self.startvalue)
		self.scaleTimer.grid(row=2, column=1, sticky=EW)

		self.buttonPlus = Button(self, text="+5", command=lambda: self.updateVar(self.varTimer, self.varTimer.get()+5))
		self.buttonPlus.bind("<Return>", lambda e: self.updateVar(self.varTimer, self.varTimer.get()+5, e))
		self.buttonPlus.grid(row=2, column=2, sticky=E)

		self.buttonClose = Button(self, text="Close", command=quit)
		self.buttonClose.bind("<Return>", quit)
		self.buttonClose.grid(row=3, column=1)

		self.labelUptime= Label(self, textvariable=self.varUptime)
		self.labelUptime.grid(row=4, column=1)
		self.labelUptime.grid_remove()
		self.labelUptime.grid()

	def setupTimer(self):
		self.counter = 0
		t = time.localtime()
		self.zero = dt.timedelta(hours=t[0], minutes=t[1], seconds=t[2])
		self.lasttime = dt.datetime(1,1,1).replace(microsecond=0)
		
	def tick(self):
		uptime = dt.datetime(1,1,1).now() - self.zero
		uptime = uptime.replace(microsecond=0)
		if uptime > self.lasttime:
			self.lasttime = uptime
			if self.done:
				self.updateVar(self.varUptime, uptime.strftime('%H:%M:%S'))
			else:
				if self.varTimer.get() == 0:
					self.done = 1
					self.setupTimer()
					self.labelUptime.grid()
					self.buttonClose.focus()
				else:
					if self.counter < 59:
						self.counter += 1
					else:
						self.counter = 0
						self.updateVar(self.varTimer, self.varTimer.get()-1)
		if self.stopgo:
			self.roll = (self.roll + 1)%len(self.working)
			self.updateVar(self.varWorking, self.working[self.roll])
			if self.done: self.changebg(self, self.bgs[self.roll%2])
		self.after(150, self.tick)

	def timer(self, e=None):
		self.updateVar(self.varWorking, '')
		self.stopgo = (self.stopgo + 1)%2
		self.updateVar(self.varButton, self.texts[self.stopgo])
		if self.done:
			self.done = 0
			self.changebg(self, self.bgs[0])
			self.labelUptime.grid_remove()
			self.updateVar(self.varTimer, self.varTimer.get()+self.startvalue)
		elif self.stopgo:
			self.startvalue = self.varTimer.get()
			self.setupTimer()
		self.tick()

	def setStartValue(self, val):
		self.startvalue = val

	def updateVar(self, var, val, e=None):
		var.set(val)

	def changebg(self, element, color):
		element.configure(bg=color)
		for child in element.winfo_children():
			self.changebg(child, color)

def main():
	root = Tk()
	sw = root.winfo_screenwidth()
	sh = root.winfo_screenheight()
	w = 180
	h = 120
	x = sw / 2
	y = 0
	root.wm_title("Timer")
	root.geometry('+%d+%d' % (x, y))
	root.minsize(width=w, height=h)
	app = App(root)
	app.mainloop()

if __name__ == '__main__':
	main()