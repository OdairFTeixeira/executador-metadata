import PySimpleGUI as sg

sg.theme('Dark Blue 3')   # Add a touch of color
sg.theme_background_color('white')
# # All the stuff inside your window.
layout = [ [sg.Text('Bem vindo ao executador de metadatas', text_color='black', background_color='white')],
            [sg.Text('Usuario Postgres: ', size=(39, 1), text_color='black', background_color='white'),
             sg.Text('Senha Postgres:', size=(39, 1), text_color='black', background_color='white')],
            [sg.Input('postgres', size=(45, 1)), sg.Input('postgres', size=(45, 1))],
            [sg.Text('Em qual database deseja executar?', size=(39, 1), text_color='black', background_color='white')],
            [sg.Input(size=(92, 1))],
            [sg.Text('Informe a pasta dos scrips: ', text_color='black', background_color='white')],
            [sg.Input(size=(82, 1)), sg.FolderBrowse('Procurar')],
            [sg.Text('Arquivos encontrados: ', text_color='black', background_color='white')],
            [sg.Listbox(values=(), size=(92, 7))],
            [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Executador de Metadatas', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()