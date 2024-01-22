# name = "itheima"
# lenght = len(name)
# print(lenght)

#
# def my_len(data):  # data为参数，函数暂无返回值
#     count = 0
#     for i in data:
#         count += 1
#     print(f"字符串的长度是{count}")
#
#
# str = "itheima"  # 调用函数
# my_len(str)
#
#
# def test_COVID19():
#     print("")

#
# def add(x, y):
#     result = x + y
# # 返回值呢？？
#     print(f"相加的结果为{result}")
# add(3, 5)



# def temp_check(temp):
#     if temp_check(temp) <= 37.5:  #类型为none??
#         print("正常")
#     else:
#         print("滚出去")



# def temp_check(temp):
#     if temp <= 37.5:
#         print(f"{temp},正常")
#     else:
#         print(f"{temp},滚出去")
# temp = int(input("请输入您的体温："))
# temp_check(temp)

#
# def temp_check(temp):
#     if temp <= 37.5:
#         print(f"{temp},正常")
#     else:
#         print(f"{temp},滚出去")
# temp = input("请输入您的体温：")
# temp_check(temp)

#
# def add(a, b):
#      result = a + b
#      return result # 计算完，将result的值返回，赋给变量r，但有的函数只干活，就不返回东西
#      #  return会结束函数中的程序，相当于写了return函数就运行结束了（个人理解，勿喷，有错误就指出）
#      print('完事了')
#
# r = add(4, 5)
# print(r)


#
# def age_check(num):
#     if num >= 18:
#         return "success" # 返回值不打印出来，程序运行后看不出来，print一下就好了
#
#     # else:
#     #     return None
#
# result = age_check(16)
# print(result)
# # if result == None:
# if not result:
#     print("未成年")


money = 500000
name = None  # 未赋值的变量，可以先赋为None
name = input("请输入姓名：")


def inquiry_Credit(show_header):
    if show_header:
        print("-----余额查询-----")
    print(f"{name}，您好，您当前的余额为 {money} 元")


def deposit(add):
    global money
    money += add

    print("------存款------")
    print(f"您好，您单次存入{add}元") #相当与参数是用户手动输入的，这里先定义出来
    # return add   这里不写返回值 为什么？？
    inquiry_Credit(False)


def get_money(delete):
    global money
    money -= delete
    print("------取款------")
    print(f"您好，您单次取出{delete}元")   # 同add
    inquiry_Credit(False)


def main():
    print("------主菜单------\t\t")
    print("查看余额请按[1]\t\t")
    print("存款请按[2]\t\t")
    print("取款请按[3]\t\t")
    print("退出请按[4]\t\t")
    return int(input("请输入键盘上对应的数字："))  # 为什么int(input("~"))就不行呢？ 因为"1"是字符串
    #  字符串1和数字1是不一样的

while True:
    key_num = main()

    if key_num == 1:
        inquiry_Credit(True)
        continue
    elif key_num == 2:
        add = int(input("请输入您存入的金额："))
        deposit(add)
        continue
    elif key_num == 3:
        delete = int(input("请输入您想取出的金额："))
        get_money(delete)
        continue
    else:
        print("已退出,感谢您的使用！")
        break




