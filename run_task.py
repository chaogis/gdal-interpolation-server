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

def hour_job():
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

if __name__ == '__main__':
    mkdir_if_not_exist_once()
    executors = {
        'default': ProcessPoolExecutor(5),
        'processpool': ThreadPoolExecutor(20)
    }
    sched = BlockingScheduler(executors=executors)
    sched.add_job(hour_job, 'cron', minute='50', id='hour_job_id', misfire_grace_time=60)
    sched.add_job(day_job, 'cron', hour = '2', minute = '20', id='day_job_id', misfire_grace_time=600)
    sched.add_job(month_job, 'cron', day = '1', hour = '3', minute = '20', id='month_job_id', misfire_grace_time=600)
    try:
        print(u'>>>>>>>>>>>>>>当前时间: %s' % format_time(), u'等待执行任务>>>>>>>>>>>>>>')
        sched.start()
    except Exception:
        log = []
        log.append('>>>>>>>>>>定时任务异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        write_content(get_absolute_path('log'), log, 'a')
