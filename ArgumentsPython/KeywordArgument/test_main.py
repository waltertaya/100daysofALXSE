#!/usr/bin/env  python3
''' Keyword Arguments
Unpacking dictionary to form keyword arguments
'''
import json
from unittest.mock import patch
from unittest import TestCase
import unittest
from main import dict_to_json, json_to_dict, function_with_kwargs


class TestMain(TestCase):
    def test_dict_to_json(self):
        data = {'name': 'John', 'age': 25}
        filename = 'my_dict.json'
        with patch('main.json.dump') as mock_json_dump:
            dict_to_json(data, filename)
            mock_json_dump.assert_called_once_with(data, mock_json_dump)

    def test_json_to_dict(self):
        filename = 'my_dict.json'
        with patch('main.json.load') as mock_json_load:
            json_to_dict(filename)
            mock_json_load.assert_called_once_with(mock_json_load)

    def test_function_with_kwargs(self):
        data = {'name': 'John', 'age': 30}
        with patch('main.function_with_kwargs') as mock_function_with_kwargs:
            function_with_kwargs(**data)
            mock_function_with_kwargs.assert_called_once_with(**data)

if __name__ == '__main__':
    unittest.main()
