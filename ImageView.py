# Image Viewer
# Rafael Martínez Matías

import PySimpleGUI as sg
import os.path


# Title of the window
title = "Image View"

# Layout of the window
# Item Selector Column
itemSelectorColumn = [
    [
        # Texto before the selector
        sg.Text("Image Folder:"),
        # Bar with the folder route
        sg.Input(default_text=("C:/Users/rafam/Pictures"), size=(60, 1), background_color="white",
                 enable_events=True, key="-FOLDER-", disabled=True),
        # File Selector
        sg.FolderBrowse()
    ],
    [
        # Image Selector
        sg.Listbox(
            values=[], enable_events=True, size=(80, 20), key="-FILE LIST-",
        )
    ],

]

# image visualizer
imageViewerColumn = [
    [sg.Text("Choose an image from list on left")],
    [sg.Text(size=(100, 1), key="-TOUT-")],
    [sg.Image(k="-IMAGE", size=(200, 200))]
]

# MenuBar
menu_def = [['&File', ['!&Open', '&Save::savekey', '---', '&Exit::exit']],
            ['&Help', '&About...'], ]

layout = [
    [
        sg.MenuBar(menu_def)
    ],
    [sg.Column(itemSelectorColumn),
     sg.VSeparator(),
     sg.Column(imageViewerColumn)
     ]

]


# window
window = sg.Window(title=title, layout=layout,
                   size=(1920, 1080), resizable=True, ttk_theme="winnative", location=(0, 0))

while True:
    event, values = window.read()
    # Close the window
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    # Event of the input
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    # File chosen
    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE"].update(filename=filename)
        except:
            pass

window.close()
