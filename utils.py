#-*-coding=utf-8-*-
'''
Created on 2018年11月13日

@author: chao_qin
@description:公共方法
'''

import os
import struct
import json
import shutil
import math

from datetime import datetime
from datetime import timedelta

from config import rgb_color
from config import base_dir
from config import png_path
from config import common_path
from config import temp_path
from config import log_path
from config import hour_max_range
from config import day_max_range
from config import history_temp_path

from colors.range60 import colors
from colors.range60 import aqi
from colors.range60 import pm10
from colors.range60 import pm25
from colors.range60 import hour_co
from colors.range60 import hour_no2
from colors.range60 import hour_o3
from colors.range60 import hour_so2
from colors.range60 import day_co
from colors.range60 import day_no2
from colors.range60 import day_o3
from colors.range60 import day_so2


def hex2rgb(hex_str):
    '''
        16进制颜色转换为 RGB
        hex_str--- 16进制颜色字符串
    '''

    int_tuple = struct.unpack('BBB', bytes.fromhex(hex_str))    
    return tuple([val for val in int_tuple])  

def get_color(factor_name, val, time_interval):
    '''
        根据因子值获取对应的颜色
        factor_name--- 因子名称
        val--- 因子值
        time_interval--- 时间尺度，real/hour/day/month
    '''

    factor_ranges = aqi
    if factor_name == 'aqi':
        factor_ranges = aqi
    elif factor_name == 'pm25':
        factor_ranges = pm25
    elif factor_name == 'pm10':
        factor_ranges = pm10
    elif factor_name == 'co':
        factor_ranges = day_co if time_interval == 'day' or time_interval == 'month' else hour_co
    elif factor_name == 'no2':
        factor_ranges = day_no2 if time_interval == 'day' or time_interval == 'month' else hour_no2
    elif factor_name == 'o3':
        factor_ranges = day_o3 if time_interval == 'day' or time_interval == 'month' else hour_o3
    elif factor_name == 'so2':
        factor_ranges = day_so2 if time_interval == 'day' or time_interval == 'month' else hour_so2

    for factor_range in factor_ranges:
        if val >= factor_range[0] and val <= factor_range[1]:
            index = factor_ranges.index(factor_range)
            if rgb_color:
                return colors[index]
            else:
                return hex2rgb(colors[index][1:])

def write_content(file_path, content, file_type = 'txt', mode = 'w'):
    '''
        文本内容写入
        file_path--- 写入文件路径
        content--- 写入内容
        file_type--- 文件格式, 默认为txt, 其他包括json
        mode--- 文件打开模式
    '''

    with open(file_path, mode) as f:
        if file_type == 'txt':
            f.writelines(content)
        elif file_type == 'json':
            json.dump(content, f)
        f.flush()
        f.close()

def remove_files(dir_path):
    '''
        删除给定目录中的所有文件
        dir_path--- 待删除文件的目录
    '''

    if os.path.exists(dir_path):
        file_list=os.listdir(dir_path)
        for f in file_list:
            file_path = os.path.join(dir_path, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path, True)
    else:
        print(u'>>>>>>>>>>目录', dir_path, u'不存在！>>>>>>>>>>')


def delete_if_exist(file_path):
    '''
        文件若存在则删除
        file_path--- 待删除文件路径
    '''

    if os.path.exists(file_path):
        os.remove(file_path)
    # else:
        # print u'>>>>>>>>>>文件', file_path, u'不存在！>>>>>>>>>>'

def make_dir_if_not_exist(path):
    '''
        目录不存在则创建
        path--- 带创建的目录地址
    '''

    if not os.path.exists(path):
        os.makedirs(path)

def get_des_by_time(type = 'hour'):
    '''
        根据时间尺度类型获取对应中文说明
        type--- 时间尺度, 包括以下类型
            real: 实时
            hour: 小时
            day: 日度
            month:  月度
    '''

    if type == 'hour':
        return u'小时'
    elif type == 'day':
        return u'日度'
    elif type == 'month':
        return u'月度'
    elif type == 'real':
        return u'实时'

def format_time(format = '%Y-%m-%d %H:%M:%S'):
    '''
        获取当前时间
        format--- 时间格式, 默认YYYY-MM-DD HH:MM:SS格式
    '''
    return datetime.now().strftime(format)


def format_yestoday(format = '%Y-%m-%d', date = None):
    '''
        根据当前日期或给定日期构造前一天的日期格式
        format--- 日期格式, 默认为 YYYY-MM-DD 形式
        date--- 给定日期
    '''

    if date is None:
        return (datetime.now() + timedelta(days=-1)).strftime(format)
    else:
        return (datetime.strptime(date,'%Y%m%d') + timedelta(days=-1)).strftime(format)

