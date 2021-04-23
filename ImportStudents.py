import time

import xlrd
import xlwt
import os
import global_variable as gl

student_username_prefix = "jlurj"

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
        gl.set_value("studentNums",studentNums)
        create_users(studentNums)
        backup()
    except FileNotFoundError:
        print("文件打开失败!")
        isContinue = input("是否继续(y/n)?")
        if isContinue == "y":
            importStudentsUI()
    except ValueError:
        print("没有找到学生学号这一列")


def create_users(studentNums):
    passwd = "123456"
    for studentNum in studentNums:
        temp = os.system("useradd jlurj%s -p%s" % (studentNum, passwd))
        if temp==0:
            path = "/home/jlurj" + studentNum + "/experiences"
            os.popen("mkdir -p %s" % (path))
            print("学号%s的实验帐户创建成功，帐户名为jlurj%s" % (studentNum,studentNum))
        else:
            print("帐户创建失败，该学生%s帐户以存在"%(studentNum))


def importStudentsUI():
    path = input("请输入学生名单的路径:")
    #path = "/home/liugx/test.xlsx"
    choose = input("是否导入学生名单并创建实验用户(y/n)?")
    if choose == "y":
        action(path)

def backup():
    student_nums = gl.get_value(gl.gl_student_nums_key)
    fp = open(gl.system_data_file, "w", encoding="utf-8")
    for student_num in student_nums:
        fp.write(student_num)
        fp.write("\n")
    fp.close()
