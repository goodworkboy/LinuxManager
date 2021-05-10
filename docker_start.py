
import os
import global_variable as gl
def start_container():
    command = "docker start centos7"
    fp = os.popen(command)