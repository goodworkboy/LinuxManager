import xlrd
import os
import global_variable as gl


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
    except FileNotFoundError:
        print("文件打开失败!")
        isContinue = input("是否继续(y/n)?")
        if isContinue == "y":
            importStudentsUI()
    except ValueError:
        print("没有找到学生学号这一列")
    else:
        print(studentNums)


def create_users(studentNums):
    passwd = "123456"
    for studentNum in studentNums:
        os.system("useradd jlurj%s -p%s" % (studentNum, passwd))
        path = "/home/jlurj" + studentNum + "/experiences"
        os.system("mkdir -p %s" % (path))
        print("jlurj%s create successful" % (studentNum))


def importStudentsUI():
    # path = input("please input the location of students l book:")
    path = "/home/liugx/test.xlsx"
    choose = input("是否导入学生名单并创建实验用户(y/n)?")
    if choose == "y":
        action(path)
