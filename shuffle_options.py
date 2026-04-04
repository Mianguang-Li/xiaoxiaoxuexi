# -*- coding: utf-8 -*-
import random
import re

def shuffle_options(content):
    # 匹配题目格式: ["题目", ["选项A", "选项B", "选项C", "选项D"], "正确答案"]
    pattern = r'\["([^"]+)",\s*\["([^"]+)",\s*"([^"]+)",\s*"([^"]+)",\s*"([^"]+)"\],\s*"([^"]+)"\]'
    
    def replace(match):
        question = match.group(1)
        options = [match.group(2), match.group(3), match.group(4), match.group(5)]
        correct = match.group(6)
        
        # 打乱选项顺序
        paired = list(enumerate(options))
        random.shuffle(paired)
        new_indices, new_options = zip(*paired)
        
        # 正确答案不变（只是选项位置变了）
        new_correct = correct
        
        return f'["{question}", ["{new_options[0]}", "{new_options[1]}", "{new_options[2]}", "{new_options[3]}"], "{new_correct}"]'
    
    return re.sub(pattern, replace, content)

# 处理一二年级题库
files = ['grade1_chinese_bank.dart', 'grade1_math_bank.dart', 'grade1_english_bank.dart',
         'grade2_chinese_bank.dart', 'grade2_math_bank.dart', 'grade2_english_bank.dart']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = shuffle_options(content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f'{f} 处理完成')

print('所有题库选项已打乱')
