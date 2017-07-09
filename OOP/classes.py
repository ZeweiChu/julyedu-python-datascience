
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

class Employee(object):

	def __init__(self, name, title, salary, manager=None):
		self.name = name
		self.title = title
		self.salary = salary
		self.manager = manager

	def get_info(self):
		return "(Employee name: {}, title: {}, salary: {}, manager: {})".format(self.name, self.title, self.salary, self.manager.get_info() if self.manager is not None else "")

july = Employee("July", "CEO", 99999999)
print(july.get_info())
zewei = Employee("Zewei", "Lecturer", 1, july)
print(zewei.get_info())








