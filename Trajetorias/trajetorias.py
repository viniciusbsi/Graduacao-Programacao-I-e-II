# /usr/bin/env python3
import datetime as dt


def determina_tempo_decorrido(tempos):
    """Recebe uma lista de momentos de tempo e devolve o tempo decorrido entre eles."""
    ordenado = sorted(tempos)
    return int((ordenado[-1] - ordenado[0]).total_seconds())


def agrupa_pontos_por_id_de_trajetoria(pontos):
    tupla = ()
    dici = {}
    for ponto in pontos:
        lista = []
        lista_com_tuplas = []
        lista.append(ponto[1])
        lista.append(ponto[2])
        lista.append(dt.datetime.combine(ponto[3], ponto[4]))
        tupla = tuple(lista)
        lista_com_tuplas.append(tupla)
        if ponto[0] in dici:
            dici[ponto[0]] += lista_com_tuplas
        dici[ponto[0]] = dici.get(ponto[0], lista_com_tuplas)
    return(dici)


def determina_tempo_decorrido_trajetorias(trajetorias):
    dici = {}
    for ponto in trajetorias:
        tupla = trajetorias[ponto]
        lista_com_datas = []
        for ponto_tupla in tupla:
            lista_com_datas.append(ponto_tupla[2])
        tempo = determina_tempo_decorrido(lista_com_datas)
        if ponto in dici:
            dici[ponto] += tempo
        dici[ponto] = dici.get(ponto, tempo)
    return(dici)


def main():
    pass


if __name__ == '__main__':
    main()
