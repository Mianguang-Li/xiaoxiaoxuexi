# -*- coding: utf-8 -*-
import re

def remove_question_numbers(content):
    # 匹配题目格式: ["数字. 题目内容", ...]
    # 去掉 "数字. " 前缀
    pattern = r'\["(\d+\.\s*)([^"]+)"'
    
    def replace(match):
        number_prefix = match.group(1)  # "1. " 或 "10. " 等
        question_content = match.group(2)  # 实际题目内容
        return f'["{question_content}"'
    
    return re.sub(pattern, replace, content)

# 处理一年级数学题库
files = ['grade1_math_bank.dart']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = remove_question_numbers(content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f'{f} 处理完成')

print('题目序号已去除')
