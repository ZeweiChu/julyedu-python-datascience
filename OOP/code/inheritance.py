from abc import ABC, abstractmethod

class Person(object):
	#@abstractmethod
	def __init__(self, name, ID):
		self.name = name
		self.ID = ID

	#@abstractmethod
	def get_info(self):
		return "name: {}".format(self.name)

a = Person("Aaron", 20)
print(a.get_info())

'''
Student class

'''
class Student(Person):

	# method
	def __init__(self, name, ID, level=0):
		# field
		# self refers to the object that is being created
		super().__init__(name, ID)
		self.level = level

	def get_info(self):
		return "{} ,level: {}".format(super().get_info(), self.level)

	def take_exam(self, grade):
		if grade.upper() in ["A", "B", "C"]:
			self.level += 1
		return self.level

	def graduate(self):
		self.print_info()
		if self.level >= 12:
			print("Congratulations, you've graduated from Julyedu")
			return True
		else:
			print("Sorry, you need to pass {} extra exams".format(12-self.level))
			return False


class Employee(Person):

	def __init__(self, name, ID, title, salary, manager=None):
		super().__init__(name, ID)
		self.title = title
		self.salary = salary
		self.manager = manager

	def get_info(self):
		return "({}, title: {}, salary: {}, manager: {})".format(super().get_info(), self.title, self.salary, self.manager.get_info() if self.manager is not None else "No manager")



july = Employee("July", 1, "CEO", 99999999)
print(july.get_info())
zewei = Employee("Zewei", 2, "Lecturer", 1, july)
print(zewei.get_info())


class Company(object):

	def __init__(self, name, employees = []):
		self.name = name
		self.employees = employees

	def hire(self, employee):
		if not employee in self.employees:
			self.employees.append(employee)

	def fire(self, employee):
		if employee in self.employees:
			self.employees.remove(employee)

	def get_info(self):
		res = "Company: {}, employees: ".format(self.name)
		for employee in self.employees:
			res += ", {}".format(employee.get_info())
		return res

c = Company("Julyedu")
c.hire(july)
c.hire(zewei)

han = Employee("Han", 3, "Lecturer", 100000, july)

c.hire(han)

print(c.get_info())

print("Firing zewei!")
c.fire(zewei)
print(c.get_info())

print("Firing zewei!")
c.fire(zewei)
print(c.get_info())






