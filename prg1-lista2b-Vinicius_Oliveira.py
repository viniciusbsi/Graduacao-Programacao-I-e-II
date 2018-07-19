#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@ifc-araquari.edu.br>
# Lista de exercícios 2.2
import math
from math import sqrt

def duzias(ovos):
    ''' Receba o número de ovos e devolva a quantidade de dúzias 
    correspondente. Considere sempre dúzias cheias, arredondando pra
    cima se necessário.
    '''
    duzias = ovos / 12
    duzias = math.ceil(duzias)
    return duzias
    pass

def baskara(a,b,c):
    '''Calcule as raízes de uma equação do segundo grau, na forma 
    ax2 + bx + c. A função recebe a, b e c e faz as consistências, 
    informando ao usuário nas seguintes situações:
    - Se o usuário informar o valor de A igual a zero é uma equaçao do 
    2o grau.
    - Se o delta calculado for negativo, a equação não possui raizes reais. 
    Devolva uma tupla vazia.
    - Se o delta calculado for igual a zero a equação possui apenas uma 
    raiz real. Devolva uma tupla com um único valor.
    - Se o delta for positivo, a equação possui duas raiz reais.
    Devolva uma tupla com dois elementos.
    '''
    delta = (b ** 2)-4*a*c
    
    if (a == 0):
        raiz = -c/b
        raizes = (raiz,)
        return (raizes)
        
    if (delta < 0):
        return ()
    if (delta == 0):
        x = (-b + sqrt(delta))/2*a
        return (x,)    
    x1 = (-b + sqrt(delta))/2*a
    x2 = (-b - sqrt(delta))/2*a
    return (x1,x2)

def decompor_numero(numero):
    '''
    Leia um número inteiro menor que 1000 e devolva a quantidade de 
    centenas, dezenas e unidades do mesmo.
    Obs.: não utilize operações com strings
    '''
    if (numero < 1000):
        if (numero > 99):
            centenas = numero / 100
            centenas = round(centenas)
            n_centenas = centenas * 100
            dezenas1 = (numero - n_centenas) / 10
            dezenas = math.floor(dezenas1)
            minimo = math.floor(dezenas1)
            unidades = dezenas1 - minimo
            unidades = unidades * 10 
            unidades = round(unidades)
            return (centenas,dezenas, unidades)
        
        if (numero > 9):
            dezenas1 = numero / 10
            dezenas = math.floor(dezenas1)
            minimo = math.floor(dezenas)
            unidades = dezenas1 - minimo
            unidades = unidades * 10 
            unidades = round(unidades)
            return (0,dezenas,unidades)
        
        else:
            unidades = numero / 1
            return (0,0,unidades)
    pass

def caixa_eletronico(valor):
    '''Receba a valor do saque e retorne uma lista de pares de valores, 
    correspondentes ao valor das notas e quantidades de notas.
    As notas disponíveis serão as de 1, 5, 10, 25, 50 e 100 reais. 
    O valor mínimo é de 10 reais e o máximo de 600 reais. 
    Não se preocupe com a quantidade de notas existentes na máquina.
    Procure dar sempre o número mínimo de notas, partindo das maiores
    para as menores.
    '''
    if (valor <= 600):
        n100 = n50 = n25 = n10 = n5 = n1 = 0
        notas_100 = notas_50 = notas_25 = notas_10 = notas_5 = notas_1 = 0
        final = []
        if (valor >= 100):
            notas_100 = int(valor / 100)
            valor = math.floor(valor)
            valor = valor - (notas_100 * 100)
            n100 = 100
            final.append((n100,notas_100))
                    
        if (valor >= 50):
            notas_50 = int(valor / 50)
            valor = math.floor(valor)
            valor = valor - (notas_50 * 50)
            valor = math.floor(valor)
            n50 = 50
            final.append((n50,notas_50))
            
        if (valor >= 25):
            notas_25 = int(valor / 25)
            valor = math.floor(valor)
            valor = valor - (notas_25 * 25)
            n25 = 25
            final.append((n25,notas_25))
        
        if (valor >= 10):
            notas_10 = int(valor / 10)
            valor = math.floor(valor)
            valor = valor - (notas_10 * 10)
            n10 = 10
            final.append((n10,notas_10))
            
        if (valor >= 5):
            notas_5 = int(valor / 5)
            valor = math.floor(valor)
            valor = valor - (notas_5 * 5)
            n5 = 5
            final.append((n5,notas_5))
            
        if (valor >= 1):
            notas_1 = int(valor / 1)
            valor = math.floor(valor)
            valor = valor - (notas_1 * 1)
            n1 = 1
            final.append((n1,notas_1))
        
        return final
    else:
        return []

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
    print ('%s Esperado: %s \tObtido: %s' % (prefixo, repr(esperado), 
        repr(obtido)))

