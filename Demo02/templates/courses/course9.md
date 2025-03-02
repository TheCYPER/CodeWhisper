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
