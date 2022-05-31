
#!/usr/bin/python3
""" deserializing """
import json
from 5-save_to_json_file import save_to_json_file as jsave
from 6-load_from_json_file.py import load_from_json_file as jload
import sys

def load_from_json_file(...):
    """ load JSON representation from filename """

    with open(filename, 'w', encoding="utf-8") as f:
        for arg in sys.argv[1:]:
            f.write(json.dumps(arg))
