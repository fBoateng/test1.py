Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

x
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x
NameError: name 'x' is not defined
x = sqrt(4)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x = sqrt(4)
NameError: name 'sqrt' is not defined
import math
x = math.sqrt(4)
print(x)
2.0
y = math.sqrt(15)
print(y)
3.872983346207417
d = math.sqrt(100)
print(d)
10.0
f = math.sqrt(120)
print(f)
10.954451150103322

print(math.floor)
<built-in function floor>
print(math.floor(2.9))
2
print(math.ceil(2.2))
3
print(math.ceil(2.9))
3

3**2
9
print(pow(2, 3))
8
print(pow(3, 2))
9
import math as a
f = a.sqrt(60)
print(f)
7.745966692414834
a.sqrt(60)
7.745966692414834
