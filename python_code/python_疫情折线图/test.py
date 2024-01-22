import json
from pyecharts. charts import Line
from pyecharts.options import TitleOpts , LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts

with open("D:/美国.txt", "r", encoding="utf-8") as f_us:
    data_us = f_us.read()
    data_us = data_us.replace("jsonp_1629344292311_69436(", "")  # 空字符串相当于删掉
    data_us = data_us[: -2]
    # json 转 python
    dict = json.loads(data_us)
    trend_data = dict["data"][0]["trend"]
    # x轴数据
    # 取到2020年12.31号
    us_x_data = trend_data["updateDate"][:314]
    us_y_data = trend_data["list"][0]["data"][:314]


with open("D:/日本.txt", "r", encoding="utf-8") as f_jp:
    data_jp = f_jp.read()
    data_jp = data_jp.replace("jsonp_1629350871167_29498(", "")  # 空字符串相当于删掉
    data_jp = data_jp[: -2]
    # json 转 python
    dict = json.loads(data_jp)
    trend_data = dict["data"][0]["trend"]
    # x轴数据
    # 取到2020年12.31号
    jp_x_data = trend_data["updateDate"][:314]
    jp_y_data = trend_data["list"][0]["data"][:314]


with open("D:/印度.txt", "r", encoding="utf-8") as f_in:
    data_in = f_in.read()
    data_in = data_in.replace("jsonp_1629350745930_63180(", "")  # 空字符串相当于删掉
    data_in = data_in[: -2]
    # json 转 python
    dict = json.loads(data_in)
    trend_data = dict["data"][0]["trend"]
    # x轴数据
    # 取到2020年12.31号
    in_x_data = trend_data["updateDate"][:314]
    in_y_data = trend_data["list"][0]["data"][:314]

line = Line()   # 创建图表对象
# x轴
line.add_xaxis(in_x_data)
# y轴
line.add_yaxis("美国确诊", us_y_data)
line.add_yaxis("日本确诊", jp_y_data)
line.add_yaxis("印度确诊", in_y_data)

line.set_global_opts(
    title_opts = TitleOpts(title="美日印三国确诊人数统计表", pos_left="center", pos_bottom="1%"),
   legend_opts = LegendOpts(is_show=True),
   toolbox_opts = ToolboxOpts(is_show=True),
   visualmap_opts = VisualMapOpts(is_show=True)
)

line.set_series_opts(
label_opts = LabelOpts(is_show=False)
)

line.render()












