

userAge = [21, 22, 23, 24, 25]
userAge0 = userAge[0]
userAge1 = userAge[1]
userAge2 = userAge[2]
userAge3 = userAge[3]
print(userAge1, userAge2, userAge3, userAge0)
22 23 24 21
userAge.append(26)
print(userAge)
[21, 22, 23, 24, 25, 26]
print(len(userAge))
6
del userAge[3]
print(userAge)
[21, 22, 23, 25, 26]
print(userAge[1:3])
[22, 23]
print(userAge[-1:])
[26]
print(userAge[:-3])
[21, 22]
print(userAge[-1:-3])
[]
print(userAge[-1:-2])
[]
print(userAge[1:-1])
[22, 23, 25]
print(userAge[1:3])
[22, 23]
print(userAge[-3:-1])
[23, 25]
X = userAge.copy()
print(X)
[21, 22, 23, 25, 26]
[21, 22, 23, 25, 26]
[21, 22, 23, 25, 26]


X.remove(21)
print(X)
[22, 23, 25, 26]
[22, 23, 25, 26]
[22, 23, 25, 26]
X.pop()
26
print(X)
[22, 23, 25]

Y.sort()
print(Y)
[21, 22, 23, 24, 25, 30, 30]
Y[4]= 45
print(Y)
[21, 22, 23, 24, 45, 30, 30]
Y.append(5)
print(Y)
[21, 22, 23, 24, 45, 30, 30, 5]
print(Y+X)
[21, 22, 23, 24, 45, 30, 30, 5, 21, 22, 23, 24, 25]
X.insert(4,'001')
print(X)
[21, 22, 23, 24, '001', 25

