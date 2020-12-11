from pyecharts.charts import Map
import pyecharts.options as opts
from pyecharts.faker import Faker
(
    Map()
    .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-VisualMap（分段型）"),
        visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
    )
    .render("./picture/map_visualmap_piecewise.html")
)