### 7. 面向对象（OOP） - 虚拟工厂

**比喻**：类就像汽车设计图，对象是根据图纸生产的实际汽车

#### 类与对象

```python  
class Car:  
    # 类属性  
    wheels = 4  

    def __init__(self, brand, color):  
        # 实例属性  
        self.brand = brand  
        self.color = color  

    # 方法  
    def info(self):  
        print(f"{self.color}色{self.brand}，{self.wheels}个轮子")  

# 创建对象  
my_car = Car("比亚迪", "蓝")  
my_car.info()  
```  

#### 继承示例

```python  
class ElectricCar(Car):  
    def __init__(self, brand, color, battery):  
        super().__init__(brand, color)  
        self.battery = battery  

    # 方法重写  
    def info(self):  
        print(f"{self.color}色电动{self.brand}，续航{self.battery}km")  

tesla = ElectricCar("特斯拉", "黑", 500)  
tesla.info()  
```  

#### 常见错误

```python  
# 错误1：忘记self参数  
def info():  # 正确应为 def info(self):  
    print("...")  

# 错误2：混淆类属性和实例属性  
Car.wheels = 3  # 影响所有实例  
```  
