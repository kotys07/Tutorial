def decoretor (func):
	def wrap ():
		print ("Код до виполнения функции")
		func ()
		print ("Код каторий сработав после функции")
	return wrap
	
def test (func):
	def wrap ():
		print ("Код до виполнения функции 2")
		func ()
		print ("Код каторий сработав после функции 2")
	return wrap

@decoretor
@test
def show ():
	print ("Я обичная функция")
show ()	
	
