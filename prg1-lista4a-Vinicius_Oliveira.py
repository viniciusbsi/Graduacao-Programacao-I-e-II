#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Lista de exercícios 4a

# Exercícios apenas com for (sempre que possível), e sem funções embutidas.

def ondernamento_contrario(lista):
    return lista[::-1]
    

def intercalamento_listas(lista1,lista2):
    #''' Usando 'lista1' e 'lista2', ambas do mesmo comprimento,
    #crie uma nova lista composta pelo
    #intercalamento entre as duas.'''
    lista_intercalada = []
    for i, valor in enumerate(lista1):
        var1 = lista1[i]
        var2 = lista2[i]
        lista_intercalada.append(var1)
        lista_intercalada.append(var2)
    return lista_intercalada    

def im_pares(lista):
    #''' Separe em listas os impares e pares, dos inteiros da 'lista' '''
    listaPar = []
    listaImpar = []
    for i, valor in enumerate(lista):
        if (valor%2 == 0):
            var = lista[i]
            listaPar.append(var)
        else:
            var = lista[i]
            listaImpar.append(var)
    return (listaPar, listaImpar)

def maior_menor(lista):
    #''' Calcule o maior e o menor numero da 'lista' '''
    maior = lista[0]
    menor = lista[0] 
    for valor in lista:
        if (valor < menor):
            menor = valor
        if (valor > maior):
            maior = valor
    return (maior, menor)

def dar_troco(valor_a_pagar, valor_em_dinheiro):
    ''' Calcule o troco numa lista com notas de 1,2,5,10,20,50 com sua 
    quantidade de notas sem considerar centavos
    ex: 1 e 10 retorna troco_notas_quantidade = [5,2] quantidade_notas = [1,2] '''
    tipos_notas = [50,20,10,5,2,1]
    nova_lista = []
    troco = (valor_em_dinheiro - valor_a_pagar)
    if valor_em_dinheiro < valor_a_pagar:
        return nova_lista
    for nota in tipos_notas:
        notas = troco//nota
        troco = troco%nota 
        if notas>0: 
            nova_lista.append((nota, notas))
    return nova_lista

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0 

def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = ' Falhou.'
    else:
        prefixo = ' Passou.'
        acertos += 1
    print ('%s Esperado: %s \tObtido: %s' % (prefixo,repr(esperado), 
        repr(obtido)))

def main():
    lista1 = [1,2,3,4,5,6,7,8,9,10]
    lista2 = [-1,0]
    lista3 = [-10,0,10,2,100,-100,-100.1]
    lista4 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
    lista5 = [1,3,5,7,9]
    lista6 = [2,4,6,8,10]

    print(' Listas invertidas:')
    test(ondernamento_contrario(lista1), ([10,9,8,7,6,5,4,3,2,1]))
    test(ondernamento_contrario(lista2), ([0,-1]))
    test(ondernamento_contrario(lista3), ([-100.1,-100,100,2,10,0,-10]))

    print(' Lista Intercalada:')
    test(intercalamento_listas(lista5,lista6), [1,2,3,4,5,6,7,8,9,10])

    print(' Lista de pares e impares:')
    test(im_pares(lista1), ([2,4,6,8,10],[1,3,5,7,9]))
    test(im_pares(lista5), ([],[1,3,5,7,9]))
    test(im_pares(lista6), ([2,4,6,8,10],[]))

    print(' Maior e o menor da lista:')
    test(maior_menor(lista1), (10,1))
    test(maior_menor(lista2), (0,-1))
    test(maior_menor(lista3), (100,-100.1))
    test(maior_menor(lista4), (-1,-10))

    print(' Troco do pagamento:')
    test(dar_troco(1,51), [(50,1)])
    test(dar_troco(1,101), [(50,2)])
    test(dar_troco(1,71), [(50,1),(20,1)])
    test(dar_troco(1,21), [(20,1)])
    test(dar_troco(1,41), [(20,2)])
    test(dar_troco(1,141), [(50,2),(20,2)])
    test(dar_troco(1,181), [(50,3),(20,1),(10,1)])
    test(dar_troco(1,11), [(10,1)])
    test(dar_troco(1,31), [(20,1),(10,1)])
    test(dar_troco(1,61), [(50,1),(10,1)])
    test(dar_troco(1,6), [(5,1)])
    test(dar_troco(1,5), [(2,2)])
    test(dar_troco(1,2), [(1,1)])
    test(dar_troco(1,4), [(2,1),(1,1)])
    test(dar_troco(1,201), [(50,4)])
    test(dar_troco(1,148), [(50,2),(20,2),(5,1),(2,1)])
    test(dar_troco(1,100), [(50,1),(20,2),(5,1),(2,2)])
    test(dar_troco(10,10), [])
    test(dar_troco(10,1), [])

if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
