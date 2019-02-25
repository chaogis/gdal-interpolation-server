#-*-coding=utf-8-*-
'''
Created on 2018年11月27日

@author: chao_qin
@description:程序入口 - 设置定时程序
'''

import logging
logging.basicConfig()
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

import traceback

from datetime import datetime, timedelta

import structdata
import grid
import exportpng

from utils import write_content
from utils import get_absolute_path
from utils import get_file_directory
from utils import format_time
from utils import format_file_name
from utils import remove_files
from utils import mkdir_if_not_exist_once
from utils import del_dir_if_exist
from utils import format_specify_month

from history_hour_data_task import do_hour_task
from history_day_data_task import do_day_task
from history_month_data_task import do_month_task

def real_job():
    current_task_name = format_file_name('real')
    # 打印每次任务开始时间
    print(u'>>>>>>>>>>>>任务', current_task_name, u'开始时间: %s' % format_time(),'>>>>>>>>>>>>')
    structdata.start('real', current_task_name, False)
    grid.start('real', current_task_name)
    exportpng.start('real', current_task_name)
    remove_files(get_file_directory('tif'))
    print(u'>>>>>>>>>>>>>>>>>>>>完成时间: %s' % format_time(), '>>>>>>>>>>>>>>>>>>>>\n')

def hour_job():
    # 小时任务每次执行时,删除两小时之前的实时插值数据
    # del_dir_if_exist(get_file_directory('del'))
    current_task_name = format_file_name('hour')
    # 打印每次任务开始时间
    print(u'>>>>>>>>>>>>任务', current_task_name, u'开始时间: %s' % format_time(),'>>>>>>>>>>>>')
    structdata.start('hour', current_task_name, False)
    grid.start('hour', current_task_name)
    exportpng.start('hour', current_task_name)
    remove_files(get_file_directory('tif'))
    print(u'>>>>>>>>>>>>>>>>>>>>完成时间: %s' % format_time(), '>>>>>>>>>>>>>>>>>>>>\n')

def day_job():
    current_task_name = format_file_name('day')
    # 打印每次任务开始时间
    print(u'>>>>>>>>>>>>任务', current_task_name, u'开始时间: %s' % format_time(),'>>>>>>>>>>>>')
    structdata.start('day', current_task_name, False)
    grid.start('day', current_task_name)
    exportpng.start('day', current_task_name)
    remove_files(get_file_directory('tif'))
    print(u'>>>>>>>>>>>>>>>>>>>>完成时间: %s' % format_time(), '>>>>>>>>>>>>>>>>>>>>\n')

def month_job():
    current_task_name = format_file_name('month')
    # 打印每次任务开始时间
    print(u'>>>>>>>>>>>>任务', current_task_name, u'开始时间: %s' % format_time(),'>>>>>>>>>>>>')
    structdata.start('month', current_task_name, False)
    grid.start('month', current_task_name)
    exportpng.start('month', current_task_name)
    remove_files(get_file_directory('tif'))
    print(u'>>>>>>>>>>>>>>>>>>>>完成时间: %s' % format_time(), '>>>>>>>>>>>>>>>>>>>>\n')
    
def auto_make_play_data():
    '''
        自动生成播放功能涉及数据
        小时数据:距当前时间24小时之前
        日数据:距当前日期30天之前
        月数据:距当前时间12个月
    '''
    format = '%Y-%m-%d %H:%M:%S'
    str_24hour_ago = (datetime.now() + timedelta(hours=-24)).strftime(format)
    str_30day_ago = (datetime.now() + timedelta(days=-30)).strftime(format)
    str_12month_ago = (format_specify_month(datetime.now(), -12)).strftime(format)
    do_hour_task(str_24hour_ago, format_time())
    do_day_task(str_30day_ago, format_time())
    do_month_task(str_12month_ago, format_time())

if __name__ == '__main__':
    mkdir_if_not_exist_once()
    auto_make_play_data()
    executors = {
        'default': ProcessPoolExecutor(5),
        'processpool': ThreadPoolExecutor(20)
    }
    sched = BlockingScheduler(executors=executors)
    sched.add_job(real_job, 'cron', second ='1', max_instances=6, id='real_job_id', misfire_grace_time=10)
    sched.add_job(hour_job, 'cron', minute='55', second ='15', id='hour_job_id', misfire_grace_time=60)
    sched.add_job(day_job, 'cron', hour = '6', minute = '20', second ='30', id='day_job_id', misfire_grace_time=600)
    sched.add_job(month_job, 'cron', day = '1', hour = '2', minute = '30', second ='45', id='month_job_id', misfire_grace_time=600)
    try:
        print(u'>>>>>>>>>>>>>>当前时间: %s' % format_time(), u'等待执行任务>>>>>>>>>>>>>>')
        sched.start()
    except Exception:
        log = []
        log.append('>>>>>>>>>>定时任务异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        write_content(get_absolute_path('log'), log, 'a')
