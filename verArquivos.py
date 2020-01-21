import os

arquivosPasta = []

for _, _, arquivo in os.walk('/home/odair/java/workspace/pyhton/DB project'):
    arquivosPasta.append(arquivo)


def apenasTxt(array):
	arquivos = []
	for item in array:
		split = item.split('txt')
		if (len(split) == 2):
			arquivos.append(item)
	return arquivos

arquivos = apenasTxt(arquivosPasta[0])


teste = arquivos
print(teste)