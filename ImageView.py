# Image Viewer
# Rafael Martínez Matías

import PySimpleGUI as sg
import os.path

sg.theme("TealMono")

# Title of the window
title = "Image View"

# Layout of the window
layout = [
    [
        sg.Text("Image Folder:"),
        sg.Input(size=(30, 1), background_color="white",
                 enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse()
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# window
window = sg.Window(title=title, layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
window.close()
