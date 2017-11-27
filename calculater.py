#функці додавання

def add(x, y):
	return x + y


def subtract(x, y):
	return x - y


def multiply(x, y):
	return x * y


def divide(x, y):
	return x / y


print("ВИБЕРИ ОПЕРАЦИЮ :")
print("1.Додавання")
print("2.Виднемание")
print("3.Множение")
print("4.Диление")

asd = input("Введи число(1/2/3/4):")

num1 = int(input("Введи перше число : "))
num2 = int(input("Введи друге число : "))

	
if asd == '1':
	print(num1,"+",num2,"=", add(num1,num2))

elif asd == '2':
	print(num1,"-",num2,"=", subtract(num1,num2))
	
elif asd == '3':
	print(num1,"*",num2,"=", multiply(num1,num2))

elif asd == '4':
	print(num1,"/",num2,"=", divide(num1,num2))
	


else: 
	print("Invalid input")

	