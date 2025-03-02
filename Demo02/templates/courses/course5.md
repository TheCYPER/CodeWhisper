### 5. 循环（Loop） - 自动重复机

**比喻**：像传送带，自动重复处理同类物品

#### for循环

```python
# 遍历列表
fruits = ["苹果", "香蕉", "橘子"]
for fruit in fruits:
    print(f"今天吃{fruit}")

# 使用range
for i in range(3):     # 0,1,2
    print(f"第{i+1}次尝试")

# 循环+条件组合
numbers = [12, 35, 60]
for num in numbers:
    if num > 50:
        print(f"{num} 超标")
        break         # 提前终止
```

#### while循环

```python
# 基础用法
count = 0
while count < 5:
    print(f"倒计时：{5-count}")
    count += 1  # 必须改变条件变量！

# 避免无限循环
password = ""
while password != "123456":  # 示例用简单密码
    password = input("请输入密码：")
```

#### 常见错误

```python
# 错误：无限循环
count = 0
while count < 5:
    print(count)  # 忘记count +=1

# 错误：错误缩进
for i in range(3):
    print(i)  # 需要缩进！
```