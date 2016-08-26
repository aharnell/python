#!python
'''Timer

Usage:
	timer [-h | --help] [-v STARTVALUE] [-s | --start] 

Options:
	-h --help		Show this screen.
	-s --start		Starts the timer immediately.
	-v STARTVALUE		Start time [default: 30].

'''

import datetime as dt
import time
from sys import version
from docopt import docopt

if version[0] == '3':
	from tkinter import *
elif version[0] == '2':
	from Tkinter import *
else:
	print('Python version incompatible with Tkinter')

class App(Frame):
#	self.stopgo = args[--start]
	def __init__(self, master=None, args={}):#, **kwargs):
		print(args)
		Frame.__init__(self, master)#, *args, **kwargs)
		self.master = master
		self.grid()
		self.args = args

		self.done = self.counter = self.roll = 0

		self.texts = ("Start Timer", "Stop Timer")
		self.working = ("|", "\\", "-", "/")
		self.bgs=(self.cget('bg'), 'red')

		self.varButton  = StringVar()
		self.varWorking = StringVar()
		self.varUptime  = StringVar()
		self.varTimer   = IntVar()

		if self.args['STARTVALUE']:
			self.startvalue = int(self.args['STARTVALUE'])
		else:
			self.startvalue = 30

		if self.args['--start']:
			self.stopgo = 1
		else:
			self.stopgo = 0

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

		if self.stopgo:
			self.setupTimer()
			self.tick()

#		self.labelUptime= Label(self, textvariable=self.varUptime, font='32')
#		self.labelUptime.grid(row=4, column=1)
#		self.labelUptime.grid_remove()
#		self.labelUptime.grid()

	def setupTimer(self):
		self.counter = 0
		t = time.localtime()
		self.zero = dt.timedelta(hours=t[3], minutes=t[4], seconds=t[5])
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
					self.labelUptime= Label(self, textvariable=self.varUptime, font='32')
					self.labelUptime.grid(row=4, column=1)
#					self.labelUptime.grid()
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
			self.labelUptime.destroy()
#			self.labelUptime.grid_remove()
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

def main(args):
	root = Tk()
	sw = root.winfo_screenwidth()
	sh = root.winfo_screenheight()
	w = 180
	h = 120
	x = (sw - w)/ 2
	y = 0
	root.wm_title("Timer")
	root.geometry('+%d+%d' % (x, y))
#	root.minsize(width=w, height=h)
	app = App(root, args)
	app.mainloop()

if __name__ == '__main__':
	args = docopt(__doc__)
	main(args)