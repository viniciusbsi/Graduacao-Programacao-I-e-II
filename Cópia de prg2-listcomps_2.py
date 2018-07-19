#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Resolva os exercícios tentando usar compreensão de lista onde possível.
# Crie os testes para cada função

from itertools import groupby

def nomes_com_menos_de_4_letras(lista):
    '''1. Use uma listcomp para gerar uma lista de homens com nomes de 4 ou menos letras.'''
    s = [nome for nome in lista if len(nome) <= 4]
    return(s)

def lista_de_nomes_e_inicial(lista):
    '''
    2. Use uma listcomp para gerar uma lista de duplas (também conhecida em 
    computação como uma lista associativa) formada pela letra inicial e o nome 
    de cada homem. Por exemplo, a resposta para a lista mulheres seria:

    [('M', 'Mariana'), ('A', 'Ana'), ('P', 'Paula')]
    '''
    s = [(nome[0], nome)for nome in lista]
    return(s)

def iniciais_e_nomes_incompleto(lista):
    '''3. Gere um dicionário associando iniciais aos nomes de homens. 
    Quantos itens terá o dicionário assim produzido?'''
    s = [(nome[0], nome) for nome in lista]
    return({ini:nome for (ini, nome) in s})

def iniciais_e_nomes_completo(lista):
    '''3b. Gere um dicionário associando iniciais aos nomes de homens. 
    A chave deve ser a inicial e o valor deve conter uma lista de nomes 
    com a inicial
    '''
    s = [(nome[0], nome) for nome in lista]
    return({ini:[nome] for ini, nome in s})

def mulher_homem(mulher,homem):
    '''4. Use a função zip para gerar uma lista associativa, e com ela carregar 
    um dicionário associando cada mulher a um homem. Quantos itens terá o 
    dicionário assim produzido?'''
    s = [(x[0],x[1]) for x in zip(mulher, homem)]
    return({mulher:homem for mulher,homem in s})
	
    
def produto_cartesiano(homens,mulheres):
    '''5. Gere uma lista associativa para organizar uma aula de dança na qual 
    todos devem dançar com todos. Quantos casais serão formados?
    Dica: o nome da operação a ser feita neste exercício é produto cartesiano, 
    e para fazer isso em uma listcomp ou genexp você precisa usar mais de um 
    for dentro da expressão.'''
    s = [(homem, mulher) for homem in homens for mulher in mulheres]
    return(s)

def produto_cartesiano_filtro(homens,mulheres):
    '''6. Repita o exercício 5, acrescentando um filtro com if para remover os 
    nomes com menos de 4 letras das duas listas. Quantos casais serão formados?'''
    s = [x for x in produto_cartesiano(homens,mulheres) if len(x[0])>= 4 and len(x[1])>= 4]
    return(s)
   
# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0 

def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido == esperado:
        acertos += 1
        print ('+ Obtido: %s' % (repr(obtido)))
    else:
        print ('- Esperado: %s \tObtido: %s' % (repr(esperado), 
        repr(obtido)))

def main():
    print('')
    mulheres = ['Mariana', 'Ana', 'Paula']
    homens = ['Pedro', 'Juca', 'Tom', 'Joaquim']
    
    print('\n1.Nomes com 4 ou menos letras:')
    test(nomes_com_menos_de_4_letras(homens), ['Juca', 'Tom'])
    test(nomes_com_menos_de_4_letras(mulheres), ['Ana'])
    
    print('\n2. Inicial e Nome:')
    test(lista_de_nomes_e_inicial(mulheres), [('M', 'Mariana'), ('A', 'Ana'), ('P', 'Paula')])
    test(lista_de_nomes_e_inicial(homens), [('P', 'Pedro'), ('J', 'Juca'), ('T', 'Tom'), ('J', 'Joaquim')])

    print('\n3. Iniciais e nomes (incompleto):')
    test(iniciais_e_nomes_incompleto(mulheres), {'M': 'Mariana', 'P': 'Paula', 'A': 'Ana'})
    test(iniciais_e_nomes_incompleto(homens), {'P': 'Pedro', 'J': 'Joaquim', 'T': 'Tom'})

    print('\n3b. Iniciais e nomes (completo):')
    test(iniciais_e_nomes_completo(mulheres), {'P': ['Paula'], 'M': ['Mariana'], 'A': ['Ana']})
    test(iniciais_e_nomes_completo(homens), {'P': ['Pedro'], 'J': ['Joaquim','Juca'], 'T': ['Tom']})
    homens2 = ['Pedro', 'Juca', 'Tom', 'Joaquim', 'Andre', 'Marco', 'Gabriel', 'Juarez']
    resultado = {'T': ['Tom'], 'J': ['Joaquim', 'Juarez', 'Juca'], 'M': ['Marco'], 'A': ['Andre'], 'P': ['Pedro'], 'G': ['Gabriel']}
    test(iniciais_e_nomes_completo(homens2), resultado)

    print('\n4. Mulher com homem:')
    test(mulher_homem(mulheres,homens), {'Paula': 'Tom', 'Ana': 'Juca', 'Mariana': 'Pedro'})

    print('\n5. Produto Cartesiano')
    test(produto_cartesiano(homens,mulheres), [('Pedro', 'Mariana'), ('Pedro', 'Ana'), ('Pedro', 'Paula'), ('Juca', 'Mariana'), ('Juca', 'Ana'), ('Juca', 'Paula'), ('Tom', 'Mariana'), ('Tom', 'Ana'), ('Tom', 'Paula'), ('Joaquim', 'Mariana'), ('Joaquim', 'Ana'), ('Joaquim', 'Paula')])

    print('\n6. Produto Cartesiano com filtro (4 ou mais letras no nome):')
    test(produto_cartesiano_filtro(homens,mulheres), [('Pedro', 'Mariana'), ('Pedro', 'Paula'), ('Juca', 'Mariana'), ('Juca', 'Paula'), ('Joaquim', 'Mariana'), ('Joaquim', 'Paula')])

if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
