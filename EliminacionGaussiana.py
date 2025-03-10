matriz = []

def llenarmatriz():
    global matriz
    matriz = []
    print('Método para llenar una matriz 3x3')
    for i in range(3):
        fila = []
        for j in range(3):
            valor = int(input(f'Ingrese el valor para la posición [{i}][{j}]: '))
            fila.append(valor)
        matriz.append(fila)

def mostrarmatriz():
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=' ')
        print()

llenarmatriz()
mostrarmatriz()
