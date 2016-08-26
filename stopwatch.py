from tkinter import *
import time


class StopWatch(Frame):  
	""" Implements a stop watch frame widget. """																
	def __init__(self, parent=None, **kw):		
		Frame.__init__(self, parent, kw)
		self._start = 0.0		
		self._elapsedtime = 0.0
		self._running = False
		self.timestr = StringVar()
		self.makeButtons()
		self.makeWidgets()	  

	def makeButtons(self):
		self.Start = Button(self, text='Start', command=self.Start)
		self.Start.pack(side=LEFT)
		self.Start.focus()
		self.Stop = Button(self, text='Stop', command=self.Stop)
		self.Stop.pack(side=LEFT)
		self.Reset = Button(self, text='Reset', command=self.Reset)
		self.Reset.pack(side=LEFT)
		self.Quit = Button(self, text='Quit', command=quit)
		self.Quit.pack(side=LEFT)

	def makeWidgets(self):						 
		""" Make the time label. """
		self.Timer = Label(self, textvariable=self.timestr)
		self._setTime(self._elapsedtime)
		self.Timer.pack(fill=X, expand=NO, pady=2, padx=2)					  
	
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

	def Start(self):													 
		""" Start the stopwatch, ignore if running. """
		if not self._running:			
			self._start = time.time() - self._elapsedtime
			self._update()
			self.Stop.focus()
			self._running = True		
	
	def Stop(self):									
		""" Stop the stopwatch, ignore if stopped. """
		if self._running:
			self.after_cancel(self._timer)			
			self._elapsedtime = time.time() - self._start	
			self._setTime(self._elapsedtime)
			self._running = 0
	
	def Reset(self):								  
		""" Reset the stopwatch. """
		self._start = time.time()		 
		self._elapsedtime = 0.0	
		self._setTime(self._elapsedtime)
		
		
def main():
	root = Tk()
	sw = StopWatch(root)
	sw.pack(side=TOP)
	
	
	root.mainloop()

if __name__ == '__main__':
	main()
