#!/usr/bin/env/python3
from gendiff.cli import parse_args
from gendiff.parser import parse_file
from gendiff.engine import generate_diff


def main():
    args = parse_args()
    data1 = parse_file(args.first_file)
    data2 = parse_file(args.second_file)
    print(generate_diff(data1, data2))


if __name__ == '__main__':
    main()
