from abc import ABC, abstractmethod


class Person(ABC):
	@abstractmethod
	def __init__(self, name, ID):
		self.name = name
		self.ID = ID

	@abstractmethod
	def get_info(self):
		return "name: {}".format(self.name)

# a = Person("Aaron", 20)
# print(a.get_info())

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



class Vehicle(ABC):

	@abstractmethod
	def __init__(self, make, model, year, ID, price):
		self.make = make
		self.model = model
		self.year = year
		self.ID = ID
		self.price = price

	@abstractmethod
	def get_info(self):
		return "make: {}, model: {}, year: {}, price: {}".format(self.make, self.model, self.year, self.price)

	@abstractmethod
	def run(self):
		pass


class Car(Vehicle):

	def __init__(self, make, model, year, ID, price, speed):
		super().__init__(make, model, year, ID, price)
		self.speed = speed

	def get_info(self):
		return "This is a car. {}. Speed: {}km/h".format(super().get_info(), self.speed)

	def run(self):
		print("This car drives at speed {} km/h".format(self.speed))


class Bicycle(Vehicle):

	def __init__(self, make, model, year, ID, price):
		super().__init__(make, model, year, ID, price)

	def get_info(self):
		return "This is a bicycle. {}.".format(super().get_info())

	def run(self):
		print("You can ride the bicycle at whatever speed you can")


bmw = Car("BMW", "328xi", 2011, 1, 500000, 200)
print(bmw.get_info())
bmw.run()

volkswagon = Car("Volkswagon", "tiguan", 2010, 2, 200000, 180)
print(volkswagon.get_info())
volkswagon.run()

bicycle = Bicycle("Giant", "TCR", 2015, 2, 3000)
print(bicycle.get_info())
bicycle.run()














