# First try to PySimpleGui

import PySimpleGUI as sg

# First Window
# Title: The title of the window
title = "Image Viewer"
# Layour: To set the layout that uses the page
layout = [[sg.Text("Hello From Py")], [sg.Button("Confirm")]]
# margins: Set window margins
window = sg.Window(title=title, layout=layout, margins=(100, 50))

# Main event loop
while True:
    event, values = window.read()
    # Stop the program when closes windows or make ok
    if event == "Confirm" or event == sg.WIN_CLOSED:
        break
window.close()
