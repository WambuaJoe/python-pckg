class Employees:

	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = "{}.{}@email.com".format(first, last)

		Employees.num_of_emps += 1

	def fullname(self):
		return "{} {}".format(self.first.title(), self.last.title())
	
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount
	
	@classmethod
	def parse_str(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

# usr_input = input("Enter first & last names, and pay (separated by a space):\n")
# usr_input = usr_input.split(' ')
# if len(usr_input) != 3:
	# print("Make sure to enter 3 values separated by a space")
# else:
	# fName = usr_input[0]
	# lName = usr_input[1]
	# salary = int(usr_input[2])
# 
# emp1 = Employees(fName, lName, salary)
# print("Full name: {}\nEmail: {}\nSalary: {}".format(
			# emp1.fullname(), emp1.email, emp1.pay
# ))
# 
emp_str1 = 'joe-wambua-45000'

new_emp1 = Employees.parse_str(emp_str1)
print(new_emp1.fullname())