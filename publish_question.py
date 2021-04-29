import os
import global_variable as gl

docker_volume_mount_dir = "/src/experiences"

def publishQuestionsUI1():
    studentNums = gl.get_value(gl.gl_student_nums_key)
    path = input("请输入实验题目路径：")
    for studentNum in studentNums :
        student_experience_path="/home/jlurj"+studentNum+"/experiences/"
        result = os.system("cp -nR %s %s" %(path,student_experience_path))
        if result < 0:
            print("%s的题目发放失败"%(studentNum))


def publishQuestionsUI():
    path = input("请输入实验题目路径：")
    result = os.system("cp -nR %s %s" %(path,docker_volume_mount_dir))
    if result > 0:
        print("题目发放失败")