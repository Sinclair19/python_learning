import csv
import plotly.express as px
import pandas as pd

filename = "mapping_global_data_sets/data/world_fires_1_day.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lons_index = header_row.index('longitude')
    lats_index = header_row.index('latitude')
    bri_index =header_row.index('brightness')

    lons, lats, bri = [], [], []
    for row in reader:
        lons.append(float(row[lons_index]))
        lats.append(float(row[lats_index]))
        bri.append(float(row[bri_index]))

data = pd.DataFrame(
    data=zip(lons, lats, bri), columns=['经度', '纬度', '强度']
)

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=1200,
    height=800,
    title='全球火灾散点图',
    size='强度',
    size_max=15,
    color='强度',
    hover_name='强度',
)
fig.write_html('global_fires.html')
