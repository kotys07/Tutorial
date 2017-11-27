import math
import random as r  #рандом дорівнює r
from modul import hi as h, add as a, asd as s
try:
	import nomodule
except ImportError:
	print ("Такого модуля nomodule не существует")
print (math.pi)
print (r.random())
h()
print(a(15, 78))
print (s(12, 2))

	
	
