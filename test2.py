# M is the mark obtained by a student in 6 courses
M1 = int(input('Please enter marks for this subject'))
M2 = int(input('Please enter marks for this subject'))
M3 = int(input('Please enter marks for this subject'))
M4 = int(input('Please enter marks for this subject'))
M5 = int(input('Please enter marks for this subject'))
M6 = int(input('Please enter marks for this subject'))

tot = M6 + M5 + M4 + M3 + M2 + M1
AM = tot/6  # AM is average mark scored

print(str(AM) + ' ' + 'is your average mark')
if AM >= 90 and AM <= 100:
    print('grade A1, you have done brilliant')
elif AM >= 81 and AM >= 91:
    print('grade B2, you have done excellent')
elif AM >= 71 and AM >= 81:
    print('grade B2, you have done well')
elif AM >= 61 and AM >= 71:
    print('grade C1, you have done above average')
elif AM >= 51 and AM >= 61:
    print('grade C2, you have done average ')
elif AM >= 51 and AM >= 41:
    print('grade D, you have done poor')
elif AM >= 31 and AM >= 21:
    print('grade E, you have done very poor')
elif AM >= 0 and AM >= 21:
    print('grade F, you have done failed')
else:
    print('You have no score')
