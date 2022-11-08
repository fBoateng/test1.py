import PySimpleGUI as sg
import qrcode
import os
import PIL

# sg.theme('LightGrey2')
# sg.set_options(font = 'roman 15')
col_a = [
    [sg.T('Please enter the amount you are purchasing? ')],
    [sg.T('Petrol: '), sg.I(k='-Input-', size=(15, 15), enable_events=True), sg.Submit('Submit', k='-Submit-')],
    [sg.T('Unit: '), sg.B('Litre', k='-Litre-', enable_events=True, button_color=('white', 'firebrick4'), p=10),
     sg.B('Gallon', k='-Gallon-', enable_events=True, button_color=('white', 'firebrick4'), p=10),
     sg.CloseButton('Close', p=15)],
    [sg.T('Output', key='-OUT-')]

]

col_b = [
    [sg.I(k='-IN-', size=15)],
    [sg.Spin(['km to mile', 'miles to km'], key='-UNIT-')],
    [sg.Button('Convert', key='-CONVERT-')],
    [sg.T('Output', key='-OUTPUT-')]
]

col_c = [
    [sg.T('Pay Mode')],
    [sg.CB('Cash', key='-C-', enable_events=True)],
    [sg.CB('Scan and Pay', key='-SAP-', enable_events=True)],
    [sg.Image(key='-IMG-')],
    [sg.Button('Generate',key='-Generate-', size=25), sg.Button('Gen', key='-litre-')]
]

col_d = [
    [sg.Image(filename='A1.png', size=(700, 120))]

]

layout = [
    [sg.Col(col_a)],
    [sg.HSep()],
    [sg.Col(col_b)],
    [sg.HSep()],
    [sg.Col(col_c)],
    [sg.VSep()],
    [sg.Col(col_d)]

]


def qrcode_gen(link):
    qr = qrcode.QRCode(
        box_size=5,
        border=5,
        version=1
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='grey')
    file_name = 'Qr' + '.png'
    path = os.path.join(os.getcwd(), file_name)
    img.save(path)
    return path


window = sg.Window('Buy Fuel', layout)

while True:
    e, v = window.read()
    if e == sg.WIN_CLOSED:
        break
    if e == '-Submit-':
        user_input = v['-Input-']
        if user_input.isnumeric():
            print(f'You entered {user_input} Cedis')
    if e == '-Litre-':
        user_input = float(v['-Input-'])
        litre = user_input / 11.501
        print(litre)
        window['-OUT-'].update(litre)
    if e == '-Gallon-':
        user_input = float(v['-Input-'])
        gallon = user_input / 43.536
        print(gallon)
        window['-OUT-'].update(gallon)
    if e == '-CONVERT-':
        input_value = v['-IN-']
        if input_value.isnumeric():
            match v['-UNIT-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f'{input_value} km are {output} miles.'
                # case 'mile to km':
                # output = round(float(input_value) / 0.6214, 2)
                # output_string = f'{input_value} mile are {output} km.'
            window['-OUTPUT-'].update(output_string)

    if e == '-Generate-':
        cde_qr = v['-Input-']
        qr_image_path = qrcode_gen(cde_qr)
        window['-IMG-'].update(filename=qr_image_path)
    if e == '-litre-':
        cde_qr1 = v['-SAP-']
        qr_image_path = qrcode_gen(cde_qr1)
        window['-IMG-'].update(filename=qr_image_path)





window.close()
