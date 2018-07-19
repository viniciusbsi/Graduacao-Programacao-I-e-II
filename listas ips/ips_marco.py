#coding: utf-8
def carrega_ips():
    entrada = open("ips.txt","r")
    ips = entrada.readlines()
    entrada.close()
    return ips
    
def ip_é_valido(ip):
    octetos = ip.split('.')
    for octeto in octetos:
        if int(octeto) > 255:
            return False
    else:
        return True

def valida_ips(ips):
    ips_validos = []
    ips_invalidos = []
    for ip in ips:
        if ip_é_valido(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)
    return ips_invalidos, ips_validos

def gera_cabecalho():
    return '''<html>
    <meta charset = 'utf-8'>
    <head>
    <title> Validação de Ips </title>
    </head>
    <body>'''

def gera_rodape():
    return '''
    </body>
    </html>
    '''

def gera_bloco(titulo,ips):
    bloco = '<h2>%s</h2>' %(titulo)
    bloco += '<ul>'
    for ip in ips:
        bloco += '<li>%s</li>' %ip
    bloco += '</ul>'
    return bloco
    
def gera_listagem(ips, ips_validos, ips_invalidos):
    texto = ''
    texto += gera_cabecalho()
    texto += gera_bloco('Listagem de IPs', ips)
    texto += gera_bloco('IPs Válidos', ips_validos)
    texto += gera_bloco('IPs Inválidos', ips_invalidos)
    texto += gera_rodape()
    
    return texto

def grava_listagem(texto):
    saida = open('lista_ips.html','w')
    saida.write(texto)
    saida.close()
    
def main():
    ips = carrega_ips()
    ips_validos, ips_invalidos = valida_ips(ips)
    texto = gera_listagem(ips, ips_validos, ips_invalidos)
    print(texto)
    grava_listagem(texto)

if __name__ == '__main__':
    main()
