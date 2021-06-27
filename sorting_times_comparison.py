import random
import time
from matplotlib import pyplot as plt
import sys


def swap(arr, index_1, index_2):
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]  # Python swap.


'''Bubble Sort O(n^2)'''


def bubbleSort(a):
    n = len(a)
    intercambio = False
    # Iterating all array.
    for i in range(n-1):
        aux = n-1-i
        # It is shorter everytime, because bigger ones are going to be at the end, and so on, and so on...
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                swap(a, j, j+1)
                intercambio = True
        if not intercambio:
            return


'''Insertion Sort O(n^2)'''


def InsertionSort(a):
    n = len(a)
    for i in range(1, n):
        val = a[i]
        j = i-1
        while(j >= 0) and (a[j] > val):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = val


'''Merge SortO(nlogn)'''


def mergeSort(a):
    if(len(a)) == 1:
        return
    middle = len(a) // 2
    left = a[:middle]
    right = a[middle:]
    mergeSort(left)
    mergeSort(right)
    merge(left, right, a)


def merge(left, right, a):
    lfinger = 0
    rfinger = 0
    for i in range(len(a)):
        if((rfinger >= len(right)) or (lfinger < len(left) and left[lfinger] < right[rfinger])):
            a[i] = left[lfinger]
            lfinger += 1
        else:
            a[i] = right[rfinger]
            rfinger += 1


'''QuickSort O(nlogn)'''


def Quicksort(a, l, r):
    pivot = round(random.random()*len(a))
    a[pivot], a[r] = a[r], a[pivot]


def graficarTiempos(numDatos, tiemposBurbuja, tiemposMerge, tiemposQuick, tiemposInsertion, case):
    '''Diseños para c/u de las lineas en la grafica, junto con su color y su rastro'''
    fig, ax = plt.subplots()
    ax.plot(numDatos, tiemposBurbuja,
            label="Ordenamiento de la Burbuja", marker="*", color="r")
    ax.plot(numDatos, tiemposMerge,
            label="Ordenamiento de Merge", marker=".", color="g")
    ax.plot(numDatos, tiemposQuick,
            label="Ordenamiento de QuickSort", marker="o", color="b")
    ax.plot(numDatos, tiemposInsertion,
            label="Ordenamiento de InsertionSort", marker="x", color="y")
    '''Mando a imprimir'''
    ax.set_xlabel("Numero de Datos ")
    ax.set_ylabel("Tiempo [s]")
    ax.grid(True)
    ax.legend(loc=2)
    plt.title(case)
    plt.show()


def eficienciaAlgoritmos(numDatos, case):
    tiemposBurbuja = []
    tiemposMergeSort = []  # Creamos las listas vacias para medir tiempo
    tiemposQuick = []
    tiemposInsertion = []
    for n in numDatos:
        lista_Burbuja = random.sample(range(0, 1000000), n)  # genera(n)
        if case == "Mejor de los casos":
            print("\n\t", case)
            lista_Burbuja.sort()
        elif case == "El peor de los casos":
            print("\n\t", case)
            lista_Burbuja.sort(reverse=True)
        else:
            print("\n\t", case)
        lista_MergeSort = lista_Burbuja.copy()
        lista_Quick = lista_Burbuja.copy()
        lista_Insertion = lista_Burbuja.copy()

        print("\n=========\n")
        t0 = time.monotonic()  # Toma el tiempo (preferentemente largo) que nunca se moverá para atrás ni aunque cambies la configuracion del sistema
        bubbleSort(lista_Burbuja)  # La mando a hacer el bubbleSort
        dt = round(time.monotonic() - t0, 6)
        tiemposBurbuja.append(dt)  # meto el tiempo marcado
        print("\nBurbuja(n={}): \tTiempo transcurrido: {} seg".format(n, round(dt, 5)))

        t0 = time.monotonic()
        MergeSort(lista_MergeSort)
        dt = round(time.monotonic() - t0, 6)
        tiemposMergeSort.append(dt)
        print("MergeSort(n={}): \tTiempo transcurrido: {} seg".format(n, round(dt, 5)))

        t0 = time.monotonic()  # Toma el tiempo (preferentemente largo) que nunca se moverá para atrás ni aunque cambies la configuracion del sistema
        # La mando a hacer el QuickSort
        RandomizedQuickSort(lista_Quick, 0, len(lista_Quick)-1)
        dt = round(time.monotonic() - t0, 6)
        tiemposQuick.append(dt)  # meto el tiempo marcado
        print("QuickSort(n={}): \tTiempo transcurrido: {} seg".format(n, round(dt, 5)))

        t0 = time.monotonic()
        InsertionSort(lista_Insertion)
        dt = round(time.monotonic() - t0, 6)
        tiemposInsertion.append(dt)
        print("InsertionSort(n={}): \tTiempo transcurrido: {} seg".format(
            n, round(dt, 5)))
    return tiemposBurbuja, tiemposMergeSort, tiemposQuick, tiemposInsertion


def main():
    sys.setrecursionlimit(10000)
    for k in range(1, 4):
        cases = {1: 'Mejor de los casos',
                 2: 'Aleatorio', 3: 'El peor de los casos'}
        # numDatos = [100,200,300,400,....,2000]
        # Haremos 2000 datos en una lista para graficarlos posteriormente
        numDatos = [n*100 for n in range(1, 51)]
        tiemposBurbuja = []
        tiemposMerge = []
        tiemposQuick = []
        tiemposInsertion = []
        tiemposBurbuja, tiemposMerge, tiemposQuick, tiemposInsertion = eficienciaAlgoritmos(
            numDatos, cases[k])
        graficarTiempos(numDatos, tiemposBurbuja, tiemposMerge,
                        tiemposQuick, tiemposInsertion, cases[k])


main()
