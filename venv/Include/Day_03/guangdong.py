from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.faker import Faker
(
    Map(init_opts=opts.InitOpts(width='900px',height='600px'))
    .add(
        series_name='商家A',
        data_pair=[list(z) for z in zip(Faker.guangdong_city,Faker.values())],
        maptype='广东'
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-广东地图"),
        visualmap_opts=opts.VisualMapOpts()
    )
    .render('./picture/my_guangdong.html')
)