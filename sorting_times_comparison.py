import random
import time
from matplotlib import pyplot as plt
import sys


def swap(arr, index_1, index_2):
    arr[index_1],arr[index_2] = arr[index_2],arr[index_1] #Python swap.


'''Bubble Sort O(n^2)'''
def bubbleSort(a):  
    n = len(a)
    intercambio = False
    for i in range(n-1): #Iterating all array.
        aux = n-1-i
        for j in range(n-1-i): #It is shorter everytime, because bigger ones are going to be at the end, and so on, and so on...
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


def merge(array, left, right):
    # iteradores
    lfinger = 0
    rfinger = 0
    for k in range(len(array)):
        # Pregunta si alguno de los arreglos está desbordado, hace más enfasis en que si todavia quedan elementos en el arreglo izquierdo.
        if (rfinger >= len(right) or (lfinger < len(left) and left[lfinger] < right[rfinger])):
            array[k] = left[lfinger]
            lfinger += 1  # En esta parte hace los asignamientos nuevos al arreglo original, osea intercala las listas
        else:
            array[k] = right[rfinger]
            rfinger += 1


def MergeSort(array):
    if len(array) > 1:  # COND.BASE, Por definición una lista de un elemento ya está ordenada
        Half_array = len(array) // 2  # Divido a la mitad el arreglo
        left = array[:Half_array]
        right = array[Half_array:]
        MergeSort(left)  # Empezamos a separar el lado izquierdo recursivamente
        # "                          " derecho  "             "
        MergeSort(right)
        # UNIMOS y vamos modificando al original dentro de merge()
        merge(array, left, right)
    else:
        return


'''QuickSort O(nlogn)'''


def Particionar(a, p, r):
    piv = a[r]  # Agarra un pivote (EL DEL FINAL EN NUESTRO CASO)
    inMenores = p-1  # El indice menores
    for j in range(p, r):  # Del primero al ultimo de esa lista
        if(a[j] <= piv):  # Si el primer elemento es menor que el pivote, intercambio a los menores
            inMenores += 1  # Ahora si, lo agarro y lo voy a cambiar
            a[inMenores], a[j] = a[j], a[inMenores]
    a[inMenores+1], a[r] = a[r], a[inMenores+1]
    return inMenores+1  # Le regreso el indice de enmedio para que sepa donde va a partir


def RandomizedQuickSort(a, p, r):
    # Es decir, si el indice menor es menor al mayor (Si la lista aun no está vacia)
    if p < r:
        '''RANDOMIZED QUICKSORT 
        Eligo a un numero al azar como pivote y 
        lo meto al final del arreglo
        '''
        i = random.randint(p, r)
        a[i], a[r] = a[r], a[i]  # swap(randPivot,elementoFinal del arreglo)
        q = Particionar(a, p, r)  # Le da la micha
        RandomizedQuickSort(a, p, q-1)  # Reordena y parte la primera mitad
        RandomizedQuickSort(a, q+1, r)  # Reordena y parte la primera mitad


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
        RandomizedQuickSort(lista_Quick, 0, len(lista_Quick)-1)# La mando a hacer el QuickSort
        dt = round(time.monotonic() - t0, 6)
        tiemposQuick.append(dt) # meto el tiempo marcado
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
