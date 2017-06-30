class Student(object):
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


