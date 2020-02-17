import PySimpleGUI as sg
import psycopg2
import os

icon_file = './icons/data.png'
sg.theme_background_color('#0e0e0e')
sg.set_options(icon=icon_file)
layout = [[sg.Text('Usuario Postgres: ', size=(45, 1), text_color='white', background_color='#0e0e0e'),
           sg.Text('Senha Postgres:', size=(39, 1), text_color='white', background_color='#0e0e0e')],
          [sg.Input('postgres', size=(45, 1), key='usuario'), sg.Input('postgres', size=(45, 1), key='senha')],
          [sg.Text('Database em que o script será rodado:', size=(39, 1), text_color='white',
                   background_color='#0e0e0e')],
          [sg.Input(size=(92, 1), key='database')],
          [sg.Text('Informe a pasta dos scrips: ', text_color='white', background_color='#0e0e0e')],
          [sg.Input(size=(82, 1), key='diretorio', enable_events=True), sg.FolderBrowse('Procurar')],
          [sg.Text('Arquivos encontrados: ', text_color='white', background_color='#0e0e0e')],
          [sg.Listbox(values=[], size=(92, 7), key='files')],
          [sg.Text(size=(64, 3), background_color='#0e0e0e'), sg.Button('Cancelar'), sg.Button('Executar')]]

window = sg.Window('Executador de Metadatas', layout)

def arquivosTxt(array):
    arquivos = []
    for item in array:
        split = item.split('.txt')
        if (len(split) == 2):
            arquivos.append(item)
    return arquivos


def lerArquivos(arquivo):
    arquivo = open(arquivo, 'r')
    texto = arquivo.read()
    sql = texto.split('\n\n')
    return sql


while True:
    event, values = window.read()

    if event in (None, 'diretorio'):
        arquivosPasta = []
        for _, _, arquivo in os.walk(values['diretorio']):
            arquivosPasta.append(arquivo)
        arquivos = arquivosTxt(arquivosPasta[0])
        window.FindElement('files').Update(values=arquivos)

    if event in (None, 'Executar'):
        con = psycopg2.connect(host='localhost', database=values['database'],
                               user=values['usuario'], password=values['senha'])
        cur = con.cursor()
        for arquivo in arquivos:
            sql = lerArquivos(arquivo)
            for number in range(0, len(sql)):
                cur.execute(sql[number])
            con.commit()
            print('Arquivo', arquivo, 'executado com sucesso!!')
        print('xXx --Concluido-- xXx')
        break

    if event in (None, 'Cancelar'):
        break
window.close()
