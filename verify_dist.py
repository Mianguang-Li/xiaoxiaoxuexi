# -*- coding: utf-8 -*-
"""Verify answer position distribution in processed Dart question bank files."""
import os

def split_top_level(s):
    result = []
    depth = 0
    in_string = False
    escape_next = False
    current = []
    i = 0
    while i < len(s):
        c = s[i]
        if escape_next:
            escape_next = False
            current.append(c)
            i += 1
            continue
        if c == '\\':
            escape_next = True
            current.append(c)
            i += 1
            continue
        if in_string:
            if c == '"':
                in_string = False
            current.append(c)
            i += 1
            continue
        if c == '"':
            in_string = True
            current.append(c)
            i += 1
            continue
        if c == '[':
            depth += 1
            current.append(c)
            i += 1
            continue
        if c == ']':
            depth -= 1
            current.append(c)
            i += 1
            continue
        if c == ',' and depth == 0:
            result.append(''.join(current))
            current = []
            i += 1
            continue
        current.append(c)
        i += 1
    if current:
        result.append(''.join(current))
    return result

def get_answer_positions(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    positions = []
    i = 0
    n = len(content)
    
    while i < n:
        c = content[i]
        if c == '"':
            j = i + 1
            while j < n:
                ch = content[j]
                if ch == '\\':
                    j += 2
                    continue
                if ch == '"':
                    break
                j += 1
            i = j + 1
            continue
        if c == '[':
            depth = 0
            j = i
            in_str = False
            esc = False
            while j < n:
                ch = content[j]
                if esc:
                    esc = False
                    j += 1
                    continue
                if ch == '\\':
                    esc = True
                    j += 1
                    continue
                if in_str:
                    if ch == '"':
                        in_str = False
                    j += 1
                    continue
                if ch == '"':
                    in_str = True
                    j += 1
                    continue
                if ch == '[':
                    depth += 1
                    j += 1
                    continue
                if ch == ']':
                    depth -= 1
                    j += 1
                    if depth == 0:
                        break
                    continue
                j += 1
            
            arr = content[i:j]
            inner = arr[1:-1].strip()
            parts = split_top_level(inner)
            if len(parts) == 3:
                opts_str = parts[1].strip()
                if opts_str.startswith('[') and opts_str.endswith(']'):
                    opts_inner = opts_str[1:-1].strip()
                    opts = split_top_level(opts_inner)
                    if len(opts) == 4:
                        ans = parts[2].strip().rstrip(',').strip()
                        # Strip double quotes from answer
                        if ans.startswith('"') and ans.endswith('"'):
                            ans_val = ans[1:-1]
                        else:
                            ans_val = ans
                        # Find answer position
                        for idx_opt, opt in enumerate(opts):
                            opt_s = opt.strip()
                            if opt_s.startswith('"') and opt_s.endswith('"'):
                                if opt_s[1:-1] == ans_val:
                                    positions.append(idx_opt)
                                    break
                        else:
                            positions.append(-1)  # not found
            i = j
            continue
        i += 1
    
    return positions

files = [
    'lib/grade1_chinese_bank.dart',
    'lib/grade1_english_bank.dart',
    'lib/grade2_chinese_bank.dart',
    'lib/grade2_math_bank.dart',
    'lib/grade3_chinese_bank.dart',
    'lib/grade3_math_bank.dart',
    'lib/grade3_english_bank.dart',
]

os.chdir(r'E:\workspace\xiaoxiao_study')
all_ok = True
for fp in files:
    positions = get_answer_positions(fp)
    total = len(positions)
    dist = {0: 0, 1: 0, 2: 0, 3: 0}
    for p in positions:
        if 0 <= p <= 3:
            dist[p] += 1
    not_found = sum(1 for p in positions if p < 0)
    
    print(f'{fp}: {total} questions')
    if total > 0:
        print(f'  A={dist[0]} ({dist[0]*100//total}%), B={dist[1]} ({dist[1]*100//total}%), '
              f'C={dist[2]} ({dist[2]*100//total}%), D={dist[3]} ({dist[3]*100//total}%)')
    if not_found:
        print(f'  WARNING: {not_found} answers not found in options!')
        all_ok = False
    # Check if distribution is reasonably even (each >= 20%)
    if total > 0:
        for pos in range(4):
            pct = dist[pos] * 100 // total
            if pct < 20:
                print(f'  WARNING: Position {pos} is below 20% ({pct}%)')
                all_ok = False

if all_ok:
    print('\nAll files verified OK!')
else:
    print('\nSome issues found!')
