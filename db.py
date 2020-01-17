import psycopg2


def lerArquivos(): 
	arquivo = open('122.txt', 'r')
	texto = arquivo.read()
	sql = texto.split('\n\n')
	return sql

sql = lerArquivos() 

con = psycopg2.connect(host='localhost', database='Teste',
user='postgres', password='postgres')
cur = con.cursor()

for number in range(0, len(sql)):
	cur.execute(sql[number])

con.commit()
con.close()
print('Finalizando...')
print('-' * 100)
print('CONCLUIDO')