def suma_lista(lista):
    """
    Recibe una lista de números y calcula la suma total
    """
    total = 0
    for numero in lista:
        total = total + numero
    return total

# Ejemplo de uso
numeros = [10, 20, 30, 40, 50]
resultado = suma_lista(numeros)
print("Eduardo Salinas - Suma total:", resultado)
