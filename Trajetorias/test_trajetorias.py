import unittest
from trajetorias import *
import datetime as dt

class Test_TempoDecorridoTests(unittest.TestCase):
    def test_tempo_decorrido_recebe_1_tempo_retorna_0(self):
        intervalo = [dt.datetime(2014, 5, 27, 14, 3, 0), ]
        self.assertEqual(determina_tempo_decorrido(intervalo), 0)

    def test_tempo_decorrido_0_segundo(self):
        t1 = dt.datetime(2014, 5, 27, 14, 3, 0)
        t2 = dt.datetime(2014, 5, 27, 14, 3, 0)
        intervalo = [t1, t2]
        self.assertEqual(determina_tempo_decorrido(intervalo), 0)

    def test_tempo_decorrido_1_segundo(self):
        t1 = dt.datetime(2014, 5, 27, 14, 3, 0)
        t2 = dt.datetime(2014, 5, 27, 14, 3, 1)
        intervalo = [t1, t2]
        self.assertEqual(determina_tempo_decorrido(intervalo), 1)

    def test_tempo_decorrido_1_minuto(self):
        t1 = dt.datetime(2014, 5, 27, 14, 3, 0)
        t2 = dt.datetime(2014, 5, 27, 14, 4, 0)
        intervalo = [t1, t2]
        self.assertEqual(determina_tempo_decorrido(intervalo), 60)

    def test_tempo_decorrido_1_hora(self):
        t1 = dt.datetime(2014, 5, 27, 14, 3, 0)
        t2 = dt.datetime(2014, 5, 27, 15, 3, 0)
        intervalo = [t1, t2]
        self.assertEqual(determina_tempo_decorrido(intervalo), 3600)

    def test_tempo_decorrido_1_dia(self):
        t1 = dt.datetime(2014, 5, 27, 14, 3, 0)
        t2 = dt.datetime(2014, 5, 28, 14, 3, 0)
        intervalo = [t1, t2]
        self.assertEqual(determina_tempo_decorrido(intervalo), 86400)

    def test_tempo_decorrido_1_mes_maio_junho(self):
        t1 = dt.datetime(2014, 5, 27, 14, 3, 0)
        t2 = dt.datetime(2014, 6, 27, 14, 3, 0)
        intervalo = [t1, t2]
        self.assertEqual(determina_tempo_decorrido(intervalo), 2678400)

    def test_tempo_decorrido_1_mes_janeiro_fevereiro(self):
        t1 = dt.datetime(2014, 1, 1, 0, 0, 0)
        t2 = dt.datetime(2014, 2, 1, 0, 0, 0)
        intervalo = [t1, t2]
        self.assertEqual(determina_tempo_decorrido(intervalo), 2678400)

    def test_tempo_decorrido_1_mes_fevereiro_marco(self):
        t1 = dt.datetime(2014, 2, 1, 0, 0, 0)
        t2 = dt.datetime(2014, 3, 1, 0, 0, 0)
        intervalo = [t1, t2]
        self.assertEqual(determina_tempo_decorrido(intervalo), 2419200)

    def test_tempo_decorrido_1_ano(self):
        t1 = dt.datetime(2014, 1, 1, 0, 0, 0)
        t2 = dt.datetime(2015, 1, 1, 0, 0, 0)
        intervalo = [t1, t2]
        self.assertEqual(determina_tempo_decorrido(intervalo), 31536000)

    def test_tempo_decorrido_1_segundo_tempos_invertidos(self):
        t1 = dt.datetime(2014, 5, 27, 14, 3, 1)
        t2 = dt.datetime(2014, 5, 27, 14, 3, 0)
        intervalo = [t1, t2]
        self.assertEqual(determina_tempo_decorrido(intervalo), 1)

    def test_tempo_decorrido_2_segundos_3_tempos(self):
        t1 = dt.datetime(2014, 5, 27, 14, 3, 1)
        t2 = dt.datetime(2014, 5, 27, 14, 3, 2)
        t3 = dt.datetime(2014, 5, 27, 14, 3, 0)
        intervalo = [t1, t2, t3]
        self.assertEqual(determina_tempo_decorrido(intervalo), 2)

    def test_tempo_decorrido_com_4_tempos_desordenados(self):
        t1 = dt.datetime(2014, 5, 27, 14, 3, 2)
        t2 = dt.datetime(2014, 5, 27, 14, 3, 1)
        t3 = dt.datetime(2014, 5, 27, 14, 3, 4)
        t4 = dt.datetime(2014, 5, 27, 14, 3, 3)
        intervalo = [t1, t2, t3, t4]
        self.assertEqual(determina_tempo_decorrido(intervalo), 3)


