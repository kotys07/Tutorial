x = int (input("Введите число : "))
y = int (input("Введите втарое число : "))

try:
	res = x / y
except ZeroDivisionError:
	print ("ви ввели ноль")
	res = "на ноль не делят"
print (res)


try:
	i = int(input ("введи :"))
except ValueError:
	print ("ви ввели не число ")
	i = "а нада число"
print (i)
