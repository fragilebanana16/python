# getpass是一个非常简单的Python标准库
# 主要包含两个函数:
# 函数1:getuser //从系统变量中自动获取用户名
# 函数2:getpass // 类似于input, 但不会将我们输入的字符显示在命令行中(不回显)

from __future__ import print_function

import getpass


# 自动读取当前用户的名称
user = getpass.getuser()

print("尊敬的",user)

# 以不回显的方式,读取用户的输入
passwd = getpass.getpass("请输入您的密码:")

print("------------->华丽的分割线<----------------")


print("您的密码为:", passwd)

