### 10. 项目二：简易库存管理系统

**功能需求**：

1. 商品信息存储（名称、价格、库存）
2. 入库/出库操作
3. 数据持久化保存

#### 类设计

```python  
class Product:  
    def __init__(self, name, price, stock):  
        self.name = name  
        self.price = price  
        self.stock = stock  

class Inventory:  
    def __init__(self):  
        self.products = []  

    def add_product(self, product):  
        self.products.append(product)  

    def save_to_file(self, filename):  
        with open(filename, 'w') as f:  
            for p in self.products:  
                f.write(f"{p.name},{p.price},{p.stock}\n")  

# 使用示例  
inventory = Inventory()  
inventory.add_product(Product("鼠标", 99.9, 50))  
inventory.save_to_file("data.csv")  
```  

#### 文件操作示例

```python  
# 读取CSV文件  
import csv  

def load_inventory(filename):  
    inventory = Inventory()  
    with open(filename) as f:  
        reader = csv.reader(f)  
        for row in reader:  
            name, price, stock = row  
            inventory.add_product(Product(name, float(price), int(stock)))  
    return inventory  
```  
