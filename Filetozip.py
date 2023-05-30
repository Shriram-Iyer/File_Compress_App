import PySimpleGUI as Py
from converter import make_archive

label1 = Py.Text("Select file to be compressed:")
input1 = Py.Input(key="1")
choose_button1 = Py.FilesBrowse("Choose", key="files")
label2 = Py.Text("Select destination folder:")
input2 = Py.Input(key="2")
choose_button2 = Py.FolderBrowse("Choose", key="folder")
label3 = Py.Text("Select destination folder:")
input3 = Py.InputText(key="filename")
Convert_button = Py.Button("Compress")
output = Py.Text(key="output")
window = Py.Window("Excel to PDf",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [label3,input3],
                           [Convert_button, output]])
while True:
    event, values = window.read()
    if Convert_button:
        filePath = values['files'].split(";")
        destination = values['folder']
        filename = values['filename']
        pdf = make_archive(filePath, destination, filename)
        window["1"].update(value="")
        window["2"].update(value="")
        window["filename"].update(value="")
        window["output"].update(value="Compression Completed")
    elif event == Py.WIN_CLOSED:
        break

window.close()
