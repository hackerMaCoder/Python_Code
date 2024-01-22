
"""
# 变量 课后练习
money = 50
print("当前钱包余额：", money)
money = money - 10
print("购买了冰淇淋，花费：10 元")
money = money - 5
print("购买了可乐，花费：5 元")
print("最终，钱包剩余：", money,"元")



user_name = input("请输入用户名：")
user_type = input("请输入用户类型：")
print("您好，%s，您是尊贵的：%s用户，欢迎您的到来！"%(user_name,user_type))
print(f"您好，{user_name}，您是尊贵的：{user_type}用户，欢迎您的到来！")
"""

# num = 10>5
# print(f"10>5的结果是{num},类型是{type(num)}")

# ==,!=,<,>,+=,-=

# age = 10
# if age >= 18:
#     print("我已经成年了")
#     print("我要上大学了")
# print("时间过的真快啊")

# print("欢迎来到黑马儿童游乐场，儿童免费，成人收费")
# age = int(input("请输入您的年龄:"))

# if age >= 18:
#     print("您已成年，需补票10元")
#     if input()=="已补票":
#         print("hehe")
# else:
#     print("您未成年，可以免费游玩")
#     print("祝您游玩愉快！")


# print("欢迎来到黑马动物园")
# height = int(input("请输入您的身高(cm):"))
# VIP_Level = int(input("请输入您的VIP等级(1~5):"))
# if height < 120:
#     print("您的身高未超过120cm，可以免费游玩")
#     print("祝您游玩愉快！")
# elif VIP_Level > 3:
#     print("您的VIP等级高于3级，可以免费游玩")
#     print("祝您游玩愉快！")
# else:
#     print("您的身高超过120cm，您为非会员游客，需补票10元")
#     choice = input("是否已补票(Y/N):")
#     if "Y" == choice:
#             print("您已补票^_^!")
#             print("祝您游玩愉快！")
#     else:
#             print("请您及时补票！")

# 操，肝死我了，没想到 原来还能这么写，但思考的过程还是值得的

# print("欢迎来到黑马动物园")
# if int(input("请输入您的身高(cm):")) < 120:
#     print("您的身高未超过120cm，可以免费游玩")
#     print("祝您游玩愉快！")
# elif int(input("请输入您的VIP等级(1~5):")) > 3:
#     print("您的VIP等级高于3级，可以免费游玩")
#     print("祝您游玩愉快！")
# else:
#     print("您的身高超过120cm，您为非会员游客，需补票10元")
#     if input("是否补票(Y/N):") == "Y":
#
#         print("您已补票^_^!")
#         print("祝您游玩愉快！")
#     else:
#         print("请您及时补票！")


# if 10 == int(input("第一次猜的数字：")):
#     print("第一次就猜对了呢！真棒呀~")
# elif 10 == int(input("不对，再猜一次：")):
#     print("哎呦！不错哦~")
# elif 10 == int(input("不对，最后猜一次：")):
#     print("恭喜你，猜对啦！抓住了最后的机会~")
# else:
#     print("都不对，我想的是10，大傻逼！")


# if int(input("年龄:")) >=18 and int(input("年龄:"))<= 30:
#     print("符合标准，继续判断")
#     if int(input("入职时间:")) > 2:
#         print("符合")
#     elif int(input("职称级别:")) > 3:
#         print("符合")
#     else:
#         print("入职时间和级别不符合")
# else:
#     print("不符合")


# import random
# num = random.randint(1, 10)
#
# guess_num = int(input("请输入一个数字："))
# if guess_num == num:
#     print("恭喜你，猜对了")
# else:
#     if guess_num > num:
#         print("猜大了")
#     else:
#         print("猜小了")
#
# guess_num = int(input("请再次输入一个数字："))
# if guess_num == num:
#     print("恭喜你，这次猜对了")
# else:
#     if guess_num < num:
#         print("猜小了")
#     else:
#         print("猜大了")
#
# guess_num = int(input("请最后输入一个数字："))
# if guess_num == num:
#     print("恭喜你，终于猜对了")
# else:
#     if guess_num < num:
#         print("又猜小了")
#     else:
#         print("又猜大了")


# i = 1
# sum = 0
# while  i <= 100:
#     sum += i
#     i += 1
# print(sum)


# import random
# num = random.randint(1, 100)
#
# flag = True
# count = 0
#
# while flag:
#     guess_num = int(input("请输入一个数字(1~100)："))
#     count += 1
#     if guess_num == num:
#         print("恭喜你，猜对了！")
#         flag = False
#     else:
#         if guess_num > num:
#             print("猜大了")
#         else:
#             print("猜小了")
#
# print(f"你一共猜了{count}次")


