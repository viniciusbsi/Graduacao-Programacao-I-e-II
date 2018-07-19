#!/bin/env python3
# coding: utf-8   
# Marco André <marcoandre@gmail.com>
# Lista de exercícios 0b

#Entregar por e-mail para marcoandre@ifc-araquari.edu.br 
#com o assunto: prg2: lista0b. 
#Envie um arquivo zip com o nome no formato seu_nome.zip.

#1. Crie uma função que leia um endereço IP no formato a.b.c.d e retorne 
# se ele é ou não um IP válido.

#2. Faça um programa que leia um arquivo contendo uma lista de endereços 
#IP no formato a.b.c.d e gere um arquivo com os IPs válidos e outro com 
#os IPs inválidos.

#3. Faça um programa que leia os três arquivos com os IPs e crie uma 
#página HTML básica, contendo a lista completa desses IPs, 
#e depois a lista dos válidos e inválidos.

#4. Faça um programa que leia o arquivo alice.txt 
#(ou outro arquivo semelhante à sua escolha) 
#e mostre as dez palavras que aparecem com mais frequência no texto.

import string
from operator import itemgetter
def carrega_arquivo():
    entrada = open("chapeuzinho_vermelho.txt","r")
    texto = entrada.read()
    entrada.close()
    return texto

def criar_dicionario(texto):
    final = {}
    palavras = texto.split(' ')
    for palavra in palavras:
        nova_palavra = ''
        palavra = palavra.lower()
        if len(palavra) > 1:
            for letra in palavra:
                if (letra not in string.punctuation) and (letra != '"') and (letra != '—'):
                    nova_palavra += letra
            final[nova_palavra] = final.get(nova_palavra, 0) + 1
    return(final)

def conta_palavras(dicionario):
    dicionario_ordenado = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
    i = 0
    for chave in dicionario_ordenado:
        if i < 10:
            print("%dº Palavra: %s; Apareceu: %s vezes" %(i+1,dicionario_ordenado[i][0],dicionario_ordenado[i][1]))
            i +=1
    
texto = carrega_arquivo()
dicionario = criar_dicionario(texto)
contagem = conta_palavras(dicionario)