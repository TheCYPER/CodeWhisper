### 8. 简单排序算法 - 数据整理术

**比喻**：排序就像整理书架，冒泡法-相邻比较交换，选择法-找最小放前面

#### 冒泡排序

```python  
def bubble_sort(arr):  
    n = len(arr)  
    for i in range(n-1):  
        for j in range(n-1-i):  
            if arr[j] > arr[j+1]:  
                arr[j], arr[j+1] = arr[j+1], arr[j]  
    return arr  

print(bubble_sort([64, 34, 25, 12, 22]))  
```  

#### 选择排序

```python  
def selection_sort(arr):  
    for i in range(len(arr)):  
        min_idx = i  
        for j in range(i+1, len(arr)):  
            if arr[j] < arr[min_idx]:  
                min_idx = j  
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  
    return arr  

print(selection_sort([29, 72, 98, 13, 87]))  
```  

#### 效率对比

| 算法 | 时间复杂度 | 适合场景  |  
|----|-------|-------|  
| 冒泡 | O(n²) | 小数据集  |  
| 选择 | O(n²) | 数据交换少 |  

---

### 9. 项目一：天气数据分析系统

**功能需求**：

1. 从API获取实时天气数据
2. 分析温度变化趋势
3. 生成可视化报表

#### 关键技术点

```python  
# 使用requests获取数据  
import requests  

def get_weather(city):  
    url = f"http://api.weather.com/{city}"  
    response = requests.get(url)  
    return response.json()  # 返回JSON数据  

# 示例数据结构  
weather_data = {  
    "days": ["Mon", "Tue", "Wed"],  
    "temps": [22, 25, 19]  
}  

# 使用matplotlib绘图  
import matplotlib.pyplot as plt  

plt.plot(weather_data["days"], weather_data["temps"])  
plt.title("本周温度变化")  
plt.show()  
```  
