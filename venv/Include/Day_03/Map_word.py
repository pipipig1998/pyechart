from pyecharts.charts import Map
import pyecharts.options as opts
from pyecharts.faker import Faker
(
    Map()
    .add('商家A',[list(z)for z in zip(Faker.country,Faker.values())],'world')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title='世界地图'),
        visualmap_opts=opts.VisualMapOpts(max_=200)
    )
    .render('./picture/Map_word.html')
)
l=[list(z)for z in zip(Faker.country,Faker.values())]
print(l)