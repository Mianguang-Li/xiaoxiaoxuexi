# -*- coding: utf-8 -*-
import subprocess

r = subprocess.run(['git', 'show', 'HEAD:lib/grade1_english_bank.dart'], capture_output=True)
content = r.stdout.decode('utf-8', errors='replace')

# Find the outer list declaration
const_idx = content.find('const List')
print(f'const at: {const_idx}')
print(f'Content: {repr(content[const_idx:const_idx+80])}')
print()

# Find first [
first_bracket = content.find('[', const_idx)
print(f'First [ after const: {first_bracket}')
print(f'Content: {repr(content[first_bracket:first_bracket+100])}')
print()

# Count how many top-level commas in the outer list content
# This tells us how many parts the outer list has
outer_start = first_bracket
# Find matching ]
depth = 0
j = outer_start
in_str = False
esc = False
qc = None
for j in range(outer_start, len(content)):
    c = content[j]
    if esc:
        esc = False
        continue
    if c == '\\':
        esc = True
        continue
    if in_str:
        if c == qc:
            in_str = False
        continue
    if c in ('"', "'"):
        in_str = True
        qc = c
        continue
    if c == '[':
        depth += 1
        continue
    if c == ']':
        depth -= 1
        if depth == 0:
            break

outer_end = j + 1
outer_arr = content[outer_start:outer_end]
inner = outer_arr[1:-1].strip()
print(f'Outer list: {outer_start} to {outer_end}, length={outer_end-outer_start}')
print(f'Inner (first 200 chars): {repr(inner[:200])}')

# Count commas at depth 0
comma_count = 0
depth = 0
in_str = False
esc = False
qc = None
for k, c in enumerate(inner):
    if esc:
        esc = False
        continue
    if c == '\\':
        esc = True
        continue
    if in_str:
        if c == qc:
            in_str = False
        continue
    if c in ('"', "'"):
        in_str = True
        qc = c
        continue
    if c == '[':
        depth += 1
        continue
    if c == ']':
        depth -= 1
        continue
    if c == ',' and depth == 0:
        comma_count += 1

print(f'Top-level commas: {comma_count}')
print(f'Top-level parts: {comma_count + 1}')
