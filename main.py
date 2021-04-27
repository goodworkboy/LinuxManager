# -*- coding: utf-8 -*-
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import xlrd

from import_students import importStudentsUI
import global_variable as gl
from publish_question import publishQuestionsUI
from heart_check import heart_check_ui


def choose_action():
    choose = input("输入选项：")
    if choose == "1":
        importStudentsUI()
    elif choose == "2":
        publishQuestionsUI()
    elif choose == "3":
        heart_check_ui()
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
