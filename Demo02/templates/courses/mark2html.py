import markdown

# 读取Markdown文件
with open("course10.md", "r", encoding="utf-8") as f:
    md_content = f.read()

# 转换为HTML
html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'codehilite'])

# 保存为HTML文件
with open("course10.html", "w", encoding="utf-8") as f:
    f.write(html_content)
