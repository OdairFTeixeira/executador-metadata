import psycopg2
import os

arquivosPasta = []
for _, _, arquivo in os.walk(r'C:\Users\odair\java\workspace\Python testes\executador-metadata'):
    arquivosPasta.append(arquivo)

def arquivosTxt(array):
	arquivos = []
	for item in array:
		split = item.split('txt')
		if (len(split) == 2):
			arquivos.append(item)
	return arquivos

def lerArquivos(arquivo): 
	arquivo = open(arquivo, 'r')
	texto = arquivo.read()
	sql = texto.split('\n\n')
	return sql

arquivos = arquivosTxt(arquivosPasta[0])
print(arquivos)

con = psycopg2.connect(host='localhost', database='Teste',
user='postgres', password='postgres')
cur = con.cursor()

for arquivo in arquivos:
	sql = lerArquivos(arquivo)
	for number in range(0, len(sql)):
		cur.execute(sql[number])
	con.commit()
	print('Arquivo', arquivo, 'executado com sucesso!!')

con.close()
print('CONCLUIDO')