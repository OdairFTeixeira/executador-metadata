import PySimpleGUI as sg

arquivos = []

sg.theme_background_color('white')
layout = [  [sg.Text('Usuario Postgres: ', size=(39, 1), text_color='black', background_color='white'),
             sg.Text('Senha Postgres:', size=(39, 1), text_color='black', background_color='white')],
            [sg.Input('postgres', size=(45, 1), key='usuario'), sg.Input('postgres', size=(45, 1), key='senha')],
            [sg.Text('Database em que o script será rodado:', size=(39, 1), text_color='black',
                     background_color='white')],
            [sg.Input(size=(92, 1), key='database')],
            [sg.Text('Informe a pasta dos scrips: ', text_color='black', background_color='white')],
            [sg.Input(size=(82, 1), key='diretorio'), sg.FolderBrowse('Procurar')],
            [sg.Text('Arquivos encontrados: ', text_color='black', background_color='white')],
            [sg.Listbox(values=[], size=(92, 7), key='files')],
            [sg.Text(size=(64, 3), background_color='white'), sg.Button('Cancelar'), sg.Button('Executar')]]


window = sg.Window('Executador de Metadatas', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancelar'):
        break
    print(values['usuario'], values['senha'], values['database'], values['diretorio'], values['files'])
    window.FindElement('files').Update(values=arquivos)

window.close()
