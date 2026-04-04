# -*- coding: utf-8 -*-
snippet = '  ["Q1", ["A","B","C","D"], "A"],\n  ["Q2", ["X","Y","Z","W"], "Y"],\n];'
print('Original:')
print(repr(snippet))
print()

import re, random

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

def parse_question_array(s):
    s = s.strip()
    if not (s.startswith('[') and s.endswith(']')):
        return None
    inner = s[1:-1].strip()
    if not inner:
        return None
    parts = split_top_level(inner)
    if len(parts) != 3:
        return None
    q, opts_str, ans = parts[0].strip(), parts[1].strip(), parts[2].strip().rstrip(',').strip()
    if not ((q.startswith('"') and q.endswith('"')) or (q.startswith("'") and q.endswith("'"))):
        return None
    if not (opts_str.startswith('[') and opts_str.endswith(']')):
        return None
    opts_inner = opts_str[1:-1].strip()
    opts = split_top_level(opts_inner)
    if len(opts) != 4:
        return None
    return (q, [o.strip() for o in opts], ans)

content = snippet
i = 0
positions = []
while i < len(content):
    start = content.find('[', i)
    if start == -1:
        break
    depth = 0
    j = start
    in_string = False
    escape_next = False
    quote_char = None
    while j < len(content):
        c = content[j]
        if escape_next:
            escape_next = False
            j += 1
            continue
        if c == '\\':
            escape_next = True
            j += 1
            continue
        if in_string:
            if c == quote_char:
                in_string = False
            j += 1
            continue
        if c in ('"', "'"):
            in_string = True
            quote_char = c
            j += 1
            continue
        if c == '[':
            depth += 1
            j += 1
            continue
        if c == ']':
            depth -= 1
            j += 1
            if depth == 0:
                break
            continue
        j += 1
    arr_str = content[start:j]
    parsed = parse_question_array(arr_str)
    if parsed is not None:
        positions.append((start, j, parsed))
        i = j
    else:
        i = start + 1

print('Found questions:')
for idx2, (s, e, data) in enumerate(positions):
    q, opts, ans = data
    after_close = content[e:]
    m = re.match(r'\s*', after_close)
    ws = m.group(0)
    first = after_close[len(ws):] if len(ws) < len(after_close) else ''
    print(f'  Q{idx2}: start={s}, end={e}')
    print(f'    arr={repr(arr_str)}')
    print(f'    after_close={repr(after_close[:20])}, ws={repr(ws)}, first_non_ws={repr(first[:10])}')

# Now simulate replacement
def strip_quotes(s):
    s = s.strip()
    if len(s) >= 2 and ((s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'"))):
        return s[1:-1]
    return s

def make_new_line(question, opts, answer_str, target_pos):
    answer_val = strip_quotes(answer_str)
    answer_idx = next((i for i, o in enumerate(opts) if strip_quotes(o) == answer_val), 0)
    new_opts = list(opts)
    if answer_idx != target_pos:
        val = new_opts[answer_idx]
        if answer_idx < target_pos:
            for k in range(answer_idx, target_pos):
                new_opts[k] = new_opts[k + 1]
        else:
            for k in range(answer_idx, target_pos, -1):
                new_opts[k] = new_opts[k - 1]
        new_opts[target_pos] = val
    others = [i for i in range(4) if i != target_pos]
    vals = [new_opts[i] for i in others]
    random.shuffle(vals)
    for k, v in zip(others, vals):
        new_opts[k] = v
    opts_repr = '[' + ', '.join(new_opts) + ']'
    return '  [' + question + ', ' + opts_repr + ', ' + answer_str + ']'

new_content = content
offset = 0
for idx2, (start, end, data) in enumerate(positions):
    q, opts, ans = data
    target_pos = idx2 % 4
    after_close = content[end:]
    m = re.match(r'\s*', after_close)
    ws = m.group(0)
    first = after_close[len(ws):] if len(ws) < len(after_close) else ''
    
    new_opts_line = make_new_line(q, opts, ans, target_pos)
    
    if first.startswith(','):
        comma_idx = len(ws)
        span_end = end + comma_idx + 1
        trailing_in_span = after_close[:comma_idx + 1]
        replace_with = new_opts_line + trailing_in_span
    else:
        span_end = end
        replace_with = new_opts_line
    
    adj_start = start + offset
    adj_end = span_end + offset
    new_content = new_content[:adj_start] + replace_with + new_content[adj_end:]
    offset += len(replace_with) - (span_end - start)
    print(f'\nQ{idx2}: replace [{start}:{end}] with {repr(new_opts_line)}')
    print(f'  span_end={span_end}, after={repr(after_close[:10])}')
    print(f'  first_non_ws={repr(first[:5])}, comma_idx={len(ws)}, trailing_in_span={repr(trailing_in_span if first.startswith(",") else "N/A")}')

print('\nFinal:')
print(repr(new_content))
