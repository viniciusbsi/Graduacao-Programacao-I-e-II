from unittest import TestCase


class TestConta_palavras(TestCase):
    def test_conta_palavras(self):
        self.assertEqual(conta_palavras('a'), {'a':1})
