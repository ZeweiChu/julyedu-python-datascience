
'''
Student class

'''
class Student(object):

	# method
	def __init__(self, name, level=0):
		# field
		# self refers to the object that is being created
		self.name = name
		self.level = level

	def print_info(self):
		print("Name: {}, level: {}".format(self.name, self.level))

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



# instantiate an object
# july = Student("July", 15)
# july.take_exam("A")
# july.take_exam("B")
# july.take_exam("C")
# july.take_exam("D")
# july.take_exam("F")
# july.print_info() # 18

# zewei = Student("Zewei")
# zewei.print_info()
# zewei.take_exam("A")
# zewei.take_exam("B")
# zewei.take_exam("C")
# zewei.print_info()
# zewei.graduate()
# zewei.take_exam("A")
# zewei.take_exam("B")
# zewei.take_exam("C")
# zewei.take_exam("A")
# zewei.take_exam("B")
# zewei.take_exam("C")
# zewei.take_exam("A")
# zewei.take_exam("B")
# zewei.take_exam("C")
# zewei.take_exam("A")
# zewei.take_exam("B")
# zewei.take_exam("C")
# zewei.print_info()
# zewei.graduate()
# b = Student()
# c = Student()

class Employee(object):

	def __init__(self, name, ID, title, salary, manager=None):
		self.name = name
		self.ID = ID
		self.title = title
		self.salary = salary
		self.manager = manager

	def get_info(self):
		return "(Employee name: {}, title: {}, salary: {}, manager: {})".format(self.name, self.title, self.salary, self.manager.get_info() if self.manager is not None else "")

	def __eq__(self, other):
		return self.ID == other.ID

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




