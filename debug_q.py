# -*- coding: utf-8 -*-
import subprocess, os, random

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

def find_all_questions(content):
    questions = []
    i = 0
    n = len(content)
    while i < n:
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
            parsed = parse_question_array(arr_str)
            if parsed is not None:
                questions.append((i, j, parsed))
                i = j
            else:
                i = i + 1
            continue
        i += 1
    return questions

os.chdir(r'E:\workspace\xiaoxiao_study')
result = subprocess.run(['git', 'show', 'HEAD:lib/grade3_math_bank.dart'], capture_output=True)
if result.returncode == 0:
    content = result.stdout.decode('utf-8')
    questions = find_all_questions(content)
    print(f'Found {len(questions)} questions')
    for idx, (qs, qe, data) in enumerate(questions[:5]):
        q, opts, ans = data
        # Find newline before qs
        nl_before = content.rfind('\n', 0, qs)
        line_start = nl_before + 1 if nl_before >= 0 else 0
        indent = content[line_start:qs]
        nl_after = content.find('\n', qe)
        line_end = nl_after + 1 if nl_after != -1 else len(content)
        print(f'\nQ{idx}: qs={qs}, qe={qe}')
        print(f'  nl_before={nl_before}, line_start={line_start}, indent={repr(indent)}')
        print(f'  nl_after={nl_after}, line_end={line_end}')
        print(f'  line: {repr(content[line_start:line_end][:80])}')
        print(f'  q={repr(q[:30])}, opts={opts}, ans={repr(ans)}')
        opts_repr = '[' + ', '.join(opts) + ']'
        new_line = indent + '[' + q + ', ' + opts_repr + ', ' + ans + '],\n'
        print(f'  NEW: {repr(new_line[:100])}')
else:
    print('Git error')
