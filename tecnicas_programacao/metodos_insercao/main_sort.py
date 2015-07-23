__author__ = 'douglas'

import random
import insercao_direta
import insercao_bolha
import insercao_selecao

def geraLista(tamLst):
	lst_resultados = []
	i = 0

	while i < tamLst:
		num = random.randint(0, 200000)

		if num not in lst_resultados:
			lst_resultados.append(num)
			i += 1
		# fim if
	# fim while

	return lst_resultados
# fim geraLista

def main():
	"""
	Tamanhos das listas para o teste de desempenho:
		100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000, 12100, 14400, 16900, 19600, 22500, 25600,
		28900, 32400, 36100, 40000, 44100, 48400, 52900, 57600, 62500, 67600, 72900, 78400, 84100, 90000
	"""
	# lst = geraLista(10000)
	lst = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
	lstBubble = lst[:]
	lstInsertion = lst[:]
	lstSelection = lst[:]

	print(lst)

	print("Bubble sort: %d troca(s)" %(insercao_bolha.bubbleSort(lstBubble)[1]))
	print("Selection sort: %d troca(s)" %(insercao_selecao.selectionSort(lstSelection)[1]))
	print("Insertion sort: %d troca(s)" %(insercao_direta.insertionSort(lstInsertion)[1]))


	# if ((lst[linha][cidade] > lst[linha+1][cidade]) or
	#    ((lst[linha][cidade] == lst[linha+1][cidade]) and (lst[linha][bairro] > lst[linha+1][bairro])) or
	# 	((lst[linha][cidade] == lst[linha+1][cidade]) and (lst[linha][bairro] == lst[linha+1][bairro]) and (lst[linha][logradouro] > lst[linha+1][logradouro]))

# fim main

main()