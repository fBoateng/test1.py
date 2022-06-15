patient_name = input('Please enter patient\'s name? ')
patient_age = input('Please enter patient\'s age? ')
patient_temp = input('Please enter patient\'s temperature? ')
patient_diagnosis = input('Please enter patient\'s diagnosis? ')

patient_data = {patient_name: patient_age, patient_temp: patient_diagnosis}
#patient_data = []
question = input('Will you make another entry? ').title()

while question == 'Yes':
    patient_name = input('Please enter patient\'s name? ')
    patient_age = input('Please enter patient\'s age? ')
    patient_temp = input('Please enter patient\'s temperature? ')
    patient_diagnosis = input('Please enter patient\'s diagnosis? ')
    question = input('Will you make another entry? ').title()

    patient_data = {patient_name: patient_age, patient_temp: patient_diagnosis}
if question == 'No':
    question_2 = input('Will you make a staff entry? ').title()
    while question_2 == 'Yes':
        staff_name = input('Please enter staff\'s name? ')
        staff_age = input('Please enter staff\'s age? ')
        staff_id = input('Please enter staff\'s id? ')
        staff_role = input('Please enter staff\'s role? ')
        staff_data = {staff_name: staff_age, staff_id: staff_role}
        question_2 = input('Will you make a staff entry? ').title()

    else:
        print('That will be all for today.')



