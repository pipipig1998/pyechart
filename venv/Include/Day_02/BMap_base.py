from pyecharts import options as opts
from pyecharts.charts import BMap
from pyecharts.faker import Faker
(
    BMap(init_opts=opts.InitOpts(width='900px',height='600px'))
    .add(
        series_name='虚假数据',
        data_pair=[list(z) for z in zip(Faker.provinces,Faker.values())],
        label_opts=opts.LabelOpts(formatter='{b}')
    )
    .add_schema(
        baidu_ak='P7TXy8G74PrSxmfq0L0DQ6raaN38yOWG',
        center=[120.13066322374, 30.240018034923]
    )
    .set_global_opts(title_opts=opts.TitleOpts(title='例子'))
    .render('my_base.html')
)