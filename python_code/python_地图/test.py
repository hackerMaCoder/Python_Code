from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()

data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("广东省 ", 499)
]

map.add("中国地图", data, "china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1, "max":9, "label":"1-9人", "color":"#CCFFFF"},
            {"min":10, "max":99, "label":"10-99人", "color":"#FFFF99"},
            {"min":100, "max":499, "label":"100-499人", "color":"#FF9966"},


        ])
)

map.render()

