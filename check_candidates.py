# -*- coding: utf-8 -*-
import subprocess

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

def parse_question(cand):
    cand = cand.strip()
    if not (cand.startswith('[') and cand.endswith(']')):
        return None
    inner = cand[1:-1].strip()
    if not inner:
        return None
    parts = split_top_level(inner)
    if len(parts) != 3:
        return None
    q, opts_str, ans = parts[0].strip(), parts[1].strip(), parts[2].strip().rstrip(',').strip()
    if not (q.startswith('"') and q.endswith('"')):
        return None
    if not (opts_str.startswith('[') and opts_str.endswith(']')):
        return None
    opts_inner = opts_str[1:-1].strip()
    opts = split_top_level(opts_inner)
    if len(opts) != 4:
        return None
    for o in opts:
        if not (o.strip().startswith('"') and o.strip().endswith('"')):
            return None
    return (q, [o.strip() for o in opts], ans)

def analyze_file(filename):
    r = subprocess.run(['git', 'show', 'HEAD:' + filename], capture_output=True)
    content = r.stdout.decode('utf-8', errors='replace')
    
    eq_idx = content.find('=')
    if eq_idx == -1:
        print(f'{filename}: No "=" found')
        return
    
    list_start = content.find('[', eq_idx)
    if list_start == -1:
        print(f'{filename}: No "[" after "=" found')
        return
    
    n = len(content)
    depth = 0
    j = list_start
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
    
    list_body = content[list_start+1:j]
    candidates = split_top_level(list_body)
    
    parsed_ok = 0
    failed = []
    for i, cand in enumerate(candidates):
        result = parse_question(cand)
        if result is not None:
            parsed_ok += 1
        else:
            failed.append((i, cand[:100]))
    
    print(f'{filename}: {len(candidates)} candidates, {parsed_ok} parsed OK, {len(failed)} failed')
    for idx, f in failed[:5]:
        print(f'  Failed[{idx}]: {repr(f[1])}')

files = [
    'lib/grade2_chinese_bank.dart',
    'lib/grade1_chinese_bank.dart',
    'lib/grade1_english_bank.dart',
]

for fp in files:
    analyze_file(fp)
