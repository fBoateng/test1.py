u = []
a = []
d = []
sn = []
sa = []
sid = []
#numOfEntries = input('Please enter the number entries to be made? ')
#while numOfEntries is True:
user = input('Please enter patient\'s name? ')
u.append(user)
age = input('Please enter patient\'s age? ')
a.append(age)
diagnosis = input('Please enter patient\'s diagnosis? ')
d.append(diagnosis)
patients = input('Will you make another entry? ').title()

if patients == 'Yes':
    user1 = input('Please enter patient\'s name')
    u.append(user1)
    age1 = input('Please enter patient\'s age? ')
    a.append(age1)
    diagnosis1 = input('Please enter patient\'s diagnosis? ')
    d.append(diagnosis1)
    patients = input('Will you make another entry? ')
elif input('Will you make a staff entry? ').title():
    staff = input('Please enter staff\'s name? ')
    sn.append(user)
    age = input('Please enter staff\'s age? ')
    sa.append(age)
    id = input('Please enter staff\'s id? ')
    sid.append(id)
    patients = input('Will you make another entry? ').title()

else:
    print('That is all for today.')

