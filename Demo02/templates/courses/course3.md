### 3. 运算符（Operators） - 数据工具箱

**比喻**：运算符就像各种工具，锤子（+）用来连接，剪刀（/）用来分割

#### 常用运算符

```python
# 算术运算
print(10 / 3)  # 3.333... (真正除法)
print(10 // 3)  # 3 (取整除法)

# 比较运算
score = 85
print("及格" if score >= 60 else "不及格")

# 逻辑运算
has_ticket = True
has_id = False
print(has_ticket and has_id)  # False
```

#### 常见错误

```python
# 错误：混淆 = 和 ==
if count = 5:  # 应该用 ==
    print("满员")

# 错误：优先级问题
result = 10 + 20 * 2  # 50 不是60（乘法优先）
```
