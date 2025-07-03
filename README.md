# Git Flow 计算器演示项目

这是一个使用Python编写的计算器项目，用于详细演示Git Flow工作流程。

## 项目概述

- **语言**: Python
- **目的**: 演示完整的Git Flow工作流程，包括多人协作、分支管理、版本发布等

## Git Flow 分支结构

### 主要分支
- **main**: 生产环境分支，只包含稳定发布版本
- **develop**: 开发分支，所有功能开发完成后合并到这里

### 支持分支
- **feature/**: 功能分支，从develop创建，完成后合并回develop
- **release/**: 发布分支，从develop创建，准备新版本发布
- **hotfix/**: 热修复分支，从main创建，修复紧急问题

## Git Flow 完整流程演示

### 第一阶段：项目初始化和基础设置

#### 1. 初始化Git仓库和创建基础分支
```bash
# 初始化仓库（已完成）
# git init

# 创建并切换到develop分支
git checkout -b develop

# 推送develop分支到远程（如果有远程仓库）
# git push -u origin develop
```

### 第二阶段：单人开发流程（v1.0.0 - 基础计算器）

#### 1. 创建第一个feature分支
```bash
# 从develop分支创建feature分支
git checkout develop
git checkout -b feature/basic-calculator

# 开发基础计算器功能（加减法）
# 创建 calculator.py - 计算器核心类
# 创建 main.py - 命令行界面
```

### 第三阶段：双人协作流程（v1.1.0 - 添加乘除功能）

模拟开发者A和开发者B同时开发不同功能

### 第四阶段：三人协作流程（v2.0.0 - 高级功能）

三个开发者同时开发：高级运算、历史记录、UI改进

### 第五阶段：Hotfix流程演示

演示如何处理生产环境的紧急问题

## 项目结构
```
git-flow-demo/
├── README.md           # 项目说明和Git Flow流程文档
├── calculator.py       # 计算器核心类
├── main.py            # 命令行界面主程序
├── test_calculator.py # 单元测试
├── requirements.txt   # 项目依赖
└── .gitignore        # Git忽略文件
```