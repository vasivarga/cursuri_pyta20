import time
import unittest


class TestDemo(unittest.TestCase):

    def setUp(self):
        print("Ruleaza metoda setUp()...")
        time.sleep(1)

    def tearDown(self):
        print("Ruleaza metoda tearDown()...")
        time.sleep(1)

    def test_case_1(self):
        print("Ruleaza motoda de test TC1")
        time.sleep(1)

    def test_case_2(self):
        print("Ruleaza motoda de test TC2")
        self.metoda_auxiliara()
        time.sleep(1)

    def metoda_auxiliara(self):
        print("Se executa metoda auxiliara")

    @unittest.skip
    def test_case_3(self):
        print("Ruleaza motoda de test TC3")
        time.sleep(1)
