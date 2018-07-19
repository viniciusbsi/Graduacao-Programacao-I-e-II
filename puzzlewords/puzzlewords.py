import random

def escolhe_palavra(nivel_dificuldade):
    if nivel_dificuldade == 1:
        palavras = open('dificil.txt').readlines()
        texto = "Nível difícil, aí sim!"
    elif nivel_dificuldade == 2:
        palavras = open('medio.txt').readlines()
        texto = "Nível médio, quase lá!"
    elif nivel_dificuldade == 3:
        palavras = open('facil.txt').readlines()
        texto = "Nível fácil, chegando agora?!"
    return (random.choice(palavras).strip(), texto)

def embaralha_palavra(palavra):
    lista_palavra = list(palavra)
    random.shuffle(lista_palavra)
    return ''.join(lista_palavra)

while True:
    print("Escolha um nível de dificuldade")
    print("Difícil: 1")
    print("Médio: 2")
    print("Fácil: 3")
    nivel_dificuldade = int(input('Digite o número referente ao nível de dificuldade!:').lower())
    palavra_secreta, texto = escolhe_palavra(nivel_dificuldade)
    palavra_embaralhada = embaralha_palavra(palavra_secreta)
    print("\n%s A palavra é: %s \n"%(texto,palavra_embaralhada))
    chute = ''
    tentativas = 1
    while tentativas <= 5 and chute != palavra_secreta:
        chute = input('Tentativa %d. Boa Sorte!: '%tentativas).lower()
        if chute == palavra_secreta:
            print("\nParabéns!Você acertou a palavra: %s em %d tentativa(s). \n"%(palavra_secreta,tentativas))
        else:
            tentativas += 1
            if tentativas > 5:
                print('\nYou Lose! A palavra era: %s. \n'%palavra_secreta)
            else:
                print('Tente novamente.')

