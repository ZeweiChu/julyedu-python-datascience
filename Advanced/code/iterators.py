x = iter([0, 1, 2, 3, 4, 5])
next(x)

class Yrange(object):
	def __init__(self, n):
		self.i = 0
		self.n = n

	def __iter__(self):
		return self

	def __next__(self):
		if self.i < self.n:
			i = self.i
			self.i += 1
			return i
		else:
			raise StopIteration

for i in Yrange(5):
	print(i)


def zrange(n):
	i = 0
	while i < n:
		yield(i)
		i += 1

for i in zrange(5):
	print(i)


from abc import ABC, abstractmethod
class Person(ABC):
	@abstractmethod
	def __init__(self, name, ID):
		self.name = name
		self.ID = ID
	
	@abstractmethod
	def get_info(self):
		return "name: {}".format(self.name)
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



class Company(object):

	def __init__(self, name, employees = []):
		self.name = name
		self.employees = employees
		self.index = -1

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

	def __iter__(self):
		return self

	def __next__(self):
		self.index += 1
		if self.index < len(self.employees):
			return self.employees[self.index]
		else:
			self.index = -1
			raise StopIteration
		



july = Employee("July", 1, "CEO", 99999999)
zewei = Employee("Zewei", 2, "Lecturer", 1, july)
han = Employee("Han", 3, "Lecturer", 100000, july)

c = Company("Julyedu")
c.hire(july)
c.hire(zewei)
c.hire(han)

for employee in c:
	print(employee.get_info())

for employee in c:
	print(employee.get_info())
