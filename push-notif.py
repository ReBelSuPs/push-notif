# hello_psg.py

import PySimpleGUI as sg

sg.theme('Dark Grey 8')
clients_column = [
    [sg.Text("Clients", font='Courier 20')],
    [sg.Text(size=(40, 1), key="-SPACE1-")],
    [sg.Text("Client 1", size=(40, 1))],
    [sg.Text("Client 2", size=(40, 1))],
    [sg.Text("Client 3", size=(40, 1))],
    [sg.Text("Client 4", size=(40, 1))],
]
message_column = [
    [sg.Text("Message", font='Courier 20')],
    [sg.Text(size=(60, 1), key="-SPACE2-")],
    [sg.Multiline(size=(60, 7), enable_events=True, key="-MESSAGE-")],
    [sg.Button('Send', key='_BUTTON_KEY_')],
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
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
