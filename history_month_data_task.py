#-*-coding=utf-8-*-
'''
Created on 2018年12月17日

@author: chao_qin
@description:程序入口 - 对月历史数据插值
'''

import datetime
import traceback

import structdata
import grid
import exportpng

from utils import write_content
from utils import get_absolute_path
from utils import get_file_directory
from utils import format_time
from utils import format_file_name
from utils import remove_files
from utils import format_specify_month
from utils import mkdir_if_not_exist_once

str_start_time = '2017-11-01 00:00:00'
str_end_time = '2018-11-01 00:00:00'

def work(current_task_name, use_history_temp = False):
    structdata.start('month', current_task_name, True, use_history_temp = use_history_temp)
    grid.start('month', current_task_name, use_history_temp)
    exportpng.start('month', current_task_name, use_history_temp)
    remove_files(get_file_directory('tif', use_history_temp = use_history_temp))

def run_task(func, month=0, day=0, hour=0, min=0, second=0, start = None, end = None, use_history_temp = False):
    try:
        # 此处修改全局变量加关键字global
        global str_start_time
        global str_end_time
        
        if start is not None and end is not None:
            str_start_time = start
            str_end_time = end

        print(u'>>>>>>>>>>>>>>>>>开始时间:',format_time(),'>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        iter_next_time = start_time = datetime.datetime.strptime(str_start_time,'%Y-%m-%d %H:%M:%S')
        str_iter_next_time = str(iter_next_time)
        # 第一次任务名称
        task_name = start_time.strftime('%Y%m')

        while str_iter_next_time <= str_end_time:
            print(u'>>>>>>>>>>>>>>>>>开始任务', task_name, u'插值,', format_time(), '>>>>>>>>>>>')
            func(task_name, use_history_temp)
            print(u'>>>>>>>>>>>>>>>>>完成任务', task_name, u'插值,', format_time(), '>>>>>>>>>>>\n')
            iter_next_time = format_specify_month(iter_next_time, month)
            str_iter_next_time = iter_next_time.strftime('%Y-%m-%d %H:%M:%S')
            task_name = iter_next_time.strftime('%Y%m')
        print(u'>>>>>>>>>>>>>>>>>结束时间:',format_time(),'>>>>>>>>>>>>>>>>>>>>>>>>>\n')
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() +' 生成月历史数据任务[ ' + task_name  + u' ]插值异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, 'a')

def start():
    run_task(work, month = 1, use_history_temp = True)


# 根据起止时间执行月插值任务
def do_month_task(start_time, end_time, type = None, use_history_temp = False):
    if start_time is not None and end_time is not None:
        if start_time <= end_time:
            mkdir_if_not_exist_once()
            run_task(work, month = 1, start = start_time, end = end_time, use_history_temp = use_history_temp)
        else:
            print('>>>>>>>>>>>月插值任务:传入的时间有问题,结束时间应大于开始时间!')
    else:
        print('>>>>>>>>>>>月插值任务:传入的开始或结束时间为None!')


if __name__=='__main__':
    mkdir_if_not_exist_once()
    start()