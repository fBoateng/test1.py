import random
import string

serial_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
print(serial_code)

import PySimpleGUI as sg
import random
import string

sg.theme('DefaultNoMoreNagging')

layout = [[sg.Text('Serial Code Generator')],
          [sg.Text(size=(20,1), key='-OUTPUT-')],
          [sg.Button('Generate'), sg.Button('Quit')]]

window = sg.Window('Serial Code Generator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    elif event == 'Generate':
        serial_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        window['-OUTPUT-'].update(serial_code)

window.close()




'''if e == '-Litre-':
        user_input = float(v['-Input-'])
        litre = user_input/11.501
        print(litre)
    if e == '-Gallon-':
        user_input = float(v['-Input-'])
        gallon = user_input / 43.536
        print(gallon)'''




