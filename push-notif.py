# hello_psg.py

import PySimpleGUI as sg

sg.theme('Dark Grey 8')
clients_column = [
    [sg.Text("Clients", font='Courier 20')],
    [sg.Text(size=(40, 1), key="-SPACE1-")],
    [sg.Text("Client 1", size=(40, 1), font='Calibri 14')],
    [sg.Text("Client 2", size=(40, 1), font='Calibri 14')],
    [sg.Text("Client 3", size=(40, 1), font='Calibri 14')],
    [sg.Text("Client 4", size=(40, 1), font='Calibri 14')],
]
message_column = [
    [sg.Text("Message", font='Courier 20')],
    [sg.Text(size=(60, 1), key="-SPACE2-")],
    [sg.Multiline(size=(60, 7), font='Calibri 13',
                  enable_events=True, key="-MESSAGE-")],
    [sg.Text(size=(60, 1), key="-SPACE3-")],
    [sg.Button('Send', font='Calibri 16', key='_BUTTON_SEND_'), sg.Button(
        'Send to all', font='Calibri 16', key='_BUTTON_SEND_TO_ALL_')],
]

layout = [
    [
        sg.Column(clients_column),
        sg.VSeparator(),
        sg.Column(message_column),
    ]
]

# Create the window
window = sg.Window("Demo", layout, margins=(50, 100))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "_BUTTON_SEND_":
        msg = values["-MESSAGE-"]
        print(msg)
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
