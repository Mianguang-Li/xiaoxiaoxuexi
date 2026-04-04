# -*- coding: utf-8 -*-
"""
Shuffle answer options so correct answers are evenly distributed across A/B/C/D.
Round-robin: question[i] → answer at position (i % 4).
A=0, B=1, C=2, D=3.
Handles: comments inside list body, single quotes in strings, outer list wrapper.
"""
import random

# ── low-level parsers ──────────────────────────────────────────────────────────

def split_top_level(s):
    """Split by top-level commas, respecting double-quoted strings and brackets."""
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

def strip_comments(s):
    """Remove // and /* */ comments from s. Preserves newlines."""
    result = []
    i = 0
    n = len(s)
    while i < n:
        if i < n - 1 and s[i] == '/' and s[i + 1] == '/':
            while i < n and s[i] != '\n':
                i += 1
            continue
        if i < n - 1 and s[i] == '/' and s[i + 1] == '*':
            j = i + 2
            while j < n - 1:
                if s[j] == '*' and s[j + 1] == '/':
                    i = j + 2
                    break
                j += 1
            else:
                i = j
            continue
        result.append(s[i])
        i += 1
    return ''.join(result)

def parse_question(cand):
    """Parse ["q", ["o1","o2","o3","o4"], "ans"] → (q_str, [opts], ans_str) or None."""
    # Strip comments first (they appear in some files' list bodies)
    clean = strip_comments(cand).strip()
    if not clean:
        return None
    if not (clean.startswith('[') and clean.endswith(']')):
        return None
    inner = clean[1:-1].strip()
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
        os = o.strip()
        if not (os.startswith('"') and os.endswith('"')):
            return None
    return (q, [o.strip() for o in opts], ans)

def strip_dq(s):
    """Strip outer double-quotes from s."""
    s = s.strip()
    if len(s) >= 2 and s.startswith('"') and s.endswith('"'):
        return s[1:-1]
    return s

def shuffle_opts(opts, ans_str, target_pos):
    """Move answer to target_pos, randomize the other 3."""
    ans_val = strip_dq(ans_str)
    answer_idx = next(
        (i for i, o in enumerate(opts) if strip_dq(o) == ans_val), 0
    )
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
    return new_opts

# ── outer list boundary finder ────────────────────────────────────────────────

def find_outer_list(content):
    """Find outer list boundaries: (list_start, list_end_excl).
    Scans for first '=' not in a string, then first '[' after it,
    then matching ']'.
    """
    n = len(content)
    i = 0
    eq_idx = -1
    while i < n:
        c = content[i]
        if c == '"':
            j = i + 1
            while j < n and content[j] not in ('"', '\\'):
                j += 1
            if j < n and content[j] == '\\':
                j += 1  # skip escaped char
            i = j + 1
            continue
        if c == '=':
            eq_idx = i
            break
        i += 1
    if eq_idx == -1:
        return (-1, -1)
    list_start = content.find('[', eq_idx)
    if list_start == -1:
        return (-1, -1)
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
    return (list_start, j)

# ── main file processor ──────────────────────────────────────────────────────

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    list_start, list_end = find_outer_list(content)
    if list_start == -1:
        print(f"  ERROR: Could not find outer list")
        return

    # list_start = position of '['
    # list_end   = position just AFTER ']'
    list_body_start = list_start + 1   # char after '['
    list_body_end   = list_end          # exclusive, same as overall list_end

    # Extract body of outer list
    list_body = content[list_body_start:list_body_end]
    raw_candidates = split_top_level(list_body)

    # Parse each candidate + capture its trailing whitespace/comma
    questions = []
    body_pos = 0
    for raw in raw_candidates:
        # Trailing separator: comma + whitespace (not part of split)
        trail_start = body_pos + len(raw)
        trail_end = trail_start
        while trail_end < len(list_body) and list_body[trail_end] in (',', ' ', '\t', '\n', '\r'):
            trail_end += 1
        trailing = list_body[trail_start:trail_end]

        parsed = parse_question(raw)
        if parsed is not None:
            abs_start = list_body_start + body_pos
            abs_end   = abs_start + len(raw)
            questions.append((abs_start, abs_end, raw, parsed, trailing))
        body_pos = trail_end

    total = len(questions)
    if total == 0:
        print("  WARNING: No questions found!")
        return

    dist = {0: 0, 1: 0, 2: 0, 3: 0}

    # Rebuild content
    parts = []
    prev_end = list_body_start

    for idx, (abs_start, abs_end, raw, parsed, trailing) in enumerate(questions):
        q_str, opts, ans_str = parsed
        target_pos = idx % 4

        # Anything between previous item and this one
        parts.append(content[prev_end:abs_start])

        # New shuffled question (no trailing comma yet)
        new_opts = shuffle_opts(opts, ans_str, target_pos)
        opts_repr = '[' + ', '.join(new_opts) + ']'
        new_q_line = '[' + q_str + ', ' + opts_repr + ', ' + ans_str + ']'

        parts.append(new_q_line)
        parts.append(trailing)  # comma + newline + indent
        dist[target_pos] += 1
        prev_end = abs_end

    # Close: whatever remains in list_body from prev_end to end
    parts.append(content[list_body_start + (prev_end - list_body_start):])
    new_content = ''.join(parts)

    print(f"  Found {total} questions")
    print(f"  Distribution: A={dist[0]} ({dist[0]*100//total}%), "
          f"B={dist[1]} ({dist[1]*100//total}%), "
          f"C={dist[2]} ({dist[2]*100//total}%), "
          f"D={dist[3]} ({dist[3]*100//total}%)")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("  Written successfully")

def main():
    files = [
        r"E:\workspace\xiaoxiao_study\lib\grade1_chinese_bank.dart",
        r"E:\workspace\xiaoxiao_study\lib\grade1_english_bank.dart",
        r"E:\workspace\xiaoxiao_study\lib\grade2_chinese_bank.dart",
        r"E:\workspace\xiaoxiao_study\lib\grade2_math_bank.dart",
        r"E:\workspace\xiaoxiao_study\lib\grade3_chinese_bank.dart",
        r"E:\workspace\xiaoxiao_study\lib\grade3_math_bank.dart",
        r"E:\workspace\xiaoxiao_study\lib\grade3_english_bank.dart",
    ]
    for fp in files:
        print(f"\nProcessing: {fp}")
        try:
            process_file(fp)
        except Exception:
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    main()
