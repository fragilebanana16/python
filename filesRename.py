# 将文件放入要命名的当前目录下运行
# 导入python内置的os模块和sys模块
import os
import sys
import datetime
import time
# 程序入口
##if __name__ == "__main__":
today = datetime.date.today()
print(today)
print("该操作将重命名当前路径下所有文件名：")
print("    1.统一添加文字前缀，如:周五xxxxx")
print("    2.统一添加尾部数字（增序），如:周五1")
print("    3.统一添加时间前缀，如:周五2018-08-10")
try:
    opt = int(input("请输入需要命名的规则:"))
except Exception:
    print("请输入序号！请输入序号！请输入序号！")
finally:
    print("option%s selected!"%opt)
#print("ok")
if opt == 1:
    # 获取需要添加的前缀
    pre = input("请输入需要添加的前缀:")
    # 为了美观,为前缀添加一个中括号
    mark = "%s"%pre
    # 获取本目录下所有的文件名
    old_names = os.listdir()
    # 遍历目录下的文件名
    for old_name in old_names:
        # 跳过本脚本文件 linux 下替换为sys.argv[0]
        if old_name != "filesRename.py":
            # 用新的文件名替换旧的文件名
            os.rename(old_name, mark+old_name)
    print("重命名成功")
elif opt == 2:
    mark = 0
    # 获取本目录下所有的文件名
    old_names = os.listdir()
    # 遍历目录下的文件名
    for old_name in old_names:
        # 跳过本脚本文件 linux 下替换为sys.argv[0]
        if old_name != "filesRename.py":
            # 用新的文件名替换旧的文件名
            (filename,extension) = os.path.splitext(old_name)
            mark += 1
            os.rename(old_name, filename+str(mark)+extension)
    print("重命名成功")
elif opt == 3:
    # 获取本目录下所有的文件名
    old_names = os.listdir()
    # 遍历目录下的文件名
    for old_name in old_names:
        # 跳过本脚本文件 linux 下替换为sys.argv[0]
        if old_name != "filesRename.py":
            # 用新的文件名替换旧的文件名
            os.rename(old_name, str(today)+old_name)
    print("重命名成功")

