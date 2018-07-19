def leet(texto):
    troca = {'a': '4', 'e': '3', 'g': '9', 'i': '1', 's': '5', 't': '7', 'o': '0'}
    texto_leet = ''
    for caracter in texto:
        texto_leet += troca.get(caracter.lower(), caracter)
    return (texto_leet)