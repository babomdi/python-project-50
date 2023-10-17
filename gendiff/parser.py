import json
import yaml
import os


def parse_file(file_path):
    _, file_name = os.path.split(file_path)
    _, file_format = file_name.split('.')
    with open(file_path) as f:
        if file_format == 'json':
            return json.load(f)
        return yaml.safe_load(f)
