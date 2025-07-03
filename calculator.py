"""
计算器核心模块
提供基本的数学运算功能
"""


class Calculator:
    """
    计算器类
    提供基本的数学运算方法
    """
    
    def __init__(self):
        """初始化计算器"""
        self.history = []  # 保存计算历史
        
    def add(self, a, b):
        """
        加法运算
        
        参数:
            a (float): 第一个数
            b (float): 第二个数
            
        返回:
            float: 两数之和
        """
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result
        
    def subtract(self, a, b):
        """
        减法运算
        
        参数:
            a (float): 被减数
            b (float): 减数
            
        返回:
            float: 两数之差
        """
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
        
    def multiply(self, a, b):
        """
        乘法运算
        
        参数:
            a (float): 第一个数
            b (float): 第二个数
            
        返回:
            float: 两数之积
        """
        result = a * b
        self._add_to_history(f"{a} × {b} = {result}")
        return result
        
    def divide(self, a, b):
        """
        除法运算
        
        参数:
            a (float): 被除数
            b (float): 除数
            
        返回:
            float: 两数之商
            
        异常:
            ValueError: 当除数为0时抛出
        """
        if b == 0:
            raise ValueError("错误：除数不能为0！")
        result = a / b
        self._add_to_history(f"{a} ÷ {b} = {result}")
        return result
        
    def power(self, a, n):
        """
        幂运算
        
        参数:
            a (float): 底数
            n (float): 指数
            
        返回:
            float: a的n次幂
        """
        result = a ** n
        self._add_to_history(f"{a} ^ {n} = {result}")
        return result
        
    def square_root(self, a):
        """
        平方根运算
        
        参数:
            a (float): 被开方数
            
        返回:
            float: a的平方根
            
        异常:
            ValueError: 当a为负数时抛出
        """
        if a < 0:
            raise ValueError("错误：不能对负数开平方根！")
        result = a ** 0.5
        self._add_to_history(f"√{a} = {result}")
        return result
        
    def _add_to_history(self, operation):
        """
        添加操作到历史记录
        
        参数:
            operation (str): 操作描述
        """
        self.history.append(operation)
        
    def get_history(self):
        """
        获取计算历史
        
        返回:
            list: 历史记录列表
        """
        return self.history.copy()
        
    def clear_history(self):
        """清空历史记录"""
        self.history.clear()
        
    def export_history(self, filename="history.txt"):
        """
        导出历史记录到文件
        
        参数:
            filename (str): 导出的文件名，默认为history.txt
            
        返回:
            bool: 导出成功返回True，失败返回False
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=== 计算器历史记录 ===\n")
                f.write(f"导出时间: {self._get_timestamp()}\n")
                f.write("=" * 30 + "\n\n")
                
                if not self.history:
                    f.write("暂无计算历史。\n")
                else:
                    for i, record in enumerate(self.history, 1):
                        f.write(f"{i}. {record}\n")
                        
            return True
        except Exception as e:
            print(f"导出失败: {e}")
            return False
            
    def _get_timestamp(self):
        """获取当前时间戳"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")