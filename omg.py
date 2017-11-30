def copy_decor(name = 'Denis'):
	 def decor(func):
	 	def wrapper(i):
			resp_file =func(i)
			
			with open(resp_file.name 'a') as file:
				file.write(name)
			return file	

		
		return wrapper
	return decor




@copy_decor(name = 'Denis')
def save_file()
with  open('some2.txt', 'w') as file:
	for line in list:
		file.write(line + '\n' )
	return file


close.file = save_my_file ([])