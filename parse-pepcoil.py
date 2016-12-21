#!/usr/bin/env python
import sys
import argparse

def parse_pepcoil(data):
    sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='outputs pepcoil data in tabular format')
    parser.add_argument('pepcoil_data', type=argparse.FileType("r"), help='pepcoil file')
    args = parser.parse_args()
    gff3_diff(args.pepcoil_data)
