class student:
	grade = 10
	print("Hi I am a student of grade", grade)

ob = student()


class Student:
	grade = 10
	name = "Penguin"
	
	def introduction(self):
		print("Hi I am a student")

	def details(self):
		print("My name is", self.name)
		print("I study in Grade", self.grade)

ob = Student()
ob.introduction()
ob.details()