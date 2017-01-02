#!/usr/bin/env python
import sys
import csv
import argparse
import itertools

def parse_pepcoil(data, names):
    ls_names = []
    for name in names:
        if len(name.strip()):
            ls_names.append(name.strip()[:-4])

    csvreader = csv.reader(data, delimiter=',', quotechar='"')
    count = 0
    with open('out-u.csv', 'wb') as out:
        writer = csv.writer(out)
        for i, row in enumerate(csvreader):
            if i == 0:
                continue
            if row[0] in ls_names:
                writer.writerow(row)
                count += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='filters pepcoil data for unique names in name list')
    parser.add_argument('pepcoil_data', type=argparse.FileType("r"), help='pepcoil data')
    parser.add_argument('names', type=argparse.FileType("r"), help='unique names')
    args = parser.parse_args()
    parse_pepcoil(args.pepcoil_data, args.names)
