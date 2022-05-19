Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 'you'
b = 24
c = 5.6
d = False
print(type(a),type(b)type(c),type(d))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(type(a),type(b),type(c),type(d))
<class 'str'> <class 'int'> <class 'float'> <class 'bool'>

a = '6'
print(str(a))
6

a = '6'
print(int(a))
SyntaxError: multiple statements found while compiling a single statement

b= '6'
print(int(b))
6

c = 5.6
print(int(c))
5

d= False
print(int(d))
0
d=''
print(int(d))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(int(d))
ValueError: invalid literal for int() with base 10: ''


e = 'free'
print(str(e))
free

e = free
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    e = free
NameError: name 'free' is not defined

e=free
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    e=free
NameError: name 'free' is not defined


e = 'a'
print(int(e))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(int(e))
ValueError: invalid literal for int() with base 10: 'a'

f = 7
print(float(7))
7.0
f = 7
print(float(f))
7.0

g = 8
h = 10

print(float(f+g+h))
25.0

e = '8'

i = 0
j = 0
l = ''
print(bool(i), bool(j), bool(l))
False False False

i = 1
j = 1
l = 'k'
print(bool(i), bool(j), bool(l))
True True True
print(bool(i) + bool(j))
2

print(bool(i))
True


some_list = [1,2,3,4,5]
print(len(some_list))
5
some_list = ['f','e','t','d','a']
print(len(some_list))
5

new_lit = [20, 50, 3, 100, 500, 7]
print(max(new_list))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print(max(new_list))
NameError: name 'new_list' is not defined. Did you mean: 'new_lit'?
NameError: name 'new_list' is not defined. Did you mean: 'new_lit'?
SyntaxError: invalid syntax


new_list = [20, 50, 3, 100, 500, 7]
print(max(new_list))
500
print(min(new_list))
3
