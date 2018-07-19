#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Lista de exercícios 2
import math
def media_final_aprovado_reprovado(prova1,prova2,exercicios_programacao1,
    exercicios_programacao2):
    ''' Recebe as notas das 2 provas e 2 exercícios de programação e retorna 
    se o aluno foi ou não aprovado. As provas tem peso 7 e os exercícios 
    tem peso 3. Cada parcial tem peso igual.'''
    media1 = (prova1 * 0.7) + (exercicios_programacao1 * 0.3)
    media2 = (prova2 * 0.7) + (exercicios_programacao2 * 0.3) 
    media_final = (media1 + media2) / 2
    if (media_final >= 7):
        return True
    else:
        return False
         
def excesso_peso_peixes(peso_peixes_kg, peso_limite):
    ''' Recebe o peso dos peixes pescados, e o limite legal e devolve 
    o peso em excesso, ou zero se não houver'''
    if (peso_peixes_kg > peso_limite):
        excesso = peso_peixes_kg - peso_limite
        return round(excesso, 2)
    else:
        return  0
def testa_lados(a,b,c):
    ''' Receba os três lados de um triângulo. Informe se os valores 
    podem ser um triângulo. Indique, caso os lados formem um triângulo, 
    se o mesmo é: equilátero, isósceles ou escaleno. '''
    if (a+b > c) and (b+c > a) and (a+c > b):
        if (a == b) and (b == c):
            var = "Triângulo equilátero"
            return var
        elif (a == b) or (b == c) or (c == a):
            var = "Triângulo isósceles"
            return var
        elif (a != b) or (b != c) or (c != a):
            var = "Triângulo escaleno"
            return var
    else:
        var = "Não forma um triângulo"
        return var     

def ano_bissexto(ano):
    ''' Determine se um ano é bissexto'''
    if (ano%4 == 0 and ano%100!= 0) or ano%400 == 0:
        return True
    
    else:
        return False
            
def data_valida(data):
    '''Valida data'''
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])
    bissexto = "nao"
    if (ano%4 == 0 and ano%100!= 0) or ano%400 == 0:
        bissexto = "sim"
        
    if mes < 1 or mes > 12:
        return False

    elif dia > 31 or dia < 1 or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30):
        return False

    elif (mes == 2 and bissexto != "sim" and dia > 28) or (mes == 2 and bissexto == "sim" and dia > 29):
        return False
    
    elif (ano == 0000):
        return False
    
    else:
        return True
    

def maior3(a,b,c):
    ''' Recebe tres valores, e retorna o maior dos tres'''
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    elif (c > a) and (c > b):
        return c 
    
def menor3(a,b,c):
    ''' Recebe tres valores, e retorna o menor dos tres'''
    if (a < b) and (a < c):
        return a
    elif (b < a) and (b < c):
        return b
    elif (c < a) and (c < b):
        return c 

def salario(dinheiro_horas,horas_mensais):
    ''' Recebe quanto ganha por hora e quantas horas trabalho ao mês,
    e retorna o salário líquido.
    Descontos:
    - INSS é 8% do salário bruto
    - IR é 11% do salário bruto
    - Sindicato é 5% do salário bruto'''
    salario = dinheiro_horas * horas_mensais
    inss = salario * 0.08
    ir = salario * 0.11
    sindicato = salario * 0.05
    liquido = (salario - inss - ir - sindicato)
    return liquido
def tinta(metros_pintar):
    ''' Recebe quanto metros quadrados precisa pintar, 
    e retorna a quantidade de latas de tinta a comprar.
    A cobertura da tinta é de 3 metros por litro de tinta
    Cada lata possui 18 litros de tinta'''
    litros = metros_pintar / 3
    lata = litros / 18
    lata = math.ceil(lata)
    return lata

