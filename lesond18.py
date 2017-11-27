class Car:
	wheels = 4
	model =  "Some"
	speed = "Some"
	
	def set(self, wheels, model, speed):
		self.wheels = wheels
		self.model = model
		self.speed = speed
	
	def getAll (self):
		print ("Автомобиль ", self.model," , " "может ехать за скорастю - ",self.speed, " , " "на всех"" , ",  self.wheels ," " "колесах!!!")
		pass
	


	
class Motorcycle (Car):
	engine = "Default"
	
	def change (self, engine):
		self.engine = engine
		print ("Двигатель мотоцикла установлен как : " + engine)

	def gitAll (self):
		print ("Мотоцикл ", self.model," , " "может ехать за скорастю - ",self.speed, " , " "на всех"" , ",  self.wheels ," " "колесах!!!")
		pass

		
BMV = Car()
BMV.set (4, "BMV", 280)
BMV.getAll ()

Audi = Car ()
Audi.set (4, "Audi", 250)
Audi.getAll ()

print ("")

harley = Motorcycle ()
harley.change = ("Powerfull")
harley.set (2, "Harley", 200)
harley.gitAll ()
		