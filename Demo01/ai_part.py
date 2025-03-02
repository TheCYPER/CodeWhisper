import requests


def get_ai_feedback(code):
    host = "192.168.110.65"
    port = "11434"
    url = f"http://{host}:{port}/api/chat"

    # 构造对话历史（支持多轮上下文）
    messages = [
        {
            "role": "system",
            "content": "你是一个编程教学助手，需要用比喻和分步骤的方式帮助新手理解代码"
        },
        {
            "role": "user",
            "content": f"请分析以下代码：\n{code}\n要求：1.指出错误 2.给出优化建议 3.用比喻解释关键概念"
        }
    ]

    data = {
        "model": "deepseek-r1:14b",  # 确保与ollama list中的模型名称一致
        "options": {
            "temperature": 0.3  # 教学场景建议0.3-0.7平衡稳定性与创造性
        },
        "stream": False,
        "messages": messages
    }

    try:
        response = requests.post(url, json=data, timeout=60)
        if response.status_code == 200:
            return response.json()['message']['content']  # 注意字段变化！
        else:
            return f"AI服务错误: {response.text}"
    except Exception as e:
        return f"连接失败: {str(e)}"

'''
# 在get_ai_feedback函数中增加教学逻辑
prompt = f"""
根据用户代码的教学级别（新手/中级），用{level}对应的方式解释：
1. [错误检测] 如果代码存在语法错误，指出具体行号
2. [知识卡片] 用'比喻：'开头说明核心概念（如变量比喻为储物柜）
3. [挑战任务] 生成一个与当前代码相关的小练习（如'尝试将for循环改为while循环'）
"""
'''
'''
# 在HTML中添加成就系统（纯前端实现）
<div id="achievements">
    <h4>已解锁成就：</h4>
    <p>✅ 完成第一个程序</p>
    <p>🕹️ 修复3个错误（2/3）</p>
</div>
'''
