#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--no-newline',
    action='store_true',
    help='disable extra newline characters between code blocks')
parser.add_argument('file')

args = parser.parse_args()

with open(args.file, 'r') as f:
    code = False
    
    for line in f:
        if line.startswith('```'):
            if code and not args.no_newline:
                print()
            code = not code
        elif code:
            print(line.rstrip())