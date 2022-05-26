import random


# def insertion_sort(lista: list):
#     print(lista)
#     for i in range(len(lista)):
#         for j in range(i, len(lista)):
#             if lista[i] > lista[j]:
#                 standard = lista[i]
#                 lista[i] = lista[j]
#                 lista[j] = standard
#                 print(lista)
#
def bubbleSort(list):
    pass


def insertionSort(list):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j] < list[j - 1]:
            list[j], list[j - 1] = list[j - 1], list[j]  # swap
            j -= 1
    return list


def selectionSort(list):
    for i in range(len(list) - 1):
        min_pointer = i  # ponteiro que aponta para o menor elemento
        for j in range(i + 1, len(list)):
            if list[j] < list[min_pointer]:
                min_pointer = j  # minimo fica na posição 'j' (a que possui o menor vetor no momento)
        aux = list[i]
        list[i] = list[min_pointer]
        list[min_pointer] = aux


def mergesort(list, inicio=0, fim=None):
    if fim is None:
        fim = len(list)
    if (fim - inicio > 1):
        meio = (fim + inicio) // 2
        mergesort(list, inicio, meio)
        mergesort(list, meio, fim)
        merge(list, inicio, meio, fim)


def merge(list, inicio, meio, fim):
    left = list[inicio:meio]
    right = list[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            list[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            list[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            list[k] = left[top_left]
            top_left = top_left + 1
        else:
            list[k] = right[top_right]
            top_right = top_right + 1


def quickSort(list, inicio=0, fim=None):
    if fim is None:
        fim = len(list) - 1  # pivo começa do  final
    if inicio < fim:
        p = partition(list, inicio, fim)
        # recursivamente na sublista à esquerda (menores)
        quickSort(list, inicio, p - 1)
        # recursivamente na sublista à direita (maiores)
        quickSort(list, p + 1, fim)


def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        # j sempre avança, pois representa o elementa em análise
        # e delimita os elementos maiores que o pivô
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            # incrementa-se o limite dos elementos menores que o pivô
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i


def heapSort(lista):
    pass


lista = [29, 10, 14, 37, 15]
# selectionSort(lista)

any_numbers = random.sample(range(1, 1000), 20)

already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28,
                  32, 34, 39, 40, 42, 76, 87, 99, 112]

inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51,
            50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1]

print(insertionSort(lista))
