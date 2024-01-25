"""
Program: salaryGUI.py
Chapter 8 practice project
1/25/2024

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

GUI-based version of the Salary Calculator app which calculates an employee's weekly earnings.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

# Class header (class name will change project to project)
class SalaryCalculator(EasyFrame):

	# Definition of our classes' constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = "Salary Calculator 2.0", background = "lightgreen")
		# variable to store a Font design for multiple labels
		labelFont = Font(family = "Georgia", size = 14)

		# Add the widgets to the window
		self.addLabel(text = "Salary Calculator", row = 0, column = 0, sticky = "NSEW", columnspan = 2, background = "lightgreen", font = Font(family = "Impact", size = 22) )
		self.addLabel(text = "Hourly Wage:", row = 1, column = 0, background = "lightgreen", foreground = "darkgreen", font = labelFont)
		self.wageField = self.addFloatField(value = 0.0, row = 1, column = 1)
		self.addLabel(text = "No. of Hours Worked:", row = 2, column = 0, background = "lightgreen", foreground = "darkgreen", font = labelFont)
		self.hoursField = self.addIntegerField(value = 0, row = 2, column = 1)
		# Bind the hoursField to the press of the enter key event
		self.hoursField.bind("<space>", lambda event: self.compute())

		self.button = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		self.button["background"] = "palegoldenrod"
		self.button["width"] = 15

		self.addLabel(text = "The employee's salary is: ", row = 4, column = 0, background = "lightgreen", font = labelFont)
		self.outputField = self.addFloatField(value = 0.0, row = 4, column = 1, precision = 2, state = "readonly")

	# Defintition of the compute() function which is the event handler
	def compute(self):
		wage = self.wageField.getNumber()
		hours = self.hoursField.getNumber()
		salary = wage * hours
		self.outputField.setNumber(salary)

# Global definition of the main() method
def main():
	# Instantiate an object from the class into mainloop()
	SalaryCalculator().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()