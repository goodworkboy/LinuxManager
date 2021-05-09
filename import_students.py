import time

import xlrd
import os
import global_variable as gl

student_username_prefix = "jlurj"
student_usergroup="students"

#导入学生名单
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
        gl.append_value("studentNums",studentNums)
        create_users(studentNums)
        backup()
    except FileNotFoundError:
        print("文件打开失败!")
        isContinue = input("是否继续(y/n)?")
        if isContinue == "y":
            importStudentsUI()
    except ValueError:
        print("没有找到’学号‘这一列")
        isContinue = input("是否继续(y/n)?")
        if isContinue == "y":
            importStudentsUI()

#创建实验账户的函数
def create_users(studentNums):
    passwd = "IZqjXY5YZu.9I" #初始密码‘12345678’
    #为每一位学生创建实验账户
    for studentNum in studentNums:
        temp = os.system(gl.docker_command_pre+"useradd jlurj%s -p %s -g %s" % (studentNum , passwd,student_usergroup))
        if temp==0:
            #path = "/home/jlurj" + studentNum + "/experiences"
            #student_account = student_username_prefix+studentNum
            #os.popen("mkdir -p %s" % (path))
            command = gl.docker_command_pre+"ln -s /src/experiences /home/"+student_username_prefix+studentNum+"/experiences"
            print("学号%s的实验帐户创建成功，帐户名为jlurj%s" % (studentNum, studentNum))
        else:
            print("帐户创建失败，该学生%s实验帐户已存在"%(studentNum))


def importStudentsUI():
    path = input("请输入学生名单的路径:")
    #path = "/home/liugx/test.xlsx"
    choose = input("是否导入学生名单并创建实验用户(y/n)?")
    if choose == "y":
        action(path)

#将创建好的实验账户名单保存到本地
def backup():
    student_nums = gl.get_value(gl.gl_student_nums_key)
    fp = open(gl.system_data_file, "w", encoding="utf-8")
    for student_num in student_nums:
        fp.write(student_num)
        fp.write("\n")
    fp.close()
