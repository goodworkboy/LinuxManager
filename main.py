# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import xlrd

from ImportStudents import importStudentsUI
import global_variable as gl
from PublishQuestion import publishQuestionsUI


def choose_action():
    choose = input("输入选项：")
    if choose == "1":
        importStudentsUI()
    elif choose == "2":
        publishQuestionsUI()
    elif choose == "3":
        print("4、监测学生在线情况")
    elif choose == "0":
        return True
    else:
        print("无效输入")
        choose_action();


def main_menu():
    gl._init()
    while True :
        print("Linux实验管理平台")
        print("1、导入学生名单并创建实验帐户")
        print("2、发布实验题目")
        print("3、监测学生在线情况")
        print("0、退出系统")
        if choose_action():
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
