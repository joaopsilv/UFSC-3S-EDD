def bucket_sort(array):
    num_buckets = len(array)
    buckets = [[] for _ in range(num_buckets)]

    for element in array:
        index = int(element * num_buckets)  # Função de distribuição para números reais entre 0 e 1
        buckets[index].append(element)

    for bucket in buckets:
        bucket.sort()  # Ao invés de sort(), idealmente, seria qualquer algoritmo simples de ordenação

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array
