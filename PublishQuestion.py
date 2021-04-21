import os
import global_variable as gl
def publishQuestionsUI():
    studentNums = gl.get_value("studentNums")
    print(studentNums)
    path = input("请输入实验题目路径：")
    for studentNum in studentNums :
        student_experience_path="/home/jlurj"+studentNum+"/experiences/"
        result = os.system("cp -nR %s %s" %(path,student_experience_path))
        if result < 0:
            print("%s的题目发放失败"%(studentNum))

