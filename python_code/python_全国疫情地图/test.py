
import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts
f = open("D:/疫情.txt", "r", encoding="utf-8")
data = f.read()
my_dict = json.loads(data)
province_data_list = my_dict["areaTree"][0]["children"]
f.close()
map_list = []
for province_data in province_data_list:
    # province_data 是每个省份的数据，作为children 列表中的一个元素，每个是一个字典
    province_name = province_data["name"] + "省"  # 细节啊！
    province_confirm = province_data["total"]["confirm"]
    map_list.append((province_name, province_confirm))
    # 不用写map_list =

map = Map()
map.add("各省份确诊人数", map_list, "china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图",pos_left="center", pos_bottom="1%"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "lable": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100~9999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000~4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000~99999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "lable": "10000~99999人", "color": "#CC3333"},
            {"min": 100000, "lable": "100000+", "color": "#990033"},
        ]
    )
)
map.render()

# 自治区，直辖市的数据显示不了吗？，因为名称不是以省结尾的？


