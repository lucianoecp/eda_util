def busca_sequencial(lista, chave):
    for i in range(len(lista)):
        if lista[i] == chave:
            return i
    return -1	

lista = [20, 5, 15, 24, 67, 45, 1, 76]
print(busca_sequencial(lista, 24))
print(busca_sequencial(lista, 100))