class Test_AgrupaPontosPorIDdeTrajetoria(unittest.TestCase):
    def test_agrupa_pontos_por_id_de_trajetoria_1_ponto(self):
     pontos = [(801, '23.793360', '38.021434', dt.date(2002, 9, 14), dt.time(9, 19, 33))]
     trajetorias = {801: [('23.793360', '38.021434', dt.datetime(2002, 9, 14, 9, 19, 33)), ]}
     self.assertEqual(agrupa_pontos_por_id_de_trajetoria(pontos), trajetorias)

    def test_agrupa_pontos_por_id_de_trajetoria_2_pontos_mesmo_id(self):
     ponto1 = (801, '23.793360', '38.021434', dt.date(2002, 9, 14), dt.time(9, 19, 33))
     ponto2 = (801, '23.790908', '38.023185', dt.date(2002, 9, 14), dt.time(9, 20, 3))
     pontos = [ponto1, ponto2]
     trajetorias = {801: [('23.793360', '38.021434', dt.datetime(2002, 9, 14, 9, 19, 33)),
                          ('23.790908', '38.023185', dt.datetime(2002, 9, 14, 9, 20, 3))]}
     self.assertEqual(agrupa_pontos_por_id_de_trajetoria(pontos), trajetorias)

    def test_agrupa_pontos_por_id_de_trajetoria_3_pontos_mesmo_id(self):
     ponto1 = (801, '23.793360', '38.021434', dt.date(2002, 9, 14), dt.time(9, 19, 33))
     ponto2 = (801, '23.790908', '38.023185', dt.date(2002, 9, 14), dt.time(9, 20, 3))
     ponto3 = (801, '23.790910', '38.025678', dt.date(2002, 9, 14), dt.time(9, 21, 43))
     pontos = [ponto1, ponto2, ponto3]
     trajetorias = {801: [('23.793360', '38.021434', dt.datetime(2002, 9, 14, 9, 19, 33)),
                          ('23.790908', '38.023185', dt.datetime(2002, 9, 14, 9, 20, 3)),
                          ('23.790910', '38.025678', dt.datetime(2002, 9, 14, 9, 21, 43))]}
     self.assertEqual(agrupa_pontos_por_id_de_trajetoria(pontos), trajetorias)

    def test_agrupa_pontos_por_id_de_trajetoria_2_pontos_ids_diferentes(self):
     ponto1 = (801, '23.793360', '38.021434', dt.date(2002, 9, 14), dt.time(9, 19, 33))
     ponto2 = (802, '23.790908', '38.023185', dt.date(2002, 9, 14), dt.time(9, 20, 3))
     pontos = [ponto1, ponto2]
     trajetorias = {801: [('23.793360', '38.021434', dt.datetime(2002, 9, 14, 9, 19, 33))],
                    802: [('23.790908', '38.023185', dt.datetime(2002, 9, 14, 9, 20, 3))]}
     self.assertEqual(agrupa_pontos_por_id_de_trajetoria(pontos), trajetorias)


    def test_agrupa_pontos_por_id_de_trajetoria_2_pontos_de_2_ids_diferentes(self):
     ponto11 = (801, '23.793360', '38.021434', dt.date(2002, 9, 14), dt.time(9, 19, 33))
     ponto12 = (801, '23.790908', '38.023185', dt.date(2002, 9, 14), dt.time(9, 20, 3))
     ponto21 = (802, '23.793360', '38.021434', dt.date(2002, 9, 14), dt.time(9, 19, 33))
     ponto22 = (802, '23.790908', '38.023185', dt.date(2002, 9, 14), dt.time(9, 20, 3))
     pontos = [ponto11, ponto12, ponto21, ponto22]
     trajetorias = {801: [('23.793360', '38.021434', dt.datetime(2002, 9, 14, 9, 19, 33)),
                          ('23.790908', '38.023185', dt.datetime(2002, 9, 14, 9, 20, 3))],
                    802: [('23.793360', '38.021434', dt.datetime(2002, 9, 14, 9, 19, 33)),
                          ('23.790908', '38.023185', dt.datetime(2002, 9, 14, 9, 20, 3))]}
     self.assertEqual(agrupa_pontos_por_id_de_trajetoria(pontos), trajetorias)


