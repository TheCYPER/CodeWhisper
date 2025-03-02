### 6. 函数（Functions） - 代码工具箱

**比喻**：函数就像厨房工具（比如榨汁机），输入原料 → 处理 → 输出成品

#### 基础语法

```python  
# 定义计算圆面积的函数  
def calculate_area(radius):  
    """计算圆面积"""  
    pi = 3.14159  
    return pi * radius ** 2  

# 调用函数  
print(f"半径为3的圆面积：{calculate_area(3):.2f}")  
```  

#### 参数类型演示

```python  
# 默认参数  
def greet(name, greeting="你好"):  
    print(f"{greeting}, {name}!")  

greet("小明")                  # 输出：你好, 小明!  
greet("Alice", "Hello")       # 输出：Hello, Alice!  

# 可变参数  
def sum_numbers(*nums):  
    return sum(nums)  

print(sum_numbers(1, 2, 3))  # 输出6  
```  

#### 常见错误

```python  
# 错误1：修改外部变量  
count = 0  
def increment():  
    count += 1  # 报错！需使用global声明  

# 错误2：缺少return语句  
def add(a, b):  
    result = a + b  # 没有return  
print(add(2,3))     # 输出None  
```  