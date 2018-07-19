#!/usr/bin/env python3
#coding: utf-8

'''
Faça um programa que verifique se o cardápio do IFC Araquari, disponivel
na sua página, está atualizado.
Para isso, acesse a página online diretamente através do seu programa, 
pegue a informação do período de vigência de cardápio e compare com a data
atual. Informe se o cardápio está atualizado ou a quantos dias ele está 
desatualizado.

Dicas:
- O endereço do cardápio é: http://araquari.ifc.edu.br/car
- Utilize o módulo urrlib.request para a leitura da página
-- Use como base os exemplos dos slides sobre a Starbuzz Café.
- Para executar operações com datas, utilize o módulo datetime.
-- Você pode fazer comparação de datas e verificar dias decorridos entre 
    duas datas, entre outras operações.
-- Também é possível fazer a conversão de uma string que contenha uma 
    data.
'''

import urllib.request
import webbrowser
import datetime
import smtplib

url = "http://araquari.ifc.edu.br/cardapio/"
pagina = urllib.request.urlopen(url)
texto  = pagina.read().decode("utf8")
string_inicio = 'http://araquari.ifc.edu.br/wp-content/uploads/2014/02/10-a-16.10.2016.pdf'
inicio = texto.find(string_inicio) + len(string_inicio) + 2
string_fim = '2016'
fim = texto.find(string_fim, inicio) + len(string_fim)
periodo = texto[inicio:fim]
periodo = periodo.split('-')
dia_inicio = periodo[0]
dia_fim = periodo[2]
mes = periodo[3]
if dia_fim > dia_inicio:
    print('Cardápio Atualizado')
    print('Período de validade do calendário: %s a %s/%s/2016' %(dia_inicio, dia_fim, mes))
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()

    smtp.login('ifc.vinicius@gmail.com', 'GMpassw02')

    de = 'ifc.vinicius@gmail.com'
    para = ['marcoandre@ifc-araquari.edu.br']
    msg = """From: %s
    To: %s
    Subject: Cardapio atualizado

    O cardario do refeitorio esta atualizado.""" % (de, ', '.join(para))

    smtp.sendmail(de, para, msg)

    smtp.quit()
#webbrowser.open(url)