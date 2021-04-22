
import xlrd

system_data_file = "students.txt"
gl_student_nums_key="studentNums"

def _init():#初始化
    global _global_dict
    _global_dict = {}
    try:
        fp = open(system_data_file, "r", encoding="utf-8");
        student_nums = []
        for line in fp.readlines():
            strs = line.split(" ")
            student_nums.append(strs[0].replace("\n", ""))
        _global_dict[gl_student_nums_key] = student_nums

    except FileNotFoundError:
        print("系统文件打开失败!")
    except ValueError:
        print("没有找到学生学号这一列")
    finally:
        fp.close()

def set_value(key , value):
    _global_dict[key] = value


def append_value(key , value):
    old_value = get_value(key)
    if old_value == None:
        set_value(key, value)
    else:
        _global_dict[key] = old_value.append(value)

def get_value(key , defValue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defValue