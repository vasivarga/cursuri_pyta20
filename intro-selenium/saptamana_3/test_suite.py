import unittest

from HtmlTestRunner import HTMLTestRunner

from saptamana_2.curs_unittest.unittest_exercitii import LoginTests
from saptamana_3.alerts import TestAlerts
from saptamana_3.explicit_wait import ExplicitWaitDemo
from saptamana_3.keys import TestKeys


class TestSuite(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys))

        teste_de_rulat.addTests(
            [
                unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
                unittest.defaultTestLoader.loadTestsFromTestCase(ExplicitWaitDemo),
                unittest.defaultTestLoader.loadTestsFromTestCase(LoginTests),
            ]
        )

        # Se instaleaza libraria html-testRunner
        runner = HTMLTestRunner(
            report_name="Nume raport",
            combine_reports=True,
            report_title="Titlu raport"
        )

        runner.run(teste_de_rulat)
