def heap_sort(array):
    lenght = len(array)

    # Construir o heap máximo
    for i in range(lenght // 2 - 1, -1, -1):
        heapify(array, lenght, i)

    # Extrair elementos do heap
    for i in range(lenght-1, 0, -1):
        array[0], array[i] = array[i], array[0]     # Move a raiz atual para o final
        heapify(array, i, 0)                        # Chama heapify na subárvore reduzida

def heapify(array, lenght, i):
    largest = i           # Inicializa largest como raiz
    left = 2 * i + 1      # Filho à esquerda
    right = 2 * i + 2     # Filho à direita

    # Se o filho à esquerda é maior que a raiz
    if left < lenght and array[left] > array[largest]:
        largest = left

    # Se o filho à direita é maior que a raiz
    if right < lenght and array[right] > array[largest]:
        largest = right

    # Se largest não é a raiz
    if largest != i:
        array[i], array[largest] = array[largest], array[i]     # Troca a raiz com o maior filho
        heapify(array, lenght, largest)                         # Recursivamente ajusta a subárvore afetada
        