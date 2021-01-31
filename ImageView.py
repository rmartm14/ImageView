# Image Viewer
# Rafael Martínez Matías

import PySimpleGUI as sg
import os.path

sg.theme("TealMono")

# Title of the window
title = "Image View"

# Layout of the window
# Item Selector Column
itemSelectorColumn = [
    [
        # Texto before the selector
        sg.Text("Image Folder:"),
        # Bar with the folder route
        sg.Input(size=(30, 1), background_color="white",
                 enable_events=True, key="-FOLDER-", disabled=True),
        # File Selector
        sg.FolderBrowse()
    ],
    [
        # Image Selector
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],

]

layout = [
    [sg.Column(itemSelectorColumn),
     sg.VSeparator(),
     ]

]

# window
window = sg.Window(title=title, layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
window.close()
