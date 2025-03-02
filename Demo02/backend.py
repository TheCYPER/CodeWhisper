# 使用Flask + Jinja2模板实现基础界面
from flask import Flask, request, render_template

import ai_part

app = Flask(__name__)

# 课程数据
'''
1. Input/Output
2. Variables
3. Operators 
4. If/Else
5. Loop
6. Function
7. OOP
8. 简单排序算法
9. Project 1
10. Project 2
'''

COURSE_PAGES = {
    1: {"title": "Input/Output"},
    2: {"title": "Variables"},
    3: {"title": "Operators"},
    4: {"title": "If/Else"},
    5: {"title": "Loop"},
    6: {"title": "Functions"},
    7: {"title": "OOP"},
    8: {"title": "Sort"},
    9: {"title": "Project1"},
    10: {"title": "Peoject2"}
}


# 在原有代码基础上修改以下部分

@app.route('/')
def index():
    # 传递完整课程数据给目录页
    return render_template('index.html', COURSE_PAGES=COURSE_PAGES)

@app.route('/templates/index.html')
def index2():
    # 传递完整课程数据给目录页
    return render_template('index.html', COURSE_PAGES=COURSE_PAGES)


@app.route('/course/<int:course_id>', methods=['GET', 'POST'])
def show_course(course_id):
    if request.method == 'POST':
        code = request.form['code']  # 获取提交的代码
        ai_response = ai_part.get_ai_feedback(code)
        return render_template('course_page.html',
                             code=code,  # 保持代码内容
                             ai_response=ai_response,
                             course_content=f"courses/course{course_id}.html",
                             course_title=COURSE_PAGES[course_id]["title"])

    # 处理GET请求
    if course_id not in COURSE_PAGES:
        return "Course not found", 404

    return render_template('course_page.html',
                           code="print(\"hello world\")",
                           ai_response="等待输入",
                           course_content=f"courses/course{course_id}.html",
                           course_title=COURSE_PAGES[course_id]["title"])

# @app.route('/page/<int:page_id>')
# def show_page(page_id):
#     page_data = COURSE_PAGES.get(page_id, {"title": "课程未找到"})
#     return render_template('course_page.html',  # 需要创建新模板
#                          page_data=page_data,
#                          current_page=page_id)

# @app.route('/course')
# def course_page():
#     # 读取course1.md的内容
#     with open(os.path.join(COURSES_DIR, 'course1.md'), 'r', encoding='utf-8') as file:
#         markdown_content = file.read()
#     # markdown_content.replace("`", "")
#     return render_template('course_page.html', markdown_content=markdown_content)


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=3000,
        debug=True
    )