def main():
    print('Dúzias:')
    test(duzias(12), 1)
    test(duzias(24), 2)
    test(duzias(11), 1)
    test(duzias(23), 2)

    print('Báskara:')
    test(baskara(1,5,4), (-1.0, -4.0))
    test(baskara(1,4,4), (-2.0,))
    test(baskara(4,4,4), ())
    test(baskara(0,4,2), (-0.5,))

    print('Decompor número:')
    test(decompor_numero(326), (3,2,6))
    test(decompor_numero(320), (3,2,0))
    test(decompor_numero(310), (3,1,0))
    test(decompor_numero(305), (3,0,5))
    test(decompor_numero(300), (3,0,0))
    test(decompor_numero(100), (1,0,0))
    test(decompor_numero(101), (1,0,1))
    test(decompor_numero(311), (3,1,1))
    test(decompor_numero(111), (1,1,1))
    test(decompor_numero(12), (0,1,2))
    test(decompor_numero(25), (0,2,5))
    test(decompor_numero(20), (0,2,0))
    test(decompor_numero(10), (0,1,0))
    test(decompor_numero(21), (0,2,1))
    test(decompor_numero(11), (0,1,1))
    test(decompor_numero(16), (0,1,6))
    test(decompor_numero(1), (0,0,1))
    test(decompor_numero(7), (0,0,7))

    print('Caixa eletrônico:')
    test(caixa_eletronico(100), [(100,1)])
    test(caixa_eletronico(200), [(100,2)])
    test(caixa_eletronico(150), [(100,1),(50,1)])
    test(caixa_eletronico(50), [(50,1)])
    test(caixa_eletronico(175), [(100,1),(50,1),(25,1)])
    test(caixa_eletronico(75), [(50,1),(25,1)])
    test(caixa_eletronico(125), [(100,1),(25,1)])
    test(caixa_eletronico(25), [(25,1)])
    test(caixa_eletronico(250), [(100,2),(50,1)])
    test(caixa_eletronico(10), [(10,1)])
    test(caixa_eletronico(20), [(10,2)])
    test(caixa_eletronico(110), [(100,1),(10,1)])
    test(caixa_eletronico(120), [(100,1),(10,2)])
    test(caixa_eletronico(60), [(50,1),(10,1)])
    test(caixa_eletronico(70), [(50,1),(10,2)])
    test(caixa_eletronico(35), [(25,1),(10,1)])
    test(caixa_eletronico(135), [(100,1),(25,1),(10,1)])
    test(caixa_eletronico(160), [(100,1),(50,1),(10,1)])
    test(caixa_eletronico(165), [(100,1),(50,1),(10,1),(5,1)])
    test(caixa_eletronico(65), [(50,1),(10,1),(5,1)])
    test(caixa_eletronico(115), [(100,1),(10,1),(5,1)])
    test(caixa_eletronico(5), [(5,1)])
    test(caixa_eletronico(6), [(5,1),(1,1)])
    test(caixa_eletronico(191), [(100,1),(50,1),(25,1),(10,1),(5,1),(1,1)])
    test(caixa_eletronico(0), [])
    test(caixa_eletronico(600), [(100,6)])
    test(caixa_eletronico(601), [])
    test(caixa_eletronico(599), [(100, 5), (50, 1), (25, 1), (10, 2), (1, 4)])
    
if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
