import pyecharts.options as opts
from pyecharts.charts import Bar,Grid
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker
c = (
    Bar({"theme": ThemeType.MACARONS})
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .set_global_opts(
        title_opts={"text": "Bar-通过 dict 进行配置", "subtext": "我也是通过 dict 进行配置的"}
    )
)
grid=(
    Grid()
    .add(c,grid_opts=opts.GridOpts(pos_bottom="60%"))
    .render("bar_base_dict_config.html")
)