# -*- coding: utf-8 -*-
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import subprocess
import time

import xlrd
import import_students
import paramiko

from multiprocessing import Process

def action(path):
    try:
        data = xlrd.open_workbook(path)
        table = data.sheet_by_index(0)
        nrows = table.nrows
        if nrows <= 0:
            print("")
            return
        first_row = table.row_values(0)
        index = first_row.index("学号")
        studentNum1 = table.col_values(index, 1, nrows)
        studentNums = [str(int(studentNum1[i])) for i in range(0, len(studentNum1))]
        for student_num in studentNums:
            #login_in1(student_num)
            p = Process(target=login_in1,args=(student_num,))
            p.start()

    except FileNotFoundError:
        print("文件打开失败!")
        isContinue = input("是否继续(y/n)?")
        if isContinue == "y":
            import_students_UI()
    except ValueError:
        print("没有找到学生学号这一列")

def login_in1(student_num):
    passwd = "12345678"
    username= import_students.student_username_prefix+student_num
    args = "sshpass -p "+passwd+" ssh -tt "+username+"@127.0.0.1 -p 8889"
    args1 = "sshpass -p 12345678 ssh -tt jlurj55170423@127.0.0.1 -p8889"
    p = subprocess.Popen(args ,  shell=True)
    p.wait(200)
    print(student_num+" login in")

def login_in2(student_num):
    passwd = "12345678"
    username= import_students.student_username_prefix+student_num
    args = "sshpass -p "+passwd+" ssh "+username+"@127.0.0.1 -p 8889"
    subprocess.Popen(args , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


def login_in(student_num):
    passwd = "12345678"
    username= import_students.student_username_prefix+student_num
    ip="127.0.0.1"
    port = 8889
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, passwd)

    print(student_num+" login in")
    stdin, stdout, stderr = ssh.exec_command('ls')
    print(stdout.read())
    time.sleep(50)

def import_students_UI():
    #path = input("请输入学生名单的路径:")
    path = "/home/liugx/test.xlsx"
    action(path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import_students_UI()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
