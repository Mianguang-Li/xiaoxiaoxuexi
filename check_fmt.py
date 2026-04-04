# -*- coding: utf-8 -*-
import os
os.environ['PYTHONIOENCODING'] = 'utf-8'
files = [
    'lib/grade1_chinese_bank.dart',
    'lib/grade2_chinese_bank.dart',
    'lib/grade3_math_bank.dart',
    'lib/grade3_english_bank.dart',
]
for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(fp)
    print(f'  Total lines: {len(lines)}')
    count = 0
    for l in lines:
        if l.strip().startswith('["'):
            print(f'  Q start: {repr(l[:70])}')
            count += 1
            if count >= 3:
                break
    for l in reversed(lines):
        if l.strip().startswith('["'):
            print(f'  Q end:   {repr(l[:70])}')
            break
    print()
