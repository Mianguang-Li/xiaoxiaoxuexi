# -*- coding: utf-8 -*-
import subprocess

files = [
    'lib/grade1_chinese_bank.dart',
    'lib/grade1_english_bank.dart',
    'lib/grade2_math_bank.dart',
    'lib/grade3_math_bank.dart',
    'lib/grade3_english_bank.dart',
]

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f'{fp}: {len(lines)} lines')
    for i, l in enumerate(lines):
        if l.strip().startswith('["'):
            print(f'  First Q line {i}: {repr(l[:70])}')
            break
    for i in range(len(lines)-1, -1, -1):
        if lines[i].strip().startswith('["'):
            print(f'  Last  Q line {i}: {repr(lines[i][:70])}')
            break
    print()
