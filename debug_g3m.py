# -*- coding: utf-8 -*-
with open(r'E:\workspace\xiaoxiao_study\lib\grade3_math_bank.dart', 'r', encoding='utf-8') as f:
    content = f.read()

def split_top_level(s):
    result = []
    depth = 0
    in_string = False
    escape_next = False
    quote_char = None
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
            if c == quote_char:
                in_string = False
            current.append(c)
            i += 1
            continue
        if c in ('"', "'"):
            in_string = True
            quote_char = c
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

i = 0
n = len(content)
count = 0
while i < n and count < 3:
    c = content[i]
    if c in ('"', "'"):
        quote_char = c
        j = i + 1
        while j < n:
            ch = content[j]
            if ch == '\\':
                j += 2
                continue
            if ch == quote_char:
                break
            j += 1
        i = j + 1
        continue
    if c == '[':
        depth = 0
        j = i
        in_str = False
        esc = False
        qc = None
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
                if ch == qc:
                    in_str = False
                j += 1
                continue
            if ch in ('"', "'"):
                in_str = True
                qc = ch
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
        arr_str = content[i:j]
        inner = arr_str[1:-1].strip()
        parts = split_top_level(inner)
        print(f'Question {count}: i={i}, j={j}, parts={len(parts)}')
        if len(parts) == 3:
            print(f'  inner={repr(inner[:100])}')
            print(f'  parts={repr(parts)}')
        else:
            print(f'  inner={repr(inner[:150])}')
            print(f'  parts={repr(parts)}')
        count += 1
        i = j
        continue
    i += 1
