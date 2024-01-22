# my_tuple = ("cc", 3, 6, 7, 0)
#
# for element in my_tuple:
#     print(element)
#
# i = 0
# while i < len(my_tuple):
#     print(my_tuple[i])
#     i += 1


# my_tuple = (["asc", "asavcceqr"], 4, 4, 8, [1, 2, 3, 4])
# my_tuple[0][-1] = "uo" # 如果列表里的元素是整形的数字，不支持此修改，只能修改字符串
# print(my_tuple)


# t1 = ("周杰伦", 11, ["football", "music"])
# age_index = t1.index(11)
# name = t1[0]
# del t1[2][0]
# t1[2].append("coding") # 元组先通过下标，锁定到列表
# # ('周杰伦', 11, ['music', 'coding'])
#
# print(f"年龄下标是{age_index}，姓名是{name}，\n{t1}")




# str = "itheima and itcast"
# index = str.index("i")
# print(index)
#
# new_str = str.replace ("it", "程序")
# print(new_str)
#
# my_list = str.split("h") # 以"h"分，h就没有了，变成空格
# my_list = str.split("t")
# my_list = str.split(" ")
# print(my_list)
#
#
# str = "  itheima and itcast "
# new_str2 = str.strip()
# print(new_str2)


# str = "itheima itcast baoxuegu"
# num = str.count("it")
# print(f"有{num}个it字符")
# new_1 = str.replace(" ","|")
# print(f"新的字符串为：{new_1}")
# my_list = new_1.split("|") # 要想有效果，不是用str了，而是new_1,因为已经改过了
# print(f"得到列表为：{my_list}")


# 序列切片
# list = [1, 2, 3, 4, 5, 6]
# # new_list = list[0:3] # 正向
# new_list_1 = list[-1:-4:-1] #反向
# new_list = list[:2:-1]# 和上面是一样的效果
# print(new_list)
# # tuple = (1, 2, 3, 4, 5, 6)
# # new_tuple = tuple[2:5:2]
# # new_tuple_1 = tuple[::2]
# # print(new_tuple_1)
# # str = "123456"
# # new_1 = str[:4:2]
# # print(new_1)


# str = ("万过薪月，员序程马黑来，nohtyP学")
# list = str.split("，")
# new_str = list.pop(1).replace("来","")[::-1]
# print(new_str)


