#-*-coding=utf-8-*-
'''
Created on 2018年12月18日

@author: chao_qin
@description: 浙江嘉兴GDAL空间插值配置信息
'''

import os

# 数据接口域名
# domain = 'http://hzzhhb.net'
domain = 'http://agms-server'

# 颜色形式(rgb/16进制hex)
rgb_color = False

# 插值因子列表
z_fields = ['aqi', 'no2', 'pm25', 'o3', 'pm10', 'co', 'so2']

# 菏泽插值结果宽度和高度(3857)-像元大小约 500m
width = 223
height = 183

# 正常数据范围(左上、右下)
output_bounds = [120.301277, 31.026175, 121.265427, 30.320141]

# 出图模板文件名称
export_png_template = 'zjjx.png'

# 插值算法(点位多且分布均匀,不需平滑)
grid_algorithm = 'invdist:power=2:smoothing=0:radius1=0.0:radius2=0.0:angle=0.0:max_points=0:min_points=0:nodata=0.0'
# grid_algorithm = 'invdist:power=1.6:smoothing=0.0:radius1=0.0:radius2=0.0:angle=0.0:max_points=0:min_points=0:nodata=0.0'

# 请求数据url
station_url = domain + '/agms/web/outside/v1/interpolation/stations'
# 实时数据
realdata_url = domain + '/agms/web/outside/v1/interpolation/data'
# 指定小时获取小时数据
hourdata_url = domain + '/agms/web/outside/v1/interpolation/hour-data/{yyyy-mm-dd hh}'
# 指定日期获取日数据
daydata_url = domain + '/agms/web/outside/v1/interpolation/day-data/{yyyy-mm-dd}'
# 指定日期获取月数据
monthdata_url = domain + '/agms/web/outside/v1/interpolation/month-data/{yyyy-mm}'

# 当前工作空间
# base_dir = 'G:/InterpolationResult'
base_dir = os.path.join(os.getcwd(), 'interpolation_result_dir')

# png出图模板保存路径等
common_path = 'common'

# png图片保存位置(国控站点)
png_path = 'images'

# 日志文件保存位置
log_path = 'log'

# 临时文件保存位置，包括geojson、各因子tif等
temp_path = 'temp'

# 通过接口对历史数据/错误数据补插值临时文件保存位置
history_temp_path = 'history_temp'

# 小时数据各因子最大值
hour_max_range = {
    'aqi': 500,
    'pm25': 500,
    'pm10': 600,
    'no2': 3840,
    'o3': 1200,
    'co': 150,
    'so2': 800
}

# 日数据各因子最大值
day_max_range = {
    'aqi': 500,
    'pm25': 500,
    'pm10': 600,
    'no2': 940,
    'o3': 800,
    'co': 60,
    'so2': 2620
}