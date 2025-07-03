"""
UI辅助模块
提供彩色输出和格式化功能
"""

import sys


class Colors:
    """终端颜色代码"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_header(text):
    """打印标题"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'=' * 40}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text.center(40)}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'=' * 40}{Colors.ENDC}")


def print_menu_item(number, text):
    """打印菜单项"""
    print(f"{Colors.CYAN}{number}.{Colors.ENDC} {text}")


def print_success(message):
    """打印成功消息"""
    print(f"{Colors.GREEN}✓ {message}{Colors.ENDC}")


def print_error(message):
    """打印错误消息"""
    print(f"{Colors.RED}✗ {message}{Colors.ENDC}")


def print_result(result):
    """打印计算结果"""
    print(f"\n{Colors.YELLOW}{Colors.BOLD}结果: {result}{Colors.ENDC}\n")


def print_info(message):
    """打印信息消息"""
    print(f"{Colors.BLUE}ℹ {message}{Colors.ENDC}")


def format_history_item(index, item):
    """格式化历史记录项"""
    return f"{Colors.CYAN}{index}.{Colors.ENDC} {item}"


def clear_screen():
    """清屏"""
    if sys.platform == "win32":
        import os
        os.system("cls")
    else:
        print("\033[2J\033[H")