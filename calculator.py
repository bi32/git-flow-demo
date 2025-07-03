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