from pyecharts.charts import BMap
from pyecharts.faker import Faker
from pyecharts import options as opts
(
    BMap(init_opts=opts.InitOpts(
        width='900px',
        height='600px',
        page_title='热力图',
        )
    )
    .add(
        series_name='热力图',
        data_pair=[list(z) for z in zip(Faker.provinces,Faker.values())],
        type_='heatmap'
    )
    .add_schema(
        baidu_ak='P7TXy8G74PrSxmfq0L0DQ6raaN38yOWG',
        center=[120.13066322374, 30.240018034923],
        zoom=5,
        is_roam=True
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="BMap-热力图"), visualmap_opts=opts.VisualMapOpts()
    )
    .render('./picture/my_heat_map.html')
)
print([list(z) for z in zip(Faker.provinces,Faker.values())])