from datetime import *

# today's date.
TodayDate = date.today()
print(f'Today is {TodayDate}')
# user date of birth input
userDob = input('Please enter your date of birth? dd/mm/yyyy ')
# splitting date of birth input into lists
dobStr = userDob.split('/')
d_Dob = int(dobStr[0])
m_Dob = int(dobStr[1])
y_Dob = int(dobStr[2])

DoB = date(y_Dob, m_Dob, d_Dob)
# calculating days lived.
daysLived = (TodayDate - DoB).days
age = daysLived // 365
print(f'You are {age} old, and you have lived {daysLived} days.')
# days to next birthday
thisYear = TodayDate.year
nextBirthday = date(thisYear, m_Dob, d_Dob)
if TodayDate < nextBirthday:
    daysToNextbday = (nextBirthday - TodayDate).days
    print(f'Your birthday is {daysToNextbday} away.')
elif TodayDate == nextBirthday:
    print('Hurray!!! today is your birthday!!!!!')
else:
    nextBirthday = date(thisYear+1, m_Dob, d_Dob)
    daysToNextbday = (nextBirthday - TodayDate).days
    print(f'Your birthday is {daysToNextbday} days away.')