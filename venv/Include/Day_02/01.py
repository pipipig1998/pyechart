from pyecharts.charts import Bar
from pyecharts import options as ops
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts.globals import ThemeType
# （1）传统建立
# bar=Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# # 也可以传入路径参数，如 bar.render("mycharts.html")
# bar.render('fist_chart.html')

# （2）链式建立
# bar=(
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# )
# bar.render('first_chart.html')

# 渲染图片
# bar=(
#     Bar(init_opts=ops.InitOpts(theme=ThemeType.LIGHT))
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#     .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
#     .add_yaxis("商家C", [15, 6, 45, 20, 35, 66])
# )
# bar.set_global_opts(title_opts=ops.TitleOpts(title='主标题',subtitle='副标题'))
# # 变成网页显示
# # bar.render('1.html')
# # 渲染成图片
# make_snapshot(snapshot,bar.render(),'bar.png')

