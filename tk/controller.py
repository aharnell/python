#!python

from tkinter import *

class Application(Frame):
	def say_hi(self):
		print("hi there, everyone!")

	def createWidgets(self):
		self.Forward = Button(self, text="/\\", command=lambda: self.control("F"), font=(20))
		self.Reverse = Button(self, text="V", command=lambda: self.control("R"), font=(20))
		self.Left = Button(self, text="<", command=lambda: self.control("L"), font=(20))
		self.Right = Button(self, text=">", command=lambda: self.control("R"), font=(20))
		self.QUIT = Button(self, text="QUIT", fg="red", command=self.quit)
		self.QUIT.focus()
		

		self.Forward.grid(column=1, row=0)
		self.Left.grid(column=0, row=1)
		self.QUIT.grid(column=1, row=1)
		self.Right.grid(column=2, row=1)
		self.Reverse.grid(column=1, row=2)

#		self.hi_there = Button(self)
#		self.hi_there["text"] = "Hello",
#		self.hi_there["command"] = self.say_hi

#		self.hi_there.pack({"side": "left"})

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def control(self, command):
		print(command)

def main():
	root = Tk()
	app = Application(master=root)
	app.mainloop()
	root.destroy()

if __name__ == "__main__":
	main()