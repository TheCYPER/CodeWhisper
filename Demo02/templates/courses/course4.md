### 4. 条件判断（If/Else） - 程序的红绿灯

**比喻**：像交通信号灯，根据条件决定执行哪条路

#### 基础结构

```python
# 温度判断
temperature = 28

if temperature > 30:
    print("开启空调")
elif 25 <= temperature <= 30:  # 25到30度之间
    print("开风扇")
else:
    print("自然通风")

# 简化嵌套
age = 18
is_local = True
if age >= 18 and is_local:
    print("允许参加")
```

#### 常见错误

```python
# 错误：遗漏冒号
if temperature > 30  # 缺少冒号！
    print("太热了")

# 错误：错误缩进
if x > 5:
    print("大于5")  # 需要缩进！
```