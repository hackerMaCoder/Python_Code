# my_list = [[1,2,3],[4,5,6]]  # [1,2,3]是一个元素，[4,5,6]是一个元素
# print(my_list)
# print(type(my_list))
# # print(my_list[1])
# print(my_list[1][1])  # 5
# print(my_list[-2][1])  # 2
# print(my_list[-2][-1])  # 3


# my_list = ["itheima","itcast","python"]  # my_list是对象，index是方法
# index = my_list.index("python")
# print(f"\"python\"的下标值是{index}")
# my_list[0] = "adidas"
# print(my_list)
# my_list.insert(0,"sda")
# print(my_list)
# my_list.append(4)
# print(my_list)
# my_list2 = [1, 2, 3, 4]
# my_list.extend(my_list2)
# print(my_list)

# my_list = ["itheima","itcast","python"]
# del my_list[0]
# print(my_list)
# element = my_list.pop(0)
# print(f"剩余列表为{my_list}，取出的元素是{element}")


# my_list = ["itheima","itheima", "itcast","python"]
# count = my_list.count("itheima")
# print(count)
# my_list.remove("itheima")
# print(f"剩余列表为{my_list}")


# my_list.clear()
# print(my_list)





# my_list = ["itheima","itcast","python"]
# count = len(my_list)
# print(count)




# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def list_for_func():
#     for element in my_list:
#         print(f"{element}", end='')
# list_for_func()
# print()
# def list_while_func():
#     i = 0
#     num = len(my_list)
#     while i < num:
#         print(my_list[i], end='')
#         i += 1
# list_while_func()




my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_new = []
for element in my_list:
    if element % 2 == 0:
        my_list_new.append(element)
print(f"透过for循环，取出偶数元素，组成新列表：{my_list_new}")




my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_new = []

i = 0
while i < len(my_list):
    if my_list[i] % 2 == 0:
        my_list_new.append(my_list[i])
    i += 1


# i = 1
# while i < len(my_list):
#     my_list_new.append(my_list[i])
#     i +=2
print(f"透过while循环，取出偶数元素，组成新列表：{my_list_new}")


