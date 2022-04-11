import unittest
from data.datesnew import dates

class TestDate(unittest.TestCase):

    def test_case_1_1(self):
        self.assertEqual(dates(["2016"]), True)

    def test_case_1_2(self):
        self.assertEqual(dates(["2015"]), False)

    def test_case_1_3(self):
        self.assertEqual(dates(["2000"]), True)

    def test_case_1_4(self):
        self.assertEqual(dates(["1900"]), False)


    def test_case_2_1(self):
        self.assertEqual(dates(["1", "2022"]), 31)

    def test_case_2_2(self):
        self.assertEqual(dates(["4", "2022"]), 30)

    def test_case_2_3(self):
        self.assertEqual(dates(["2", "2022"]), 28)

    def test_case_2_4(self):
        self.assertEqual(dates(["2", "2020"]), 29)


    def test_case_3_1(self):
        self.assertEqual(dates(["1", "4", "2022"]), "piątek")

    def test_case_3_2(self):
        self.assertEqual(dates(["2", "4", "2022"]), "sobota")

    def test_case_3_3(self):
        self.assertEqual(dates(["3", "4", "2022"]), "niedziela")

    def test_case_3_4(self):
        self.assertEqual(dates(["4", "4", "2022"]), "poniedziałek")

    def test_case_3_5(self):
        self.assertEqual(dates(["5", "4", "2022"]), "wtorek")

    def test_case_3_6(self):
        self.assertEqual(dates(["6", "4", "2022"]), "środa")

    def test_case_3_7(self):
        self.assertEqual(dates(["7", "4", "2022"]), "czwartek")
