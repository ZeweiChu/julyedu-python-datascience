class Student(object):
	job = "student"
	def __init__(self, name, level=1):
		self.name = name
		self.level = level

	def take_exam(self, grade):
		if grade.upper() in ['A', 'B', 'C']:
			self.level += 1
		return self.level
		
	def graduate(self):
		if self.level >= 12:
			print("Congratulations, you've graduated!")
			return True
		else:
			print("Sorry, you need to pass {} more course exams".format(12-self.level))
			return False

july = Student("July", 12)
xiaoyang = Student("Xiaoyang", 8)
zewei = Student("Zewei", 1)


class Employee(object):

	'''
		name: name of the employee
		manager: manager of the employee
		salary: salary of the employee
		title: title of the employee
	'''
	def __init__(self, name, title, salary, manager=None):
		self.name = name
		self.title = title
		self.salary = salary
		self.manager = manager

	def get_info(self):
		return "(Employee name: {}, title: {}, salary: {}, manager: {})".format(self.name, self.title, self.salary, self.manager.get_info() if self.manager is not None else "")

july = Employee("July", "CEO", 9999999)
zewei = Employee("Zewei", "Lecturer", 1, july)
print(zewei.get_info())

'''


'''
