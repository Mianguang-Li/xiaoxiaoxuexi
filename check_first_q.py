# -*- coding: utf-8 -*-
import subprocess
r = subprocess.run(['git', 'show', 'HEAD:lib/grade2_chinese_bank.dart'], capture_output=True)
content = r.stdout.decode('utf-8', errors='replace')
# Find first double-quote
idx = content.index(chr(34))
print('First question area:', repr(content[idx-5:idx+120]))
print()
# Check how split_top_level splits the list body
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

eq_idx = content.find('=')
list_start = content.find('[', eq_idx)
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
print(f'Candidates 0-5:')
for i, c in enumerate(candidates[:6]):
    print(f'  {i}: {repr(c[:80])}')
