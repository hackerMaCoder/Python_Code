
# import time
# file = open("D:/test.txt", "r", encoding="utf-8")  # 扩展名也写上
# print(type(file))
# content = file.read(3)
# print(content)
# content = file.read()
# print(content)
# content = file.readlines()
# print(content)
# content = file.readline()
# print(f"content")
# content = file.readline()
# print(content)
# content = file.readline()
# print(content)
#
# for line in file:
#     print(line)
# time.sleep(20)
# file.close()
# with open("D:/test.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line)
#     file.close()


# count方法来统计
# count变量来统计
# f = open("D:/test.txt", "r", encoding="utf-8")
# count = 0  # 不要在循环里定义变量，统一放到最前边
# for line in f:
#     line = line.strip()
#     print(line)
#     words = line.split(" ")
#     for word in words:
#         if word == "asdl":
#             count += 1
# print(f"asdl的个数是{count}个")
# f.close()

# contents.strip() # 列表可没有strip方法

# print(contents)
# num = contents.count("a`sdl")
#
# print(f"asdl出现的次数是{num}次")


# f = open("D:/test.txt", "w", encoding="utf-8")
# f.write("itheima")
# f.flush()
# # f.close()  # close方法内置了flush功能

# f = open("D:/test.txt", "a", encoding="utf-8")
# f.write("\n黑马程序员")
# f.flush()


# fr = open("D:/chart", "r", encoding="utf-8")
# fw = open("D:/chart", "w", encoding="utf-8")
# for line in fr:
#     line.strip()
#     str = line.split(",")
#     if str[4] == "测试":
#         continue
#     else:
#         fw.write(line)
#         fw.write("\n")
# fr.close()
# fw.close()




