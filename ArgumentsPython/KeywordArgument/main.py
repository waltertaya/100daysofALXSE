#!/usr/bin/env  python3
''' Positional Arguments
Unpacking list to form positional arguments
'''
import json


def dict_to_json(my_dict, filename, **Kwargs):
    print(f'Kwargs: {Kwargs}')
    json_txt = json.dumps(my_dict, **Kwargs)
    with open(filename, 'w') as f:
        f.write(json_txt)


if __name__ == '__main__':
    my_dict = {'name': 'John', 'age': 25}
    options = {'indent': 4, 'sort_keys': True}
    dict_to_json(my_dict, 'my_dict.json', **options)
    print('File my_dict.json created successfully')
