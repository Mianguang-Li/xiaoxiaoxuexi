# -*- coding: utf-8 -*-
import subprocess

r = subprocess.run(['git', 'show', 'HEAD:lib/grade1_english_bank.dart'], capture_output=True)
content = r.stdout.decode('utf-8', errors='replace')

# Print the first 100 chars of content
print('First 100 chars:')
for i, c in enumerate(content[:100]):
    print(f'  {i}: {repr(c)} ord={ord(c)}')
print()

# Find where first [ appears
idx = content.find('[')
print(f'First [ at: {idx}')
if idx >= 0:
    print(f'Context: {repr(content[max(0,idx-30):idx+50])}')
