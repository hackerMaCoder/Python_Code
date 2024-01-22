# set = {2, 2, 2, 4, 5, 78, 4}
# print(f"set的内容是{set}，类型是{type(set)}")
# set的内容是{2, 4, 5, 78}，类型是<class 'set'>  去重


# set1 = {1, 2, 3}
# set2 = {1, 4, 5}
# # 取出集合1和集合2的差集（集合1有 而集合2没有的）
#
# set3 = set1.difference(set2)
# print(set3)
# # {2, 3}


# 我觉得这个名字”消除2个集合的差集“不大对，
# 应该是”在集合1中消除2个集合的交集“   来自B站弹幕
#在集合1里消除和集合2相同的元素

# set1.difference_update(set2)
# # 不产生新的集合，不用定义变量去接收
# print(set1)
# 不用定义set4了，因为set1被修改了，所以赋给新的set1，

# set1在前，最终变化的都是集合1里发生变化

# set1.union(set2)

# # 是可以的，wile(len(集合))然后用pop()，敲一下就知道了
# # 不能使用pop（）因为这样会改变集合本身，并不是遍历 来自B站弹幕
# for element in set1:
#     print(element)


# list(set)可以直接把集合转换成列表  来自B站评论
# list = list(set2)
# print(list)

# [1, 4, 5]


# my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客',
#     'itheima', 'itcast', 'itheima', 'itcast', 'best']
# set_empty = set()
# for element in my_list:
#     set_empty.add(element)
# print(set_empty)
#
# my_dict ={}
#
file = open("D:/test.txt", "r", encoding="UTF-8")
# with open("D:/test.txt", "r", encoding="UTF-8") as file:
    # for line in file:
    #     print(line)
    # file.read(3)#字节
    # file.readlines()



        

