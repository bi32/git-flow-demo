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
    """
    获取用户输入的两个数字
    
    返回:
        tuple: (第一个数, 第二个数)
    """
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