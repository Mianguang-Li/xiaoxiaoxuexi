# -*- coding: utf-8 -*-
import subprocess, os
os.chdir(r'E:\workspace\xiaoxiao_study')
result = subprocess.run(['git', 'show', 'HEAD:lib/grade3_math_bank.dart'], capture_output=True)
if result.returncode == 0:
    content = result.stdout.decode('utf-8')
    lines = content.split('\n')
    print('Original lines 3-8:')
    for i, l in enumerate(lines[3:8]):
        print(f'  {i+3}: {repr(l)}')
    print()
    # Find first question
    idx = content.find('"')
    print('First question area:', repr(content[idx-3:idx+100]))
