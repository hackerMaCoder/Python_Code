# my_list = [["a",55], ["b", 11], ["c", 33]]
# def choose_sort_key(element):
#     return element[1]
# # my_list.sort(key=choose_sort_key,reverse=True)
# my_list.sort(key=lambda element:element[1])
# print(my_list)


from pyecharts.charts import Timeline,Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

f = open("D:/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
# 文件是一个列表
data_lines = f.readlines()
f.close()

# 删除第一行的表头
data_lines.pop(0)
dict_data = {}
for data_line in data_lines:
    year = int(data_line.split(",")[0])
    all_name = data_line.split(",")[1]
    # 涉及到科学计数法，转成float类型就变成数字了，以亿为单位，/1 0000 0000
    # country_gdp = float(data_line.split(",")[2]) / 100000000,还没到画图这一步 先不用处理，先取就行
    all_gdp = float(data_line.split(",")[2])
    # 封装成{key：[[country_name, country_gdp],key:[],……]}
    # 第一次封装的时候可能没有key，就会出现异常
    try:
        year_data = dict_data[year].append([all_name, all_gdp])
    except KeyError:
        dict_data[year] = []  # 先构建出{year:[]}
        dict_data[year].append([all_name, all_gdp])


# 先把字典数据的year key 按年份排序
keys = dict_data.keys()
sorted_year_list = sorted(keys)
timeline = Timeline({"theme":ThemeType.LIGHT})
for year in sorted_year_list:
    dict_data[year].sort(key=lambda element: element[1],reverse=True)
    year_data = dict_data[year][0:8]
    x_data = []
    y_data = []
    # year_data = [[country_data],[country_data]……]
    for country_data in year_data:
        x_data.append(country_data[0])
        y_data.append(country_data[1]/100000000)
        # 就往x.y轴上添加数据时，套一个for循环，下面的代码跳出去

    bar = Bar()
    #在传入之前反转x y 轴的数据
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)",y_data,label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}全球GDP前八的国家")
    )
    # 至此，时间线上一个点的数据图标画完了，下面循环生成1960-2019年的所有图表


    # timeline.add(bar, year),错误，year 为int型，按照timeline的语法需转成str类型
    timeline.add(bar, str(year))

timeline.add_schema(
    play_interval=500,  # 500 ms
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

timeline.render("1960-2019全球GDP前八国家的数据统计.html")
















