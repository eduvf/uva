#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')

args = parser.parse_args()

with open(args.file, 'r') as f:
    code = False
    
    for line in f:
        if line.startswith('```'):
            code = not code
        elif code:
            print(line.rstrip())