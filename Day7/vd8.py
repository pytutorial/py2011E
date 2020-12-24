#vd8: Module
import m1
print(m1.add(2, 3))
print(m1.PI)

#Cach 2
from m1 import add
from m1 import PI

print(add(2, 3))
print(PI)

#Built-in modules
import math
print(math.sqrt(9))
