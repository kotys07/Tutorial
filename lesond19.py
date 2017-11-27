class Person :
	name = "Denis"
	age = 21
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	
	def set(self, name, age):
		self.name = name
		self.age = age
	
class Student (Person):
	course = 5
	
	def set(self, name, age, course):
		self.name = name
		self.age = age
		self.course = course


dima = Student ("Dima", 18)
#dima.set ("Dima", 18)
dima.set ("Dima", 18, 1)
#dima.course = 2
print ("Имя : ", dima.name,  ",возраст - ", dima.age, ",курс - ", dima.course)

ivan = Student ("Ivan", 21)
#ivan.set ("Ivan", 21)
ivan.set ("Ivan", 21, 4)
#ivan.course = 3
print ("Имя : ", ivan.name,  ",возраст - ",ivan.age, ",курс - ", ivan.course)

oleg = Student("Oleg", 22)	
#oleg.set ("Oleg", 22)
oleg.set ("Oleg", 22, 5)
#oleg.course = 5
print ("Имя : ", oleg.name,  ",возраст - ",oleg.age, ",курс - ", oleg.course)
