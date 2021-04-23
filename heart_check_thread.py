import sys
import threading
import os
import global_variable as gl
import time

prefix = "liugx"

def do_once_check():
    fp = os.popen("w -shf")
    input_stream = fp.read()
    strs = input_stream.split(" ")
    online_student =[]
    for temp in strs:
        if temp.startswith(prefix):
            online_student.append(temp[5:len(temp)])
    return online_student

def is_online(temp):
    if temp:
        return "在线"
    else:
        return "离线"


def match_and_print(online_student):
    student_nums = gl.get_value(gl.gl_student_nums_key)
    time_local = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("学号    状态    时间")
    for student_num in student_nums:
        temp = is_online(student_num in online_student)

        temp = student_num+"    "+temp+"    "+time_local
        print("%s" % (temp))

if __name__ == '__main__':
    gl._init()
    if gl.get_value(gl.gl_student_nums_key) is None:
        time.sleep(1)
        exit()
    while True:
        os.system("clear")
        print("学生在线情况")
        online_student = do_once_check()
        match_and_print(online_student)
        time.sleep(2)

