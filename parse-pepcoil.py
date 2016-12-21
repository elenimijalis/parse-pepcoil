#!/usr/bin/env python
import sys
import argparse
import itertools

def parse_pepcoil(data):
    groups = []
    buff = []
    for key, group in itertools.groupby(data, lambda line: line.startswith('PEPCOIL of')):
        if key:
            if len(buff):
                groups.append(buff)
            buff = []
            buff += list(group)
        else:
            buff += list(group)
    groups.append(buff)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='outputs pepcoil data in tabular format')
    parser.add_argument('pepcoil_data', type=argparse.FileType("r"), help='pepcoil file')
    args = parser.parse_args()
    parse_pepcoil(args.pepcoil_data)
