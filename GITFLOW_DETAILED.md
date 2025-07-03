# Git Flow 详细教程 - 计算器项目实战

## 目录
1. [Git Flow 标准流程图](#git-flow-标准流程图)
2. [本项目的Git Flow实践图](#本项目的git-flow实践图)
3. [详细操作步骤](#详细操作步骤)
4. [冲突解决详解](#冲突解决详解)

## Git Flow 标准流程图

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Git Flow 标准工作流程                               │
└─────────────────────────────────────────────────────────────────────────────┘

时间线 ──────────────────────────────────────────────────────────────────────►

        ┌─────────────────────────────────────────────────────────────┐
main    │ ●───────────────●─────────────────●───────────●             │ 生产分支
        │                 ↑                 ↑           ↑             │
        │                 │                 │           │             │
        │              merge            merge       merge            │
        │                 │                 │           │             │
        └─────────────────┼─────────────────┼───────────┼─────────────┘
                          │                 │           │
        ┌─────────────────┼─────────────────┼───────────┼─────────────┐
hotfix  │                 │                 │      ●────●             │ 紧急修复
        │                 │                 │     /      \            │
        └─────────────────┼─────────────────┼────────────┼────────────┘
                          │                 │             │
        ┌─────────────────┼─────────────────┼─────────────┼───────────┐
release │            ●────●            ●────●             │           │ 发布准备
        │           /      \          /      \            │           │
        └──────────────────┼────────────────┼─────────────┼───────────┘
                           │                │             │
        ┌──────────────────┼────────────────┼─────────────┼───────────┐
develop │ ●───●───●───●───●───●───●───●───●───●───●───●──●           │ 开发主线
        │     │   │   │       │   │   │       │   │   │              │
        └─────┼───┼───┼───────┼───┼───┼───────┼───┼───┼──────────────┘
              │   │   │       │   │   │       │   │   │
        ┌─────┼───┼───┼───────┼───┼───┼───────┼───┼───┼──────────────┐
feature │     ●───●   │       ●───●   │       ●───●   │              │ 功能开发
        │             ●───●           ●───●           ●───●           │
        └─────────────────────────────────────────────────────────────┘

图例：
● 提交点
─ 分支线
↑ 合并方向
```

## 本项目的Git Flow实践图

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    计算器项目 Git Flow 实际流程图                             │
└─────────────────────────────────────────────────────────────────────────────┘

开发者：Alice👩 Bob👨 Charlie👦

时间线 ──────────────────────────────────────────────────────────────────────►

main    ●─────────────────[v1.0.0]───────────────────[v1.0.1]─────────►
        │                    ↑                           ↑
        │                    │                           │
        │                 merge                      merge(hotfix)
        │                    │                           │
        │              ┌─────┴─────┐              ┌──────┴──────┐
        │              │release/1.0│              │hotfix/     │
        │              │     👩     │              │negative-fix│
        │              └─────┬─────┘              │     👩      │
        │                    │                    └──────┬──────┘
        │                    │                           │
develop ●──[初始化]──●──●──●─┴──●────●────●──[冲突]──●──●──●──●──●─────►
        │     👩      │  │  │    │    │    │         │  │  │  │  │
        │            │  │  │    │    │    │         │  │  │  │  │
        │      ┌─────┴──┴──┴────┴┐ ┌─┴────┴┐ ┌─────┴┐ │  │  │  │
        │      │feature/basic-   │ │feature│ │feature│ │  │  │  │
        │      │calculator       │ │/multi- │ │/div-  │ │  │  │  │
        │      │      👩          │ │plication│ision │ │  │  │  │
        │      └─────────────────┘ │   👨    │ │  👩   │ │  │  │  │
        │                          └────────┘ └───────┘ │  │  │  │
        │                                               │  │  │  │
        │                    ┌──────────────────────────┴┐ │  │  │
        │                    │feature/power-functions    │ │  │  │
        │                    │          👩                │ │  │  │
        │                    └───────────────────────────┘ │  │  │
        │                              ┌───────────────────┴┐ │  │
        │                              │feature/history-    │ │  │
        │                              │export      👨       │ │  │
        │                              └────────────────────┘ │  │
        │                                      ┌──────────────┴┐ │
        │                                      │feature/       │ │
        │                                      │improved-ui 👦 │ │
        │                                      └───────────────┘ │
        │                                                        ↓
        └────────────────────────────────────────────────────────┴─────►

关键事件：
[初始化] - Alice创建项目结构
[v1.0.0] - 发布基础版本（加减法）
[冲突]   - Bob和Alice的代码产生冲突
[v1.0.1] - 紧急修复负数显示问题
```

## 详细操作步骤

### 阶段1：项目初始化（Alice负责）

#### 1.1 创建项目并初始化Git
```bash
# Alice的操作
mkdir git-flow-demo
cd git-flow-demo
git init

# 设置身份
git config user.name "Alice"
git config user.email "alice@example.com"

# 创建初始提交
echo "# git-flow-demo" > README.md
git add README.md
git commit -m "Initial commit"
```

#### 1.2 创建develop分支
```bash
# 创建并切换到develop分支
git checkout -b develop

# 创建项目基础文件
cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
.venv/
*.log
EOF

# 更新README
cat > README.md << 'EOF'
# Git Flow 计算器演示项目
这是一个使用Python编写的计算器项目，用于详细演示Git Flow工作流程。
EOF

# 提交
git add .gitignore README.md
git commit -m "docs: 初始化项目，添加Git Flow文档和gitignore"
```

### 阶段2：单人开发 - v1.0.0基础计算器（Alice）

#### 2.1 创建feature分支
```bash
# 从develop创建feature分支
git checkout develop
git checkout -b feature/basic-calculator
```

#### 2.2 开发基础功能
```bash
# 创建calculator.py
cat > calculator.py << 'EOF'
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
        """加法运算"""
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result
        
    def subtract(self, a, b):
        """减法运算"""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
        
    def _add_to_history(self, operation):
        """添加操作到历史记录"""
        self.history.append(operation)
        
    def get_history(self):
        """获取计算历史"""
        return self.history.copy()
        
    def clear_history(self):
        """清空历史记录"""
        self.history.clear()
EOF

# 提交第一个功能
git add calculator.py
git commit -m "feat: 添加Calculator类和加减法功能"

# 创建main.py
cat > main.py << 'EOF'
#!/usr/bin/env python3
"""
计算器命令行界面
提供用户交互功能
"""

from calculator import Calculator

def print_menu():
    """打印操作菜单"""
    print("\n========== 计算器 v1.0.0 ==========")
    print("1. 加法")
    print("2. 减法")
    print("3. 查看历史")
    print("4. 清空历史")
    print("0. 退出")
    print("===================================")

def get_numbers():
    """获取用户输入的两个数字"""
    try:
        a = float(input("请输入第一个数: "))
        b = float(input("请输入第二个数: "))
        return a, b
    except ValueError:
        print("输入错误！请输入有效的数字。")
        return None, None

def main():
    """主函数"""
    calc = Calculator()
    print("欢迎使用计算器 v1.0.0！")
    
    while True:
        print_menu()
        
        try:
            choice = input("\n请选择操作 (0-4): ")
            
            if choice == '0':
                print("感谢使用，再见！")
                break
                
            elif choice == '1':
                # 加法
                a, b = get_numbers()
                if a is not None and b is not None:
                    result = calc.add(a, b)
                    print(f"结果: {result}")
                    
            elif choice == '2':
                # 减法
                a, b = get_numbers()
                if a is not None and b is not None:
                    result = calc.subtract(a, b)
                    print(f"结果: {result}")
                    
            elif choice == '3':
                # 查看历史
                history = calc.get_history()
                if history:
                    print("\n计算历史:")
                    for i, record in enumerate(history, 1):
                        print(f"{i}. {record}")
                else:
                    print("暂无计算历史。")
                    
            elif choice == '4':
                # 清空历史
                calc.clear_history()
                print("历史记录已清空。")
                
            else:
                print("无效选择，请重试。")
                
        except KeyboardInterrupt:
            print("\n\n程序被中断，再见！")
            break
        except Exception as e:
            print(f"发生错误: {e}")

if __name__ == "__main__":
    main()
EOF

# 创建requirements.txt
echo "# 基础版本暂无外部依赖" > requirements.txt

# 提交主程序
git add main.py requirements.txt
git commit -m "feat: 添加命令行界面和项目依赖文件"
```

#### 2.3 合并feature到develop
```bash
# 切换到develop
git checkout develop

# 使用--no-ff确保创建合并提交
git merge --no-ff feature/basic-calculator -m "merge: 合并基础计算器功能到develop"

# 删除feature分支（Git Flow标准做法）
git branch -d feature/basic-calculator
```

#### 2.4 创建release分支并发布
```bash
# 从develop创建release分支
git checkout -b release/1.0.0

# 更新版本信息（在README中添加版本号）
sed -i '8a\- **当前版本**: v1.0.0' README.md
git add README.md
git commit -m "chore: 准备v1.0.0版本发布"

# 合并到main
git checkout main
git merge --no-ff release/1.0.0 -m "merge: 发布v1.0.0版本"

# 打标签
git tag -a v1.0.0 -m "版本 v1.0.0: 基础计算器功能（加减法）"

# 合并回develop
git checkout develop
git merge --no-ff release/1.0.0 -m "merge: 同步release/1.0.0到develop"

# 删除release分支
git branch -d release/1.0.0
```

### 阶段3：双人协作 - v1.1.0添加乘除功能

#### 3.1 Bob开发乘法功能
```bash
# Bob的操作
git config user.name "Bob"
git config user.email "bob@example.com"

# 从develop创建feature分支
git checkout develop
git checkout -b feature/multiplication

# 修改calculator.py，在subtract方法后添加：
# （在第45行后添加）
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

# 修改main.py
# 1. 更新菜单（第12行改为v1.1.0，在减法后添加"3. 乘法"）
# 2. 更新菜单选项范围（第47行改为"(0-5): "）
# 3. 在减法处理后添加乘法处理代码

git add calculator.py main.py
git commit -m "feat: 添加乘法功能"
```

#### 3.2 Alice同时开发除法功能
```bash
# Alice的操作（在另一个时间点）
git config user.name "Alice"
git config user.email "alice@example.com"

# 从develop创建另一个feature分支
git checkout develop
git checkout -b feature/division

# 也修改calculator.py，在subtract方法后添加：
# （注意：这会导致冲突，因为Bob也在相同位置添加代码）
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

# 同样修改main.py
# 1. 更新菜单（第12行改为v1.1.0，在减法后添加"3. 除法"）
# 2. 更新菜单选项范围
# 3. 添加除法处理（包含异常处理）

git add calculator.py main.py
git commit -m "feat: 添加除法功能和除零错误处理"
```

#### 3.3 合并和冲突解决
```bash
# 先合并Bob的功能（无冲突）
git checkout develop
git merge --no-ff feature/multiplication -m "merge: 合并Bob的乘法功能"
git branch -d feature/multiplication

# 再合并Alice的功能（产生冲突）
git merge --no-ff feature/division -m "merge: 合并Alice的除法功能"

# 冲突信息：
# Auto-merging calculator.py
# CONFLICT (content): Merge conflict in calculator.py
# Auto-merging main.py
# CONFLICT (content): Merge conflict in main.py
```

### 冲突解决详解

#### 冲突1：calculator.py中的方法位置冲突

冲突内容：
```python
    def subtract(self, a, b):
        """减法运算"""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
        
<<<<<<< HEAD
    def multiply(self, a, b):
        """乘法运算"""
        result = a * b
        self._add_to_history(f"{a} × {b} = {result}")
=======
    def divide(self, a, b):
        """除法运算"""
        if b == 0:
            raise ValueError("错误：除数不能为0！")
        result = a / b
        self._add_to_history(f"{a} ÷ {b} = {result}")
>>>>>>> feature/division
        return result
```

解决方案：保留两个方法
```python
    def subtract(self, a, b):
        """减法运算"""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
        
    def multiply(self, a, b):
        """乘法运算"""
        result = a * b
        self._add_to_history(f"{a} × {b} = {result}")
        return result
        
    def divide(self, a, b):
        """除法运算"""
        if b == 0:
            raise ValueError("错误：除数不能为0！")
        result = a / b
        self._add_to_history(f"{a} ÷ {b} = {result}")
        return result
```

#### 冲突2：main.py中的菜单冲突

冲突内容：
```python
    print("1. 加法")
    print("2. 减法")
<<<<<<< HEAD
    print("3. 乘法")
=======
    print("3. 除法")
>>>>>>> feature/division
    print("4. 查看历史")
    print("5. 清空历史")
```

解决方案：调整菜单顺序
```python
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("5. 查看历史")
    print("6. 清空历史")
```

同时需要：
1. 更新选择范围为"(0-6): "
2. 调整后续的elif选项编号
3. 确保两个功能的处理代码都包含

#### 完成冲突解决
```bash
# 手动编辑文件解决冲突后
git add calculator.py main.py
git commit -m "merge: 解决合并冲突，整合乘法和除法功能"

# 删除Alice的分支
git branch -d feature/division
```

### 阶段4：三人协作 - v2.0.0高级功能

#### 4.1 Alice添加幂运算功能
```bash
git checkout develop
git checkout -b feature/power-functions

# 在calculator.py添加power和square_root方法
# 代码略（见实际文件）

git add calculator.py
git commit -m "feat: 添加幂运算和平方根功能"
```

#### 4.2 Bob添加历史导出功能
```bash
git config user.name "Bob"
git checkout develop
git checkout -b feature/history-export

# 在calculator.py添加export_history方法
# 代码略（见实际文件）

git add calculator.py
git commit -m "feat: 添加历史记录导出功能"
```

#### 4.3 Charlie改进UI
```bash
git config user.name "Charlie"
git config user.email "charlie@example.com"
git checkout develop
git checkout -b feature/improved-ui

# 创建新文件ui_helper.py
# 包含颜色定义和格式化函数

git add ui_helper.py
git commit -m "feat: 添加UI辅助模块，支持彩色输出"
```

#### 4.4 依次合并（无冲突）
```bash
git checkout develop
git merge --no-ff feature/power-functions -m "merge: 合并Alice的幂运算功能"
git merge --no-ff feature/history-export -m "merge: 合并Bob的历史导出功能"
git merge --no-ff feature/improved-ui -m "merge: 合并Charlie的UI改进"

# 删除所有feature分支
git branch -d feature/power-functions feature/history-export feature/improved-ui
```

### 阶段5：Hotfix流程 - v1.0.1紧急修复

#### 5.1 发现问题
生产环境（main分支）发现bug：减法结果为负数时显示格式有问题

#### 5.2 创建hotfix
```bash
# 从main分支创建hotfix（注意不是从develop）
git checkout main
git checkout -b hotfix/negative-number-fix

# 修改calculator.py的subtract方法
def subtract(self, a, b):
    """减法运算"""
    result = a - b
    # 修复：确保负数结果正确显示
    if result < 0:
        self._add_to_history(f"{a} - {b} = ({abs(result)})")
    else:
        self._add_to_history(f"{a} - {b} = {result}")
    return result

git add calculator.py
git commit -m "fix: 修复减法负数结果显示问题"
```

#### 5.3 合并hotfix
```bash
# 合并到main
git checkout main
git merge --no-ff hotfix/negative-number-fix -m "merge: 紧急修复v1.0.1 - 负数显示问题"
git tag -a v1.0.1 -m "版本 v1.0.1: 修复减法负数显示问题"

# 合并到develop（重要！确保修复也在开发分支中）
git checkout develop
git merge --no-ff hotfix/negative-number-fix -m "merge: 同步hotfix到develop"

# 删除hotfix分支
git branch -d hotfix/negative-number-fix
```

## 关键要点总结

1. **分支命名规范**
   - feature/功能名称
   - release/版本号
   - hotfix/问题描述

2. **合并策略**
   - 始终使用 `--no-ff` 保留合并历史
   - feature完成后立即删除分支

3. **冲突预防**
   - 经常从develop拉取最新代码
   - 功能模块化，减少文件重叠
   - 及时沟通协调

4. **版本管理**
   - main分支只包含稳定版本
   - 每个版本都要打tag
   - hotfix要同时合并到main和develop