def padd_zero(num):
    '''
        小于10的数字左侧补0
        num--- 待补位数字
    '''
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)

def format_specify_month(iter_time, month_interval = 1):
    '''
        构造指定月份间隔的时间
        iter_time--- '%Y-%m-%d %H:%M:%S'格式时间
        month--- 月份间隔
        返回值: '%Y-%m-%d %H:%M:%S'格式下个月时间
    '''
    str_iter_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
    time_split = str_iter_time.split('-')
    year = int(time_split[0])
    month = int(time_split[1])
    next_month = month + month_interval

   # 后续年份
    if next_month >= 13:
        year = year + next_month // 12
        next_month = next_month % 12
    # 前面年份
    elif next_month <= 0:
        year = year - (abs(next_month) // 12 + 1)
        next_month = 12 - abs(next_month) % 12
    
    # 对二月份单独进行处理(若day >= 29,将其处理成28)
    day_time = time_split[2].split(' ')
    day = int(day_time[0])
    if next_month == 2:
        if day >= 29:
            day = 28

    #月度间隔后的时间
    str_next_month = str(year) + '-' + padd_zero(next_month) + '-' + str(day) + ' ' + day_time[1]

    return datetime.strptime(str_next_month,'%Y-%m-%d %H:%M:%S')

def format_last_month(format = '%Y-%m', date = None):
    '''
        构造上个月同期的日期, 数据请求时使用, YYYY-MM 形式
        format--- 日期格式, 默认为 YYYY-MM-DD 形式
        date--- 给定日期, 字符串形式
    '''
    if date is None:
        return format_specify_month(datetime.strptime(format_time(),'%Y-%m-%d %H:%M:%S'), -1).strftime(format)
    else:
        return format_specify_month(datetime.strptime(date,'%Y%m%d %H:%M:%S'), -1).strftime(format)


def format_file_name(time_interval = 'hour', current_task_name = None):
    '''
        构造文件名称, 分为根据任务名称和当前日期/小时/时间构造, 实时-YYYYMMDDHHMM 小时-YYYYMMDDHH 天-YYYYMMDD 月-YYYYMM
        time_interval--- real, hour, day, month
        current_task_name--- 当前任务名称, 依次为 YYYYMMDDHHMM/YYYYMMDDHH/YYYYMMDD/YYYYMM 格式
    '''
    if current_task_name is not None:
        return current_task_name
    else:
        if time_interval == 'hour':
            return format_time('%Y%m%d%H')
        elif time_interval == 'day':
            return format_yestoday('%Y%m%d')
        elif time_interval == 'month':
            return format_last_month('%Y%m')
        elif time_interval == 'real':
            return format_time('%Y%m%d%H%M')

def format_png_path(time_interval, current_task_name = None):
    '''
        构造png图片路径
        time_interval--- 时间尺度
        current_task_name--- 当前任务名称
    '''

    if current_task_name is not None: 
        if time_interval == 'hour':
            return datetime.strptime(current_task_name,'%Y%m%d%H').strftime('%Y/%m/%d')
        elif time_interval == 'day':
            return datetime.strptime(current_task_name,'%Y%m%d').strftime('%Y/%m/%d')
        elif time_interval == 'month':
            return datetime.strptime(current_task_name,'%Y%m').strftime('%Y/%m')
        elif time_interval == 'real':
            return datetime.strptime(current_task_name,'%Y%m%d%H%M').strftime('%Y/%m/%d')
    else:
        # 待定实时插值结果的保存路径
        if time_interval == 'hour' or time_interval == 'real':
            return format_time('%Y/%m/%d')
        elif time_interval == 'day':
            return format_yestoday('%Y/%m/%d')
        elif time_interval == 'month':
            return format_last_month('%Y/%m')

def get_file_name(file_type, factor = 'aqi', time_interval = 'hour', current_task_name = None, template_name = 'state'):
    '''
        根据文件类型、因子名称、时间尺度、任务名称获取文件名, 文件名格式如下:
            2018111409.json
            aqi_2018111409.tif
            so2_2018111409.tif
            aqi_2018111319.png
            so2_2018111319.png
            aqi_201812171501.png
            20181114.log
        file_type--- json, tif, png, log
        factor--- aqi, no2, pm25, o3, pm10, co, so2
        time_interval--- real, hour, day, month
        current_task_name--- 当前任务名称, 依次为 YYYYMMDDHHMM/YYYYMMDDHH/YYYYMMDD/YYYYMM 格式
        template_name--- 模板名称
    '''
    file_name = format_file_name(time_interval, current_task_name) + '.' + file_type
    if file_type == 'png' or file_type == 'tif':
        file_name = factor + '_' + format_file_name(time_interval, current_task_name) + '.' + file_type
    elif file_type == 'log':
        file_name = format_time('%Y%m%d') + '.' + file_type
    elif file_type == 'template':
        file_name = template_name + '.png'

    return file_name

def get_file_directory(type, time_interval = 'hour', current_task_name = None, template_name = 'state', use_history_temp = False):
    '''
        获取文件目录
        type--- 文件类型
        time_interval--- 时间尺度
        current_task_name--- 任务名称
        template_name--- 模板名称(确定存储目录)
    '''
    relative_path = temp_path
    if type == 'template':
        relative_path = common_path
    elif type == 'png':
        relative_path = os.path.join(png_path, template_name, format_png_path(time_interval, current_task_name))
    elif type == 'log':
        relative_path = log_path
    elif type == 'json' or type == 'tif':
        relative_path = temp_path if use_history_temp == False else history_temp_path
    
    # 对png图片, 若路径不存在则创建之
    if type == 'png':
        make_dir_if_not_exist(os.path.join(base_dir, relative_path))

    return os.path.join(base_dir, relative_path)

def get_absolute_path(file_type, factor = 'aqi', time_interval = 'hour', current_task_name = None, template_name = 'state', use_history_temp = False):
    '''
        根据类型获取文件绝对路径
        file_type--- 文件类型
        factor--- 因子名称
        time_interval--- 时间尺度
        current_task_name--- 任务名称
        template_name--- 模板名称(确定存储路径)
        use_history_temp--- 是否使用历史数据临时文件夹
    '''
    file_dir = get_file_directory(file_type, time_interval, current_task_name, template_name, use_history_temp)
    file_name = get_file_name(file_type, factor, time_interval, current_task_name, template_name)
    return os.path.join(file_dir, file_name)


def lnglat_2_webmercator(lng, lat):
    '''
        经纬度转网络墨卡托投影坐标
        lng--- 经度
        lat--- 纬度
        参数：[114.32894, 30.585748]
        返回值：[12727039.383734727, 3579066.6894065146]
    '''
    earthRad = 6378137.0
    x = lng * math.pi / 180 * earthRad
    a = lat * math.pi / 180
    y = earthRad / 2 * math.log((1.0 + math.sin(a)) / (1.0 - math.sin(a)))
    return [x, y]

def mkdir_if_not_exist_once():
    '''
        在初始化时执行一次创建目录的操作(若不存在)
    '''
    make_dir_if_not_exist(os.path.join(base_dir, common_path))
    make_dir_if_not_exist(os.path.join(base_dir, png_path))
    make_dir_if_not_exist(os.path.join(base_dir, log_path))
    make_dir_if_not_exist(os.path.join(base_dir, temp_path))
    make_dir_if_not_exist(os.path.join(base_dir, history_temp_path))

def kill_out_of_range_val(val, factor_name = 'aqi', time_interval = 'hour'):
    '''
        处理超限的监测值, 若超限则处理成最大值
        val--- 监测值
        factor_name--- 因子名称
        time_interval--- 时间尺度
    '''
    if val is not None:
        max_range = hour_max_range
        if time_interval == 'day' or time_interval == 'month':
            max_range = day_max_range

        if val > max_range[factor_name]:
            val = max_range[factor_name]
    else:
        val = -1

    return val

def get_factor_max_val(factor_name = 'aqi', time_interval = 'hour'):
    '''
        获取因子允许最大值
        factor_name--- 因子名称
        time_interval--- 时间尺度
    '''
    max_range = hour_max_range
    if time_interval == 'day' or time_interval == 'month':
            max_range = day_max_range

    return max_range[factor_name]
    
def make_dir_by_date(str_date):
    if str_date is not None:
        if len(str_date) == 6:
            return str_date[0:4] + '/' + str_date[4:6]
        elif len(str_date) == 8  or  len(str_date) == 10:
            return str_date[0:4] + '/' + str_date[4:6] + '/' + str_date[6:8]
        elif len(str_date) == 12:
            return str_date[0:4] + '/' + str_date[4:6] + '/' + str_date[6:8] + '/' + str_date[8:10]
        else:
            return '传入的文件名称格式有误'
    else:
        return '传入的日期/时间字符串为null'