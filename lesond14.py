#f = open ('fl.txt', 'rt') 
#print (f.read ())
#for line in f:
#	print (line)
	
#це спопсоби перегляду файлу

f = open ('fl.txt', 'w')
f.write ('Hi. it\'s me!\nTest')
f.close ()

f = open ('fl.txt', 'r')
print (f.read ())
f.close ()




