def busca_sequencial(lista, chave):
    for i in range(len(lista)):
        if lista[i] == chave:
            return i

    return -1	


def busca_binaria(lista, chave):
    inicio = 0
    fim = len(lista)-1
    
    while inicio <= fim:
        meio = (inicio + fim)//2
        if lista[meio] == chave:
            return meio
        elif lista[meio] > chave:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1
