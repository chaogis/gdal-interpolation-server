#-*-coding=utf-8-*-
'''
Created on 2018年11月27日

@author: chao_qin
@description: 请求数据并进行预处理
'''

import os
import urllib.request
import simplejson
import json
from datetime import datetime
from datetime import timedelta
import traceback

from config import station_url
from config import realdata_url
from config import hourdata_url
from config import daydata_url
from config import monthdata_url
from config import output_bounds

from utils import get_absolute_path
from utils import write_content
from utils import format_time
from utils import format_file_name
from utils import get_des_by_time
from utils import format_yestoday
from utils import format_last_month
from utils import lnglat_2_webmercator
from utils import kill_out_of_range_val

def request_data(url, time_interval = 'hour', current_task_name = None):
    '''
        请求数据
        url--- 请求链接
        time_interval--- 时间尺度，real/hour/day/month
        current_task_name--- 当前任务名称
    '''
    try:
        return simplejson.loads(urllib.request.urlopen(url).read())
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() + ' [' + format_file_name(time_interval, current_task_name) + '] 请求数据异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, mode = 'a')


def get_url(time_interval = 'hour', current_task_name = None, history = False, sta_url = None, data_url = None):
    '''
        获取站点和监测数据请求url
        time_interval--- 时间尺度，real/hour/day/month
        current_task_name--- 当前任务名称
        history--- 是否为历史数据任务
        sta_url--- 站点数据url
        data_url--- 监测数据url
    '''

    try:
        # 站点数据请求url
        if sta_url is not None:
            local_station_url = sta_url
        else:
            local_station_url = station_url

        # 监测数据请求url
        if data_url is not None:
            local_data_url = data_url
        else:
            if time_interval == 'real':
                    local_data_url = realdata_url
            elif time_interval == 'hour':
                if current_task_name is not None:
                    local_data_url = hourdata_url.replace('{yyyy-mm-dd hh}', datetime.strptime(current_task_name,'%Y%m%d%H').strftime('%Y-%m-%d %H'))
                else:
                    local_data_url = hourdata_url.replace('{yyyy-mm-dd hh}', format_time('%Y-%m-%d %H'))
            elif time_interval == 'day':
                if current_task_name is not None:
                    local_data_url = daydata_url.replace('{yyyy-mm-dd}', datetime.strptime(current_task_name,'%Y%m%d').strftime('%Y-%m-%d'))
                else:
                    local_data_url = daydata_url.replace('{yyyy-mm-dd}', format_yestoday('%Y-%m-%d'))
            elif time_interval == 'month':
                if current_task_name is not None:
                    local_data_url = monthdata_url.replace('{yyyy-mm}', datetime.strptime(current_task_name,'%Y%m').strftime('%Y-%m'))
                else:
                    local_data_url = monthdata_url.replace('{yyyy-mm}', format_last_month('%Y-%m'))

        return [local_station_url, local_data_url.replace(' ', '%20')]
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() + ' [' + format_file_name(time_interval, current_task_name) + '] 获取站点和监测数据url异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, mode = 'a')

def struct_data(time_interval = 'hour', current_task_name = None, history = False, sta_url = None, data_url = None):
    '''
        将站点和数据进行挂接
        time_interval--- 时间尺度，real/hour/day/month
        current_task_name--- 当前任务名称
        history--- 是否为历史数据任务
        station_url--- 站点数据url
        data_url--- 监测数据url
    '''
    try:
        url = get_url(time_interval, current_task_name, history, sta_url, data_url)
        stations = request_data(url[0], time_interval, current_task_name)
        monitordatas = request_data(url[1], time_interval, current_task_name)

        features = stations['features']
        entries = monitordatas['entries']

        for feature in features:
            # 若输出范围为网络墨卡托投影坐标, 则将经纬度转网络墨卡托投影坐标
            if output_bounds[0] > 180 and output_bounds[1] > 90:
                coords = feature['geometry']['coordinates']
                feature['geometry']['coordinates'] = lnglat_2_webmercator(coords[0], coords[1])

            stationCode = feature['properties']['stationCode'].strip()
            for entry in entries:
                MN = entry['MN'].strip()
                if stationCode == MN:
                    feature['properties']['aqi'] = entry.get('V_AQI', -1)
                    feature['properties']['no2'] = entry.get('V_141', -1)
                    feature['properties']['pm25'] = entry.get('V_121', -1)
                    feature['properties']['o3'] = entry.get('V_108', -1)
                    feature['properties']['pm10'] = entry.get('V_107', -1)
                    feature['properties']['co'] = entry.get('V_106', -1)
                    feature['properties']['so2'] = entry.get('V_101', -1)
                    entries.remove(entry)

        return stations
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() + ' [' + format_file_name(time_interval, current_task_name) + '] 数据挂接异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, mode = 'a')


def write_structed_data(time_interval, current_task_name = None, history = False, station_url = None, data_url = None, use_history_temp = False):
    '''
        将geojson写入json文件
        time_interval--- 时间尺度，real/hour/day/month
        current_task_name--- 当前任务名称
        history--- 是否为历史数据任务
        station_url--- 站点数据url
        data_url--- 监测数据url
    '''
    try:
        content = struct_data(time_interval, current_task_name, history, station_url, data_url)
        file_path = get_absolute_path('json', time_interval = time_interval, current_task_name = current_task_name, use_history_temp = use_history_temp)
        write_content(file_path, content, 'json')
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() + ' [' + format_file_name(time_interval, current_task_name) + '] 写入GeoJSON异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, mode = 'a')


def start(time_interval = 'hour', current_task_name = None, history = False, station_url = None, data_url = None, use_history_temp = False):
    '''
        执行主方法
        time_interval--- 时间尺度，real/hour/day/month
        current_task_name--- 当前任务名称
        history--- 是否为历史数据任务
        station_url--- 站点数据url
        data_url--- 监测数据url
    '''
    write_structed_data(time_interval, current_task_name, history, station_url, data_url, use_history_temp)
    print(u'<<<<<<<<<<<<<<<<<<<<<<1. 写入', get_des_by_time(time_interval), u'GeoJSON完成>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


    '''
        程序入口
    '''
if __name__ =='__main__':
    print(u'>>>>>>>>>>>>数据预处理开始时间:', format_time(),'>>>>>>>>>>>>>>>>>>>>>>')
    start('real')
    print(u'>>>>>>>>>>>>数据预处理结束时间:', format_time(),'>>>>>>>>>>>>>>>>>>>>>>')
    print(u'>>>>>>>>>>>>数据预处理成功>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')