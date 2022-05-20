import unittest
import requests
import json
from weatherapi import is_xml, is_json
import xml.etree.ElementTree as et
import xml
import xmltodict
from bs4 import BeautifulSoup
from langdetect import detect


url = 'https://api.openweathermap.org/data/2.5/weather?'


class TestWeatherApi(unittest.TestCase):

    def test_1(self):
        parameters = {"lat": 51.509865, "lon": -0.118092, "appid": "4a646e6cf8b06de0d731287d1da6b670"}
        test_req = requests.get(url, parameters)
        parse_json = json.loads(test_req.text)
        self.assertEqual(is_json(test_req.text), True)
        self.assertEqual(test_req.status_code, 200)
        self.assertEqual(detect(json.loads(test_req.text)["weather"][0]['description']), 'en')
        self.assertTrue(parse_json['main']['temp'] > 200)

    def test_2(self):
        parameters = {"lat": 53, "lon": 14, "appid": ""}
        test_req = requests.get(url, parameters)
        self.assertEqual(test_req.status_code, 401)
        self.assertEqual(test_req.reason, 'Unauthorized')

    def test_3(self):
        parameters = {"lat": 51.509865, "lon": -0.118092,
                      "appid": "4a646e6cf8b06de0d731287d1da6b670",
                      "units": "metric", "lang": "pl"}
        test_req = requests.get(url, parameters)
        parse_json = json.loads(test_req.text)
        self.assertEqual(is_json(test_req.text), True)
        self.assertEqual(test_req.status_code, 200)
        self.assertEqual(detect(json.loads(test_req.text)["weather"][0]['description']), 'pl')
        self.assertTrue(parse_json['main']['temp'] < 40)

    def test_4(self):
        parameters = {"lat": 51.509865, "lon": -0.118092,
                        "appid": "4a646e6cf8b06de0d731287d1da6b670",
                        "units": "standard"}
        test_req = requests.get(url, parameters)
        parse_json = json.loads(test_req.text)
        self.assertEqual(is_json(test_req.text), True)
        self.assertEqual(test_req.status_code, 200)
        self.assertEqual(detect(json.loads(test_req.text)["weather"][0]['description']), 'en')
        self.assertTrue(parse_json['main']['temp'] > 200)

    def test_5(self):
        parameters = {"lat": 51.509865, "lon": -0.118092,
                        "appid": "4a646e6cf8b06de0d731287d1da6b670",
                        "units": "imperial"}
        test_req = requests.get(url, parameters)
        parse_json = json.loads(test_req.text)
        self.assertEqual(is_json(test_req.text), True)
        self.assertEqual(test_req.status_code, 200)
        self.assertEqual(detect(json.loads(test_req.text)["weather"][0]['description']), 'en')
        self.assertTrue(parse_json['main']['temp'] > 35)

    def test_6(self):
        parameters = {"lat": 51.509865, "lon": -0.118092,
                        "appid": "4a646e6cf8b06de0d731287d1da6b670",
                        "mode": "xml", "lang": "pl"}
        test_req = requests.get(url, parameters)
        string_xml = test_req.content
        self.assertEqual(is_xml(string_xml), True)
        dict_data = xmltodict.parse(test_req.content)
        self.assertEqual(detect(dict_data["current"]["clouds"]['@name']), 'pl')
        self.assertEqual(dict_data["current"]["temperature"]['@unit'], 'kelvin')

    def test_7(self):
        parameters = {"lat": 51.509865, "lon": -0.118092,
                        "appid": "4a646e6cf8b06de0d731287d1da6b670",
                        "mode": "xml", "lang": "pl", "units": "metric"}
        test_req = requests.get(url, parameters)
        string_xml = test_req.content
        self.assertEqual(is_xml(string_xml), True)
        dict_data = xmltodict.parse(test_req.content)
        self.assertEqual(detect(dict_data["current"]["clouds"]['@name']), 'pl')
        self.assertEqual(dict_data["current"]["temperature"]['@unit'], 'celsius')

    def test_8(self):
        parameters = {"lat": 51.509865, "lon": -0.118092,
                        "appid": "4a646e6cf8b06de0d731287d1da6b670",
                        "mode": "html"}
        test_req = requests.get(url, parameters)
        soup = str(BeautifulSoup(test_req.content, 'html.parser'))
        self.assertEqual(soup.lower().startswith("<!doctype html>"), True)
        self.assertEqual(soup.lower().endswith("</html>"), True)
        self.assertIn("London", soup)
        self.assertIn("°C", soup)

    def test_9(self):
        parameters = {"lat": 51.509865, "lon": -0.118092,
                        "appid": "4a646e6cf8b06de0d731287d1da6b670",
                        "mode": "html", "lang": "pl", "units": "metric"}
        test_req = requests.get(url, parameters)
        soup = str(BeautifulSoup(test_req.content, 'html.parser'))
        self.assertEqual(soup.lower().startswith("<!doctype html>"), True)
        self.assertEqual(soup.lower().endswith("</html>"), True)
        self.assertIn("Londyn", soup)
        self.assertIn("°C", soup)

    def test_10(self):
        parameters = {"lat": 51.509865, "lon": -0.118092,
                        "appid": "4a646e6cf8b06de0d731287d1da6b670",
                        "mode": "html", "lang": "pl", "units": "imperial"}
        test_req = requests.get(url, parameters)
        soup = str(BeautifulSoup(test_req.content, 'html.parser'))
        self.assertEqual(soup.lower().startswith("<!doctype html>"), True)
        self.assertEqual(soup.lower().endswith("</html>"), True)
        self.assertIn("Londyn", soup)
        self.assertIn("°F", soup)

    def test_11(self):
        parameters = {"q": "London",
                      "appid": "4a646e6cf8b06de0d731287d1da6b670",
                      "units": "metric", "lang": "pl"}
        test_req = requests.get(url, parameters)
        parse_json = json.loads(test_req.text)
        self.assertEqual(is_json(test_req.text), True)
        self.assertEqual(test_req.status_code, 200)
        self.assertEqual(parse_json['name'], 'Londyn')
        self.assertTrue(parse_json['main']['temp'] < 40)

    def test_12(self):
        parameters = {"zip": "EC4Y 9BE,GB",
                      "appid": "4a646e6cf8b06de0d731287d1da6b670",
                      "units": "metric", "lang": "pl"}
        test_req = requests.get(url, parameters)
        parse_json = json.loads(test_req.text)
        self.assertEqual(is_json(test_req.text), True)
        self.assertEqual(test_req.status_code, 200)
        self.assertEqual(detect(json.loads(test_req.text)["weather"][0]['description']), 'pl')
        self.assertTrue(parse_json['main']['temp'] < 40)
