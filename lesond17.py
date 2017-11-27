class Person:
	name = "Denis"
	age = 21
	
	def set(self, name, age):
		self.name = name
		self.age = age


Denis = Person()
Denis.set ("Denis", 21)
print (Denis.name + " " + str(Denis.age))


Petr = Person()
Petr.set ("Petr", 22)
print (Petr.name + " " + str(Petr.age))