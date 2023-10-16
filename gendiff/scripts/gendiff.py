#!/usr/bin/env/python3
import argparse
import json
from gendiff.engine import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Compares\
    two configuration files and shows a difference.')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    parser.add_argument(
            '-f',
            '--format',
            help='set format of output')
    args = parser.parse_args()
    file1 = json.load(open(args.first_file))
    file2 = json.load(open(args.second_file))
    print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
