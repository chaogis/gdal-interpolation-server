#-*-coding=utf-8-*-
'''
Created on 2018年11月27日

@author: chao_qin
@description: 执行GDAL空间插值及投影变换
'''

import traceback
from osgeo import gdal

from config import z_fields
from config import width
from config import height
from config import output_bounds
from config import grid_algorithm

from utils import get_absolute_path
from utils import get_des_by_time
from utils import format_file_name
from utils import format_time
from utils import write_content
from utils import delete_if_exist
from utils import get_factor_max_val


def read_geojson(path, time_interval = 'hour', current_task_name = None):
    '''
        打开GeoJSON文件获取DataSet对象
        path--- geojson文件路径
        time_interval--- 时间尺度
        current_task_name--- 当前任务名称
    '''
    try:
        # gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "YES")
        return gdal.OpenEx(path)
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() + ' [' + format_file_name(time_interval, current_task_name) + '] 打开GeoJSON文件异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, mode = 'a')

def grid_option(factor_name, time_interval = 'hour', current_task_name = None):
    '''
        构造插值选项
        factor--- 插值因子名称
        time_interval--- 时间尺度
        current_task_name--- 当前任务名称
    '''
    try:
        max_val = get_factor_max_val(factor_name, time_interval)
        return gdal.GridOptions(options = [],
                                format = 'GTiff',
                                outputType = gdal.GDT_Float32,
                                width = width,
                                height = height,
                                creationOptions = None,
                                outputBounds = output_bounds,
                                outputSRS = 'EPSG:4326' if output_bounds[0] < 180 and output_bounds[1] < 90 else 'EPSG:3857',
                                noData = None,
                                algorithm = grid_algorithm,
                                layers = None,
                                SQLStatement = None,
                                where = '{} >= 0 and {} <= {}'.format(factor_name, factor_name, max_val),
                                spatFilter = None,
                                zfield = factor_name,
                                z_increase = None,
                                z_multiply = None,
                                callback = None,
                                callback_data = None
                                )
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() + ' [' + format_file_name(time_interval, current_task_name) + '] 构造插值选项异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, mode = 'a')


def do_grid(dest_name, dataset, grid_opt, time_interval = 'hour', current_task_name = None):
    '''
        执行空间插值
        dest_name--- 插值结果保存路径
        dataset--- 用于插值的dataset对象
        grid_opt--- 插值配置信息
        time_interval--- 时间尺度
        current_task_name--- 当前任务名称
    '''
    try:
        gdal.Grid(dest_name, dataset, options = grid_opt)
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() + ' [' + format_file_name(time_interval, current_task_name) + '] 构造插值选项异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, mode = 'a')

def start(time_interval = 'hour', current_task_name = None, use_history_temp = False):
    '''
        执行主方法
        time_interval--- 时间尺度
        current_task_name--- 当前任务名称
    '''
    path = get_absolute_path('json', time_interval = time_interval, current_task_name = current_task_name, use_history_temp = use_history_temp)
    dataset = read_geojson(path, time_interval, current_task_name)
    for z_field in z_fields:
        grid_opt = grid_option(z_field, time_interval, current_task_name)
        dest_name = get_absolute_path('tif', z_field, time_interval, current_task_name, use_history_temp)
        delete_if_exist(dest_name)
        do_grid(dest_name, dataset, grid_opt, time_interval, current_task_name)
    print(u'<<<<<<<<<<<<<<<<<<<<<<<<<2. ' + get_des_by_time(time_interval) + u' GDAL空间插值完成>>>>>>>>>>>>>>>>>>>>>>>>>')
    
'''
    程序入口
'''
if __name__ =='__main__':
    print(u'>>>>>>>>>>>>>>>插值开始时间:', format_time(),'>>>>>>>>>>>>>>>>>>>>>>>>>')
    start('real', '201812191641')
    print(u'>>>>>>>>>>>>>>>插值结束时间:', format_time(),'>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(u'>>>>>>>>>>>>>>>插值成功>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')