#!/usr/bin/env/python3
import argparse
from gendiff.parser import parse_file
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
    data1 = parse_file(args.first_file.name)
    data2 = parse_file(args.second_file.name)
    print(generate_diff(data1, data2))


if __name__ == '__main__':
    main()
