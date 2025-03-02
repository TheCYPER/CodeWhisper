# 使用Flask + Jinja2模板实现基础界面
from flask import Flask, render_template_string, request
import ai_part

app = Flask(__name__)

# 极简代码编辑器界面（纯HTML+少量CSS）
EDITOR_HTML = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .container { display: flex; }
        #editor { width: 60%; height: 500px; padding: 10px; }
        #ai-panel { width: 35%; margin-left: 20px; padding: 10px; border: 1px solid #ccc; }
    </style>
</head>
<body>
    <div class="container">
        <textarea id="editor" placeholder="输入你的代码...">{{ code }}</textarea>
        <div id="ai-panel">
            <h3>AI助手反馈：</h3>
            <p>{{ ai_response }}</p>
        </div>
    </div>
    <form method="POST">
        <input type="hidden" name="code" id="code-input">
        <button type="submit">获取AI帮助</button>
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def editor():
    if request.method == 'POST':
        code = request.form['code']
        # 调用Ollama接口获取AI反馈
        ai_response = ai_part.get_ai_feedback(code)
        return render_template_string(EDITOR_HTML, code=code, ai_response=ai_response)
    return render_template_string(EDITOR_HTML, code="", ai_response="等待输入...")

if __name__ == "__main__":
    app.run(
      host='0.0.0.0',
      port= 3000,
      debug=True
    )
