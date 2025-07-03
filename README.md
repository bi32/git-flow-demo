# Git Flow 计算器演示项目

这是一个使用Python编写的计算器项目，用于详细演示Git Flow工作流程。

## 项目概述

- **语言**: Python
- **目的**: 演示完整的Git Flow工作流程，包括多人协作、分支管理、版本发布等
- **当前版本**: v1.0.0

## Git Flow 分支结构

### 主要分支
- **main**: 生产环境分支，只包含稳定发布版本
- **develop**: 开发分支，所有功能开发完成后合并到这里

### 支持分支
- **feature/**: 功能分支，从develop创建，完成后合并回develop
- **release/**: 发布分支，从develop创建，准备新版本发布
- **hotfix/**: 热修复分支，从main创建，修复紧急问题

## Git Flow 完整流程演示

### 第一阶段：项目初始化和基础设置 ✅

#### 1. 初始化Git仓库和创建基础分支
```bash
# 设置Git用户身份
git config user.name "Alice"
git config user.email "alice@example.com"

# 创建并切换到develop分支
git checkout -b develop

# 创建初始文档
# - README.md (Git Flow文档)
# - .gitignore (Python项目忽略文件)

git add README.md .gitignore
git commit -m "docs: 初始化项目，添加Git Flow文档和gitignore"
```

### 第二阶段：单人开发流程（v1.0.0 - 基础计算器）✅

#### 1. Alice创建第一个feature分支
```bash
# 从develop分支创建feature分支
git checkout develop
git checkout -b feature/basic-calculator
```

#### 2. 开发基础功能
- 创建 `calculator.py` - 计算器核心类（加减法）
- 创建 `main.py` - 命令行界面
- 创建 `requirements.txt` - 项目依赖

```bash
# 提交代码
git add calculator.py
git commit -m "feat: 添加Calculator类和加减法功能"

git add main.py requirements.txt
git commit -m "feat: 添加命令行界面和项目依赖文件"
```

#### 3. 合并到develop
```bash
git checkout develop
git merge --no-ff feature/basic-calculator -m "merge: 合并基础计算器功能到develop"
git branch -d feature/basic-calculator  # 删除feature分支
```

#### 4. 创建release并发布
```bash
# 创建release分支
git checkout -b release/1.0.0

# 更新版本信息
# 修改README.md添加版本号
git add README.md
git commit -m "chore: 准备v1.0.0版本发布"

# 合并到main
git checkout main
git merge --no-ff release/1.0.0 -m "merge: 发布v1.0.0版本"
git tag -a v1.0.0 -m "版本 v1.0.0: 基础计算器功能（加减法）"

# 合并回develop
git checkout develop
git merge --no-ff release/1.0.0 -m "merge: 同步release/1.0.0到develop"

# 删除release分支
git branch -d release/1.0.0
```

### 第三阶段：双人协作流程（v1.1.0 - 添加乘除功能）✅

#### 1. Bob开发乘法功能
```bash
# 切换到Bob身份
git config user.name "Bob"
git config user.email "bob@example.com"

# 创建feature分支
git checkout develop
git checkout -b feature/multiplication

# 修改calculator.py添加multiply方法
# 修改main.py添加乘法菜单选项
git add calculator.py main.py
git commit -m "feat: 添加乘法功能"
```

#### 2. Alice同时开发除法功能
```bash
# 切换到Alice身份
git config user.name "Alice"
git config user.email "alice@example.com"

# 创建另一个feature分支
git checkout develop
git checkout -b feature/division

# 修改calculator.py添加divide方法（包含除零检查）
# 修改main.py添加除法菜单选项
git add calculator.py main.py
git commit -m "feat: 添加除法功能和除零错误处理"
```

#### 3. 合并和冲突解决
```bash
# 先合并Bob的功能
git checkout develop
git merge --no-ff feature/multiplication -m "merge: 合并Bob的乘法功能"
git branch -d feature/multiplication

# 再合并Alice的功能（产生冲突）
git merge --no-ff feature/division -m "merge: 合并Alice的除法功能"

# 冲突发生在calculator.py和main.py
# 手动解决冲突：保留乘法和除法两个功能
# 编辑文件，整合代码

git add calculator.py main.py
git commit -m "merge: 解决合并冲突，整合乘法和除法功能"
git branch -d feature/division
```

### 第四阶段：三人协作流程（v2.0.0 - 高级功能）✅

#### 1. 三个开发者同时开发不同功能

##### Alice: 添加平方和平方根功能
```bash
git checkout develop
git checkout -b feature/power-functions
# 修改calculator.py，添加power()和square_root()方法
git add calculator.py
git commit -m "feat: 添加幂运算和平方根功能"
```

##### Bob: 实现计算历史导出功能
```bash
git config user.name "Bob"
git checkout develop
git checkout -b feature/history-export
# 修改calculator.py，添加export_history()方法
git add calculator.py
git commit -m "feat: 添加历史记录导出功能"
```

##### Charlie: 改进UI界面
```bash
git config user.name "Charlie"
git checkout develop
git checkout -b feature/improved-ui
# 创建ui_helper.py模块
git add ui_helper.py
git commit -m "feat: 添加UI辅助模块，支持彩色输出"
```

#### 2. 依次合并三个功能
```bash
git checkout develop
git merge --no-ff feature/power-functions -m "merge: 合并Alice的幂运算功能"
git merge --no-ff feature/history-export -m "merge: 合并Bob的历史导出功能"
git merge --no-ff feature/improved-ui -m "merge: 合并Charlie的UI改进"

# 删除已合并的分支
git branch -d feature/power-functions feature/history-export feature/improved-ui
```

### 第五阶段：Hotfix流程演示 ✅

#### 模拟生产环境紧急bug修复

```bash
# 从main分支创建hotfix
git checkout main
git checkout -b hotfix/negative-number-fix

# 修复减法负数显示问题
# 修改calculator.py的subtract方法
git add calculator.py
git commit -m "fix: 修复减法负数结果显示问题"

# 合并到main并打标签
git checkout main
git merge --no-ff hotfix/negative-number-fix -m "merge: 紧急修复v1.0.1 - 负数显示问题"
git tag -a v1.0.1 -m "版本 v1.0.1: 修复减法负数显示问题"

# 合并到develop
git checkout develop
git merge --no-ff hotfix/negative-number-fix -m "merge: 同步hotfix到develop"

# 删除hotfix分支
git branch -d hotfix/negative-number-fix
```

## GitHub协作 ✅

### 推送到远程仓库
```bash
# 推送所有分支
git push -u origin main
git push -u origin develop

# 推送标签
git push origin --tags
```

### 创建GitHub Release
```bash
gh release create v1.0.0 --title "v1.0.0 - 基础计算器" --notes "功能特性..."
```

## 项目运行方式

```bash
# 克隆项目
git clone https://github.com/bi32/git-flow-demo.git
cd git-flow-demo

# 运行计算器
python main.py
```

## 版本历史

- **v1.0.0** (2025-01-03): 基础计算器，支持加减法
- **v1.0.1** (2025-01-03): 修复减法负数显示问题
- **v1.1.0** (开发中): 添加乘除法功能
- **v2.0.0** (开发中): 添加高级功能（幂运算、平方根、历史导出）和UI改进

## 重要说明：分支状态

**注意**：在Git Flow中，develop分支通常会领先于main分支，这是正常现象！

- **main分支**：只包含稳定发布版本（v1.0.0, v1.0.1）
- **develop分支**：包含所有最新开发的功能，等待下次发布

当前develop分支领先main分支15个提交，包含了乘除法、高级功能、UI改进等待发布的新特性。

## 项目结构
```
git-flow-demo/
├── README.md              # 项目说明和Git Flow流程文档
├── GITFLOW_DETAILED.md    # Git Flow详细教程（含冲突解决）
├── BRANCH_STATUS.md       # 分支状态说明
├── calculator.py          # 计算器核心类
├── main.py               # 命令行界面主程序
├── ui_helper.py          # UI辅助模块（彩色输出）
├── test_calculator.py    # 单元测试（待实现）
├── requirements.txt      # 项目依赖
├── LICENSE              # MIT许可证
└── .gitignore           # Git忽略文件
```