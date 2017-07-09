from tkinter import *
import time
import logging
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('logging', default='CRITICAL' )
level = parser.parse_args().logging.upper()
logging.basicConfig(filename=sys.argv[0]+'.log',level=level, format='%(asctime)s -- %(levelname)s: %(message)s', datefmt='%d %H:%M:%S Z%z %b %Y')
ld = logging.debug
li = logging.info

class StopWatch(Frame):  
	""" Implements a stop watch frame widget. """																
	def __init__(self, parent=None, **kw):		
		Frame.__init__(self, parent, kw)
		self._start = 0.0
		self.ssbuttons = {True:'Stop',	False:'Start'}
		self.buttons = {0: ('Split', 'p', self.Split), 
						1: ('Reset', 'r', self.Reset),
						2: ('Clear', 'c', self.Clear),
						3: ('Quit', 'q', self.Quit)}
		self._elapsedtime = 0.0
		self._running = False
		self.timestr = StringVar()
		self.sstext = StringVar()
		self.sstext.set(self.ssbuttons[self._running])
		self.makeButtons()
		self.makeWidgets()
		self.splitsCounter = 0

	def makeButtons(self):
		""" Make the buttons. """
		self.StartButton = Button(self, textvariable=self.sstext, command=self.StartStop, underline=0)
		self.StartButton.bind('s', self.StartStop)
		self.StartButton.pack(side=LEFT)
		self.StartButton.focus()
		for button, info in sorted(self.buttons.items()):
			text = info[0]
			command = info[2]
			underline = int(not button)
			key = info[1]
			self.buttons[button] = Button(self, text=text, command=command, underline=underline)
			self.buttons[button].bind(key, command)
			self.buttons[button].pack(side=LEFT)

	def makeWidgets(self):						 
		""" Make the time label. """
		self.Timer = Label(self, textvariable=self.timestr)
		self._setTime(self._elapsedtime)
		self.Timer.pack(fill=X, expand=NO, pady=2, padx=2)					  
		self.Splits = Frame()
		self.Splits.pack(side=BOTTOM)
	
	def _update(self): 
		""" Update the label with elapsed time. """
		self._elapsedtime = time.time() - self._start
		self._setTime(self._elapsedtime)
		self._timer = self.after(10, self._update)
	
	def _setTime(self, elap):
		""" Set the time string to Minutes:Seconds:Hundreths """
		minutes = int(elap/60)
		seconds = int(elap - minutes*60.0)
		hseconds = int((elap - minutes*60.0 - seconds)*100)				
		self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

	def StartStop(self, event=None):
		""" Start/Stop the stopwatch. """
		if not self._running:
			li("Stop watch started")
			self._start = time.time() - self._elapsedtime
			self._update()
			self.StartButton.focus()
		if self._running:
			li("Stop watch stopped")
			self.after_cancel(self._timer)			
			self._elapsedtime = time.time() - self._start	
			self._setTime(self._elapsedtime)
		self._running = (self._running + 1)%2
		self.sstext.set(self.ssbuttons[self._running])
	
	def Reset(self, event=None):								  
		""" Reset the stopwatch. """
		if self._running:
			self.splitsCounter = 0
			self.Splits.destroy()
			self.Splits = Frame()
			self.Splits.pack(side=BOTTOM)
		self._start = time.time()		 
		self._elapsedtime = 0.0	
		self._setTime(self._elapsedtime)
		li('Stop watch reset')

	def Split(self, event=None):
		""" Displays the time when split button pressed."""
		if self._running:
			self.splitsCounter += 1
			splitText = "({}) {}".format(self.splitsCounter, self.timestr.get())
			li('Split recorded {}'.format(splitText))
			Label(self.Splits, text=splitText).pack(side=TOP)

	def Clear(self, event=None):
		""" Clears the displayed split times."""
		if not self._running:
			self.splitsCounter = 0
			self.Splits.destroy()
			self.Splits = Frame()
			self.Splits.pack(side=BOTTOM)
	
	def Quit(self, event=None):
		li('{} exited'.format(sys.argv[0]))
		quit()

def main():
	root = Tk()
	sw = StopWatch(root)
	sw.pack(side=TOP)
	root.mainloop()

if __name__ == '__main__':
	li('{} initiated'.format(sys.argv[0]))
	main()
