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

    num_filter = {
        '1': 'first',
        '2': 'second',
        '3': 'third'
    }

    for entry in groups:
        length = 0
        num_coils = 0
        for line in entry:

            if line.strip().startswith('PEPCOIL'):
                row['name'] = line.strip()[11:-4]
                row['class'] = line.strip()[-3:]
            if line.strip().startswith('probable'):
                num_coils += 1
                coil = line.strip()[26:].replace('(', '').replace(')', '').split()
                row[num_filter[str(num_coils)] + '_start'] = coil[0]
                row[num_filter[str(num_coils)] + '_end'] = coil[2]
                row[num_filter[str(num_coils)] + '_length'] = coil[3]
            if line.strip().startswith('Other'):
                tmp_length = int(line.strip()[22:].split()[2])
                if tmp_length > length:
                    length = tmp_length

        row['length'] = length
        row['number'] = num_coils
        sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='outputs pepcoil data in tabular format')
    parser.add_argument('pepcoil_data', type=argparse.FileType("r"), help='pepcoil file')
    args = parser.parse_args()
    parse_pepcoil(args.pepcoil_data)
