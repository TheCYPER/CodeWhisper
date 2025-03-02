import os

COURSES_DIR = os.path.join(os.path.dirname(__file__), 'courses')
with open(os.path.join(COURSES_DIR, 'course1.md'), 'r', encoding='utf-8') as file:
    markdown_content = file.read()
    print(markdown_content)  # 检查内容是否正确