class Test_DeterminaTempoDecorridoTrajetorias(unittest.TestCase):
    def test_determina_tempo_decorrido_1_trajetoria_1_ponto(self):
        trajetorias = {801: [('23.793360', '38.021434', dt.datetime(2002, 9, 14, 9, 19, 33)), ]}
        tempos_trajetorias = {801: 0}
        self.assertEqual(determina_tempo_decorrido_trajetorias(trajetorias), tempos_trajetorias)

    def test_determina_tempo_decorrido_1_trajetoria_2_pontos(self):
        trajetorias = {801: [('23.793360', '38.021434', dt.datetime(2002, 9, 14, 9, 19, 1)),
                             ('23.790908', '38.023185', dt.datetime(2002, 9, 14, 9, 19, 2))]}
        tempos_trajetorias = {801: 1}
        self.assertEqual(determina_tempo_decorrido_trajetorias(trajetorias), tempos_trajetorias)

    def test_determina_tempo_decorrido_1_trajetoria_3_pontos(self):
        trajetorias = {801: [('23.793360', '38.021434', dt.datetime(2002, 9, 14, 9, 19, 1)),
                             ('23.790908', '38.023185', dt.datetime(2002, 9, 14, 9, 19, 2)),
                             ('23.790908', '38.023185', dt.datetime(2002, 9, 14, 9, 19, 3))]}
        tempos_trajetorias = {801: 2}
        self.assertEqual(determina_tempo_decorrido_trajetorias(trajetorias), tempos_trajetorias)

    def test_determina_tempo_decorrido_1_trajetoria_3_pontos_desordenados(self):
        trajetorias = {801: [('23.793360', '38.021434', dt.datetime(2002, 9, 14, 9, 19, 1)),
                             ('23.790908', '38.023185', dt.datetime(2002, 9, 14, 9, 19, 3)),
                             ('23.790908', '38.023185', dt.datetime(2002, 9, 14, 9, 19, 2))]}
        tempos_trajetorias = {801: 2}
        self.assertEqual(determina_tempo_decorrido_trajetorias(trajetorias), tempos_trajetorias)

    def test_determina_tempo_decorrido_2_trajetoria_3_pontos(self):
        trajetorias = {801: [('23.793360', '38.021434', dt.datetime(2002, 9, 14, 9, 19, 1)),
                             ('23.790908', '38.023185', dt.datetime(2002, 9, 14, 9, 19, 2)),
                             ('23.790908', '38.023185', dt.datetime(2002, 9, 14, 9, 19, 3))],
                       802: [('23.793360', '38.021434', dt.datetime(2002, 9, 14, 9, 19, 1)),
                             ('23.790908', '38.023185', dt.datetime(2002, 9, 14, 9, 19, 15)),
                             ('23.790908', '38.023185', dt.datetime(2002, 9, 14, 9, 19, 10))]}
        tempos_trajetorias = {801: 2, 802: 14}
        self.assertEqual(determina_tempo_decorrido_trajetorias(trajetorias), tempos_trajetorias)

if __name__ == '__main__':
    unittest.main()
