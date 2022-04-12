import unittest
from parameterized import parameterized
from data.datesnew import dates

class TestDate(unittest.TestCase):

    @parameterized.expand([
        (["2016"], True),
        (["2015"], False),
        (["2000"], True),
        (["1900"], False),
        (["2020"], False)
    ])
    def test_dates_1(self, x, result):
        self.assertEqual(dates(x), result)

    @parameterized.expand([
        (["1", "2022"], 31),
        (["4", "2022"], 30),
        (["2", "2022"], 28),
        (["2", "2020"], 29),
        (["2", "2021"], 29)
    ])
    def test_dates_2(self, x, result):
        self.assertEqual(dates(x), result)

    @parameterized.expand([
        (["1", "4", "2022"], "piątek"),
        (["2", "4", "2022"], "sobota"),
        (["3", "4", "2022"], "niedziela"),
        (["4", "4", "2022"], "poniedziałek"),
        (["5", "4", "2022"], "wtorek"),
        (["6", "4", "2022"], "środa"),
        (["7", "4", "2022"], "czwartek"),
        (["31", "4", "2022"], "No such day"),
        (["8", "4", "2022"], "niedziela")
    ])
    def test_dates_3(self, x, result):
        self.assertEqual(dates(x), result)


