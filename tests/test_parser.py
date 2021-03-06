import unittest
import json
import pyjucontrol.parsers as parsers

class TestParser(unittest.TestCase):
    def test_parser(self):
        f = open('tests/samples/get_device_data.json')
        data = json.load(f)
        parser = parsers.Parser()
        parser.parse_get_device_data(data)
        f.close()