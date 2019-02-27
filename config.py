#-*-coding=utf-8-*-
'''
Created on 2018年11月27日

@author: chao_qin
@description: GDAL空间插值配置信息
'''

import os

# 颜色形式(rgb/16进制hex)
rgb_color = False

# 插值因子列表
z_fields = ['aqi', 'no2', 'pm25', 'o3', 'pm10', 'co', 'so2']

# 全国插值结果宽度和高度(3857)
width = 1091
height = 800

# 插值结果输出范围(3857,左上、右下)
output_bounds = [8176078.187514, 7086793.365356, 15036953.326737, 2056389.759979]

# 出图模板文件名称
dict_template_name = {'state': '中国',
                       'ah': '安徽',
                       'bj': '北京',
                       'cq': '重庆',
                       'fj': '福建',
                       'gd': '广东',
                       'gs': '甘肃',
                       'gx': '广西',
                       'gz': '贵州',
                       'ha': '河南',
                       'hb': '湖北',
                       'he': '河北',
                       'hi': '海南',
                       'hl': '黑龙',
                       'hn': '湖南',
                       'jl': '吉林',
                       'js': '江苏',
                       'jx': '江西',
                       'ln': '辽宁',
                       'nm': '内蒙',
                       'nx': '宁夏',
                       'qh': '青海',
                       'sc': '四川',
                       'sd': '山东',
                       'sh': '上海',
                       'sn': '陕西',
                       'sx': '山西',
                       'tj': '天津',
                       'tw': '台湾',
                       'xj': '新疆',
                       'xz': '西藏',
                       'yn': '云南',
                       'zj': '浙江'}

# 插值算法
grid_algorithm = 'invdist:power=3.6:smoothing=0.2:radius1=0.0:radius2=0.0:angle=0.0:max_points=0:min_points=0:nodata=0.0'
# grid_algorithm = 'invdist:power=2.0:smoothing=0.0:radius1=0.0:radius2=0.0:angle=0.0:max_points=0:min_points=0:nodata=0.0'

# 请求数据url
state_station_url = 'http://yun.fpi-inc.site/fpi-basemap-server/api/v1/stations'
# 小时最新数据
state_hourdata_recent_url = 'http://yun.fpi-inc.site/scas/api/v1.0/stations/hour-data/recent'
# 指定小时获取小时数据
state_hourdata_url = 'http://yun.fpi-inc.site/scas/api/v1.0/stations/hour-data/{yyyy-mm-dd hh}'
# 指定日期获取日数据
state_daydata_url = 'http://yun.fpi-inc.site/scas/api/v1.0/stations/day-data/{yyyy-mm-dd}'
# 制定日期获取月数据
state_monthdata_url = 'http://yun.fpi-inc.site/scas/api/v1.0/stations/month-data/{yyyy-mm}'

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