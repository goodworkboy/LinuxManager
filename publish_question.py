import os
import global_variable as gl

docker_volume_mount_dir = "/src/experiences"

#将实验题目拷贝到容器内实验目录在服务器上的挂载目录下#将实验题目拷贝到容器内实验目录在服务器上的挂载目录下
def publishQuestionsUI1():
    studentNums = gl.get_value(gl.gl_student_nums_key)
    path = input("请输入实验题目路径：")
    for studentNum in studentNums :
        student_experience_path="/home/jlurj"+studentNum+"/experiences/"
        fp = os.popen("cp -nR %s %s" %(path,student_experience_path))
        result = fp.read()
        if result < 0:
            print("%s的题目发放失败"%(studentNum))


def publishQuestionsUI():
    path = input("请输入实验题目路径：")
    fp = os.popen("cp -nR %s %s" %(path,docker_volume_mount_dir))
    result = len(fp.read())
    if result > 0:
        print("题目发放失败" )
        isContinue = input("是否继续(y/n)?")
        if isContinue == "y":
            publishQuestionsUI()

