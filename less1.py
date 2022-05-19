Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


a = 'you'
b = 24
c = 5.6
d = False
print(type(a), type(b),type(c),type(d))








a = 1
b = 'me'
c = 5.6
print(a,b,c)
1 me 5.6


print(a + c)
6.6


me = 'He will come tomorrow.'
print(me.title())
He Will Come Tomorrow.
print(me.upper())
HE WILL COME TOMORROW.
print(me.lower())
he will come tomorrow.
you= 'what are you doing?'
print(me + you)
He will come tomorrow.what are you doing?
me = 1
you = 27
print(me + you)
28
us = 1
we = 27
print(me + us +you +we)
56
print('me' + us + 'you' +we)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print('me' + us + 'you' +we)
TypeError: can only concatenate str (not "int") to str


print('me'+'us'+'you'+'we')
meusyouwe


a = 'This is a \n new line'
print(a)
This is a 
 new line
b =  '\t this is tab space'
print(b)
	 this is tab space
A = 'Hello'
print(a)
This is a 
 new line
print(A)
Hello
print(A.strip())
Hello
print(A.rstrip())
Hello
print(A.lstrip())
Hello
a = 'He is awesome'
print(len(a))
13
a = 'heisawesome'
print(len(a))
11




water = 4
rice = 5
full meal = water + rice
SyntaxError: invalid syntax

full_meal = water + rice
print(full_meal)
9
print(len(full_meal))
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(len(full_meal))
TypeError: object of type 'int' has no len()
f= 'good morning ghana'
print(f.upper())
GOOD MORNING GHANA
print(f.strip())
good morning ghana
print(f.title())
Good Morning Ghana
print(len(f))
18
18
18


s='see you'
d='later'
print(s+d)
see youlater
print(d+s)
latersee you
print(len(d))
5

a = 45.3
b = 23
print(a + b)
68.3

90 = w
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
w = 456
e = 230
print(w+e)
686

V = 'WE ARE THE LAST OF OUR KIND'
print(V.lower)
<built-in method lower of str object at 0x000001B821C55160>

print(V.lower())
we are the last of our kind
print(V.title())
We Are The Last Of Our Kind

er = 'emergency rooms'
print(len(er))
15
3/2
1.5
z = 1.5
x = 34
print(x+z)
35.5




