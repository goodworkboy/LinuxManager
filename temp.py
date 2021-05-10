
import  os
import global_variable as gl

if __name__ == '__main__':
    fp = open(gl.system_data_file, "w", encoding="utf-8")
    student_num_start = 55170400
    for i in range(0,401):
        student_num_start+=1
        fp.write(str(student_num_start))
        fp.write("\n")
    fp.close()
