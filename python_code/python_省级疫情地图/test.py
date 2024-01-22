
import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("D:/疫情.txt", "r", encoding="utf-8")
json_data = f.read()
dict_data = json.loads(json_data)
city_data_list = dict_data["areaTree"][0]["children"][3]["children"]   # 河南省
f.close()
map_list = []
for city_data in city_data_list:
    city_name = city_data["name"] + "市"
    city_confirm = city_data["total"]["confirm"]
    map_list.append((city_name, city_confirm))

map = Map()
map.add("河南省疫情地图", map_list,"河南")
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图", pos_left="center", pos_bottom="1%"),
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

map.render("河南省疫情地图.html")
