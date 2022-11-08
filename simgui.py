import PySimpleGUI as sg


sg.theme('SandyBeach')

menu_button = ['menu', ['file', 'edit', 'view', 'settings', ['general', 'audio', 'video', 'graphics'], 'help']]

sports = ['Track and Field', 'Basketball', 'Swimming', 'Football']


col_a = [
    [sg.CB('Track and Field', key='Category', text_color='navy')],
    [sg.CB('Basketball', key='Category', text_color='green')],
    [sg.CB('Swimming', key='Category')],
    [sg.CB('Football', key='Category')]

]

col_b = [
    [sg.ButtonMenu('Menu', menu_def=menu_button)],
    [sg.T('Application')],
    [sg.I(key='-NAME-')],
    [sg.B('OK', button_color='purple')], [sg.Cancel('Cancel', button_color='red', p=3)],
    [sg.DD(sports, s=(15, 10), default_value='sports', k='-DD-')]

]
age = [12, 11, 10, 12]
col_c = [
    [sg.DD(age, size=(15, 10), p=3, default_value='age', k='-DD-', enable_events=True, expand_x=5)],
    [sg.CB('6-10', p=5)],
    [sg.CB('10-15', p=5, enable_events=True)],
    [sg.StatusBar('status', key='-SB-', size=(1, 1), justification='center', relief='groove')]
]

layout = [
    [sg.Col(col_a), sg.VSep(), sg.Col(col_b), sg.VSep(), sg.Col(col_c)],
    [sg.HSep()],
    [sg.LB(sports, size=(25, 10), key='-LB-'), sg.ML(key='-ML-', size=(20, 10), default_text='NOTES')]
]

window = sg.Window('New Miracle', layout)

event, values = window.read()
if event == 'Cancel':
    window.close()
elif event == 'OK':
    sg.popup('Your name is ', values['-NAME-'])


print(event, values)

