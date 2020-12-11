from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
# 直方图
# x_data=["水笔","铅笔","钢笔","圆珠笔"]
# y_data = [40,30,98,42]
# bar=(
#     Bar()
#     .add_xaxis(x_data)
#     .add_yaxis('笔类',y_data)
# )
# make_snapshot(snapshot,bar.render(),'./picture/02.png')

# 折线图
# x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu'] # x轴数据
# # y_data = [123, 153, 89, 107, 98, 23] # y轴数据
# # line=(
# #     Line()
# #     .add_xaxis(x_data)
# #     .add_yaxis('手机',y_data)
# # )
# # make_snapshot(snapshot,line.render(),'./picture/03.png')

# 散点图
# x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu'] # x轴数据
# y_data = [123, 153, 89, 107, 98, 23] # y轴数据
# scatter=(
#     Scatter()
#     # 必须先X后Y，要不报错
#     .add_xaxis(x_data)
#     .add_yaxis('手机',y_data)
# )
# make_snapshot(snapshot,scatter.render(),'./picture/04.png')

# 饼图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu'] # x轴数据
y_data = [123, 153, 89, 107, 98, 23] # y轴数据
pie=(
    Pie()
    .add('',[list(z) for z in zip(x_data,y_data)])
)
make_snapshot(snapshot,pie.render(),'./picture/05.png')