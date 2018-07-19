from unittest import TestCase
from leet import leet

class TestLeet(TestCase):
    def test_leet_sem_leet(self):
        self.assertEqual(leet(''),'')
        self.assertEqual(leet('j'),'j')

    def testa_leet_1_caracter_minusculo(self):
        self.assertEqual(leet('a'), '4')
        self.assertEqual(leet('o'), '0')
        self.assertEqual(leet('e'), '3')
        self.assertEqual(leet('e'), '3')
        self.assertEqual(leet('g'), '9')
        self.assertEqual(leet('i'), '1')
        self.assertEqual(leet('s'), '5')
        self.assertEqual(leet('t'), '7')

    def testa_leet_1_caracter_maiusculo(self):
        self.assertEqual(leet('E'), '3')
        self.assertEqual(leet('A'), '4')

    def testa_leet_2_caracter_minusculo(self):
        self.assertEqual(leet('aj'), '4j')
        self.assertEqual(leet('is'), '15')

    def testa_leet_2_caracter_maiusculo(self):
        self.assertEqual(leet('AJ'), '4J')
        self.assertEqual(leet('IS'), '15')
        self.assertEqual(leet('The Cure'), '7h3 Cur3')
        self.assertEqual(leet('fisl2013'), 'f15l2013')
        self.assertEqual(leet('Eu te amo'), '3u 73 4m0')
