import requests
import json
import xml.etree.ElementTree as elementTree

key = '4a646e6cf8b06de0d731287d1da6b670'
req = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat=52.92&lon=14.86&appid={key}')
print(req.status_code)


def json_parser():
    data = req.text
    parse_json = json.loads(data)
    print(parse_json)
    return parse_json


def xml_parser():
    pass


def is_JSON():
    data = json_parser()
    try:
        json.loads(data)
    except ValueError as err:
        return False
    return True

def is_Xml(data):
    try:
        elementTree.fromstring(data)
    except elementTree.ParseError:
        return False
    return True

is_JSON()