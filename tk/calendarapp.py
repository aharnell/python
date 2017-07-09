#!python
from sys import version
import datetime
#from dateutil.relativedelta import relativedelta
import calendar
calendar.setfirstweekday(calendar.SUNDAY)




if version[0] =='3':
	from tkinter import *
elif version[0] == '2':
	from Tkinter import *
else:
	print('Python version incompatable with Tkinter')


class App(Frame):
	def __init__(self, master=None, *args, **kwargs):
		super().__init__(master, *args, **kwargs)
		self.labels = 'SMTWHFS'
		self.grid()
		self.date = datetime.datetime.today()
		self.month = self.date.month
		self.year = self.date.year
		self.bg = master.cget('bg')
		self.oneday = datetime.timedelta(1)
		self.build()
		self.fill(self.month, self.year)
		

	def build(self):
		self.monthback = Button(self, text="<", command=self.backclick)
		self.monthLabel = Button(self, relief=FLAT, command=self.monthclick)
		self.yearLabel = Button(self, relief=FLAT, command=self.yearclick)
		self.monthahead = Button(self, text=">", command=self.forwardclick)
		self.monthback.grid(row=0, column=0)
		self.monthLabel.grid(row=0, column=2, columnspan=2)
		self.yearLabel.grid(row=0, column=3, columnspan=2)
		self.monthahead.grid(row=0, column=6)
		self.weekdayLabels = []
		for day in range(len(self.labels)):
			self.weekdayLabels.append(Label(self, text=self.labels[day]))
			self.weekdayLabels[day].grid(row=1, column=day)
		self.calendar = []
		for date in range(42):
			self.calendar.append(Button(self, text="O", relief=FLAT, width=2, borderwidth=1))
			self.calendar[date].grid(row=int(date/7+2), column=date%7)

#		self.quit = Button(self, text="QUIT", fg="red", command=self.quit)
#		self.quit.focus()
#		self.quit.grid(column=1, columnspan=5)

	def fill(self, month, year):
		firstday, lastday = self.firstlast(datetime.date(year, month, 1))
		self.monthLabel.configure(text=datetime.date(self.year, self.month, 1).strftime("%b"))
		self.yearLabel.configure(text=datetime.date(self.year, self.month, 1).strftime("%y"))
		for day in range(len(self.calendar)):
			date = firstday+self.oneday*day
			self.calendar[day].configure(text=(date.day))
			if date == datetime.date.today():
				self.calendar[day].configure(bg='red')
			else:
				self.calendar[day].configure(bg=self.bg)
			if date.month != datetime.date(self.year, self.month, 1).month:
				self.calendar[day].configure(relief=SUNKEN)
			else:
				self.calendar[day].configure(relief=FLAT)

			
	def backclick(self):
		self.date = self.monthaug(self.date, -1)
		self.month = self.date.month
		self.year = self.date.year
		self.fill(self.month, self.year)
	
	def forwardclick(self):
		self.date = self.monthaug(self.date)
		self.month = self.date.month
		self.year = self.date.year
		self.fill(self.month, self.year)

	def monthclick(self):
		self.monthpick = Frame(self)
		
	def yearclick(self):
		pass

	def monthaug(self, date, magnitude=1):
		day = date.day
		newdate = date.replace(day=15)
		newdate += self.oneday*30*magnitude
		while date.month == newdate.month:
			if magnitude > 0:
				newdate+=self.oneday
			else:
				newdate-=self.oneday
		lastday = calendar.monthrange(newdate.year, newdate.month)[1]
		if day > lastday:
			day = lastday 
		newdate = newdate.replace(day=day)
		return newdate

	def firstlast(self, date):
		self.oneday = datetime.timedelta(1)
		firstday = date
		lastday = date
		while firstday.month==date.month or firstday.weekday() != 6:
			firstday-=self.oneday
		while lastday.month==date.month or lastday.weekday() != 5:
			lastday+=self.oneday
		return (firstday, lastday)
	
def main():
		root = Tk()
		app = App(master=root)
		app.mainloop()

if __name__ == '__main__':
	main()