def acrescimo_nota_bb(nota_sozinho,nota_com_ajuda):
    ''' Recebe a nota do litle brother antes de receber ajuda, e a nota
    depois que o big brother ajudou, e retorna o acrecimo que o big
     brother recebera em sua nota pela ajuda.
     O acréscimo é de 1/4 da diferença das notas, se for positivo'''
    if (nota_sozinho < nota_com_ajuda):
        acrescimo = (nota_com_ajuda - nota_sozinho)
        acrescimo = acrescimo * 0.25
        return round(acrescimo,1)
    else:
        return 0

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
    print('Média final:')
    test(media_final_aprovado_reprovado(10,10,0,0), True)
    test(media_final_aprovado_reprovado(0,0,10,10), False)
    test(media_final_aprovado_reprovado(10,10,10,10), True)
    test(media_final_aprovado_reprovado(0,0,5,0), False)

    print('Pesca em excesso:')
    test(excesso_peso_peixes(10,50),0)
    test(excesso_peso_peixes(50,50), 0)
    test(excesso_peso_peixes(50.01,50), 0.01)
    test(excesso_peso_peixes(190.99,50), 140.99)

    print('Triângulos:')
    test(testa_lados(7,1,2),'Não forma um triângulo')
    test(testa_lados(7,2,1),'Não forma um triângulo')
    test(testa_lados(1,7,2),'Não forma um triângulo')
    test(testa_lados(1,2,7),'Não forma um triângulo')
    test(testa_lados(2,1,7),'Não forma um triângulo')
    test(testa_lados(2,7,1),'Não forma um triângulo')
    test(testa_lados(2,2,2),'Triângulo equilátero')
    test(testa_lados(3,3,3),'Triângulo equilátero')
    test(testa_lados(2,3,4),'Triângulo escaleno')
    test(testa_lados(2,4,3),'Triângulo escaleno')
    test(testa_lados(3,4,2),'Triângulo escaleno')
    test(testa_lados(3,2,4),'Triângulo escaleno')
    test(testa_lados(2,3,3),'Triângulo isósceles')
    test(testa_lados(3,2,2),'Triângulo isósceles')
    test(testa_lados(3,3,2),'Triângulo isósceles')

    print('Ano bissexto:')
    test(ano_bissexto(1000),False)
    test(ano_bissexto(1200),True)
    test(ano_bissexto(1004),True)
    test(ano_bissexto(1040),True)
    test(ano_bissexto(2012),True)
    test(ano_bissexto(2014),False)

    print('Valida datas:')
    test(data_valida("01/01/2014"),True)
    test(data_valida("31/01/2014"),True)
    test(data_valida("00/00/0000"),False)
    test(data_valida("29/02/2014"),False)
    test(data_valida("29/02/2016"),True)
    test(data_valida("30/04/2014"),True)
    test(data_valida("31/04/2014"),False)
    test(data_valida("30/06/2014"),True)
    test(data_valida("31/06/2014"),False)
    test(data_valida("30/09/2014"),True)
    test(data_valida("31/09/2014"),False)
    test(data_valida("30/11/2014"),True)
    test(data_valida("31/11/2014"),False)
    test(data_valida("32/01/2014"),False)
    test(data_valida("01/01/0000"),False)
    test(data_valida("01/13/2014"),False)

    print('Maior de 3 valores:')
    test(maior3(1,2,3), 3)
    test(maior3(1.01,1.02,1.1), 1.1)
    test(maior3(0,-1,-2), 0)
    test(maior3(-100,0,100), 100)

    print('Menor de 3 valores:')
    test(menor3(1,2,3), 1)
    test(menor3(1.01,1.02,1.1), 1.01)
    test(menor3(0,-1,-2), -2)
    test(menor3(-100,0,100), -100)

    print('Salário líquido:')
    test(salario(10,80), 608)
    test(salario(100,30), 2280)
    test(salario(2.5,300), 570)
    test(salario(5,120), 456)

    print('Latas de tinta:')
    test(tinta(10), 1)
    test(tinta(100), 2)
    test(tinta(560), 11)
    test(tinta(50001), 926)

    print('Acréscimo BB:')
    test(acrescimo_nota_bb(1,10), 2.2)
    test(acrescimo_nota_bb(7,6), 0.0)
    test(acrescimo_nota_bb(0,10), 2.5)
    test(acrescimo_nota_bb(6.9,7.1), 0.0)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
