
import os
import import_students
import global_variable as gl

def remove_one_student(student_num):
    command = gl.docker_command_pre+"userdel -r jlurj"+student_num
    temp = os.system(command)
    if temp==0:
        print("已移除学生%s的帐户"%(student_num))
    else:
        print("帐户删除失败！")

def remove_all_students():
    command =gl.docker_command_pre+ "cut -d: -f1 /etc/passwd"
    fp = os.popen(command)
    all_users = fp.read().split("\n")
    for user in all_users:
        if user.strip().startswith( import_students.student_username_prefix):
            remove_one_student(user[5:len(user)])

if __name__ == '__main__':
    remove_all_students()