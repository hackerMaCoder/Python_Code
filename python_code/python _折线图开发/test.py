from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

line = Line()
line.add_xaxis(["中国","美国","英国"])
#
#  尝试将 add_yaxis 方法中的整数列表改为包含数据点的列表
# 应为类型 'Sequence[LineItem | dict]'
line.add_yaxis("GDP", [500, 300, 200])


line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),  # 功能名之间用 , 隔开
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    # 最高才到100？？
)

line.render()