# i = 1
#
# while i <= 100:
#     print(f"今天是表白的第{i}天")
#     j = 1
#     while j <= 10:
#         print(f"送给小妹第{j}支玫瑰花")
#         j += 1
#         print("小妹，我喜欢你！")  # 更舔！
#     i += 1
#
# print(f"坚持了{i-1}天，终于成功了!")


# print("hello", end='')
# print("jdv", end='')


# print("hello\tjack")
# print("linus\tlinux")

# i = 1
# sum = 1
# while i <= 9:
#     j = 1
#     sum = j * i
#     while j <= i:
#         print(f"{j}*{i}={sum}\t", end='')
#         j += 1  # 内层循环 变量条件的变化 是为了 触发 外层循环 变量条件的变化
#     i += 1
#     print()  # 执行换行操作


# name = "itheima"
# for x in name:
#     print(x)  # 注意是x，不是name


# name = "itheima is a brand of itcast"
# count = 0
# for x in name:
#     if x == "a":
#         count += 1
# print(f"itheima is a brand of itcast 中共有{count}个\"a\"")


# for x in range(5):
#     print(x,end='')
# print()
# for x in range(5,13):
#     print(x,end='')
# print()
# for x  in range(5,10,2):
#     print(x,end='')


# for i in range(1,11):  # 通过range确定循环次数，x可以不用
#     print("送玫瑰花")


# num = 125
# count = 0
# for x in range(1, num):  # x就相当于变化的num
#     if x % 2 == 0:
#         count += 1
# print(f"1~125(不含)中共有{count}个偶数")


# i = 1
# for i in range(1, 101):
#     print(f"今天是表白的第{i}天")
#     for j in range(1, 11):
#         print(f"送小妹的第{j}朵玫瑰花")
#     print("小妹，我喜欢你")
# print(f"坚持了{i}天，终于成功了")


# for i in range(1, 10):
#     j = 1
#     for j in range(1, i+1):
#         print(f"{j}*{i}={j * i}\t", end='')
#         j += 1
#     i += 1
#     print()


# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f"{j}*{i}={j * i}\t", end='')
# print()


 #  countine 针对所在循环起作用，for 和 while 通用，终止本次循环 1 22222 4
 #  break 针对所在循环起作用，for 和 while 通用，终止整个循环 1 2 4


# Salary = 1000
# i = 1
# for x in range(1, 21):
#     import random
#     KPI = random.randint(1, 10)
#     rest = 9000
#     while i <= 10:
#         if KPI > 5:
#             print(f"向员工{x}发放工资{Salary}元，账户余额为{rest}元")
#             rest = rest - i * 1000
#         else:
#             print(f"员工{x}，绩效分为{KPI}，不发工资，下一位")
#     if rest == 0:
#         break
# print("工资发完了，下个月领取吧！")


# total = 10000
# # 把总金额放到for循环外，由for循环控制，本该10够发10次，所以钱不够，就break终止for循环，就不用里面瞎嵌套while循环了，容易死循环
# for x in range(1, 21):
#     import random
#     KPI = random.randint(1, 10)
#     if KPI < 5:
#         print(f"员工{x}，绩效分为{KPI}，不发工资，下一位")
#         continue  # 绩效不够，下面的事情与这位员工无关了，所以用continue
#
#     if total >= 1000:  # 这不比定义i清晰明了？？ while在for里是个死循环
#         total -= 1000
#         print(f"向员工{x}发放工资1000元，账户余额为{total}元")
#     if total == 0:
#         print(f"余额不足，当前{total}元，工资发完了，下个月领取吧！")
#         break
#     # elif KPI < 5:
#     #     print(f"余额不足，当前{total}元，工资发完了，下个月领取吧！")
#     #     break  # 老师的18号员工绩效应该是>5的，好像有点bug
#     #     好像多余了！


# total = 10000
# # 把总金额放到for循环外，由for循环控制，本该10够发10次，所以钱不够，就break终止for循环，就不用里面瞎嵌套while循环了，容易死循环
# for x in range(1, 21):
#     import random
#     KPI = random.randint(1, 10)
#     if total == 0:
#         print(f"余额不足，当前{total}元，工资发完了，下个月领取吧！")
#         break
#     if KPI < 5:
#         print(f"员工{x}，绩效分为{KPI}，不发工资，下一位")
#         continue  # 绩效不够，下面的事情与这位员工无关了，所以用continue
#
#     if total >= 1000:  # 这不比定义i清晰明了？？ while在for里是个死循环
#         total -= 1000
#         print(f"向员工{x}发放工资1000元，账户余额为{total}元")
#         if total == 0:
#             if x == 20:
#                 print(f"余额不足，当前{total}元，工资发完了，下个月领取吧！")
#                 break  # 针对极端情况
#     else:
#         print(f"余额不足，当前{total}元，工资发完了，下个月领取吧！")
#         break






