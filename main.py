# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import xlrd

url = "/home/liugx/test.xlsx"
def test_xlrd():
    data = xlrd.open_workbook(url)
    table = data.sheet_by_index(0)
    nrows = table.nrows
    for i in range(1, nrows):
        print(table.row_values(i))



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    test_xlrd()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
