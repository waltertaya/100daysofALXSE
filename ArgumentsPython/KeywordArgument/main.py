#!/usr/bin/env  python3
''' Positional Arguments
Unpacking list to form positional arguments
'''
import json


def dict_to_json(my_dict, filename, **kwargs):
    print(f'Kwargs: {kwargs}')
    json_txt = json.dumps(my_dict, **kwargs)
    with open(filename, 'w') as f:
        f.write(json_txt)

def json_to_dict(filename):
    with open (filename, 'r') as f:
        my_dict = json.load(f)
    return my_dict

def function_with_kwargs(**kwargs):
    print(f'Kwargs: {kwargs}')
    for key, value in kwargs.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    my_dict = {'name': 'John', 'age': 25}
    options = {'indent': 4, 'sort_keys': True}
    dict_to_json(my_dict, 'my_dict.json', **options)
    print('File my_dict.json created successfully')
    my_dict = json_to_dict('my_dict.json')
    print(my_dict)

    function_with_kwargs(name='John', age=25)
