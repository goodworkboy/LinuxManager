import os
def heart_check_ui():
    fp = os.popen("pwd")
    path = fp.read()
    filename = "heart_check_thread.py"
    commond = "gnome-terminal -e 'python "+filename+"'"
    temp = os.popen(commond)