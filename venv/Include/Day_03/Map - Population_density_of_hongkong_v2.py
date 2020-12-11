import pyecharts.options as opts
from pyecharts.charts import Map
from pyecharts.globals import ThemeType
data=[
    ['China',30],
    ['Canada',20],
    ['Russia',50],
    ['United States',90],
    ['Africa',70]
]
(
    Map(
        init_opts=opts.InitOpts(
            theme=ThemeType.CHALK
        )
    )
    .add(
        series_name='这是一个好名字',
        maptype='world',
        data_pair=data,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts()
    )
    .render('./picture/Map.html')
)