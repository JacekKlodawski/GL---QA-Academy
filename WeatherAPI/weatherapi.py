import requests
import json
import xml.etree.ElementTree as et
import xmltodict
from bs4 import BeautifulSoup
import html5lib


def is_xml(value):
    try:
        et.fromstring(value)
    except et.ParseError:
        return False
    return True


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True



key = '4a646e6cf8b06de0d731287d1da6b670'
lat = 51.509865
lon = -0.118092


#req = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric')
# print(req.status_code)
#
#
# data = req.text
# parse_json = json.loads(data)
# print(parse_json)


response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&mode=html&lang=pl&units=standard')
soup = BeautifulSoup(response.content, 'html.parser')
soup_string = str(soup)
soup_string = soup_string
print(soup_string.lower().startswith("<!doctype html>"))
print(soup_string)

