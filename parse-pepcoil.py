#!/usr/bin/env python
import sys
import argparse
import itertools

def parse_pepcoil(data):
    groups = []
    buff = []
    for key, group in itertools.groupby(data, lambda line: line.startswith('PEPCOIL')):
        if key:
            if len(buff):
                groups.append(buff)
            buff = list(group)
        else:
            buff += list(group)
    groups.append(buff)

    row = {
        'name': '', 'class': '', 'length': '', 'number': '',
        'first_start': '', 'first_end': '', 'first_length': '',
        'second_start': '', 'second_end': '', 'second_length': '',
        'third_start': '', 'third_end': '', 'third_length': '',
        'overall_length': '', 'percentage': ''
    }

    for entry in groups:
        for line in entry:
            if line.strip().startswith('PEPCOIL'):
                row['name'] = line.strip()[11:-4]
                row['class'] = line.strip()[-3:]
            if line.strip().startswith('probable'):
                pass
            if line.strip().startswith('Other'):
                pass

        print row
        sys.exit()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='outputs pepcoil data in tabular format')
    parser.add_argument('pepcoil_data', type=argparse.FileType("r"), help='pepcoil file')
    args = parser.parse_args()
    parse_pepcoil(args.pepcoil_data)
