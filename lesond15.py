with open('fl.txt', 'wt', encoding='utf-8') as inFile:
	num = int(input('Введи число - '))
	line = str('1/ ' + str(num) + ' = ' + str(1 / num))
	print(line)
	inFile.write (line)
	