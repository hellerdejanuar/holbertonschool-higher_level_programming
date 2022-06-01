#!/usr/bin/python3
""" deserializing """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'
args_list = sys.argv[1:]

try:
    json_file_list = load_from_json_file(filename)
except FileNotFoundError:
    save_to_json_file(args_list, 'add_item.json')

else:
    json_file_list += args_list
    save_to_json_file(json_file_list, 'add_item.json')
        
