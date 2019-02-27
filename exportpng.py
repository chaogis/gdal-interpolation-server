#-*-coding=utf-8-*-
'''
Created on 2018年11月27日

@author: chao_qin
@description: 输出png图片
'''
import traceback
from copy import deepcopy
from osgeo import gdal
from PIL import Image

from config import z_fields
from config import dict_template_name

from utils import get_des_by_time
from utils import get_color
from utils import get_absolute_path
from utils import write_content
from utils import format_time
from utils import format_file_name
from utils import delete_if_exist

def open_template_png(time_interval = 'hour', current_task_name = None, template_name = 'state'):
    '''
        打开模板png图像
        time_interval--- 时间尺度
        current_task_name--- 当前任务名称
        template_name--- 裁剪模板名称
    '''

    try:
        path = get_absolute_path('template', template_name = template_name)
        img = Image.open(path)

        return img
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() + ' ' + dict_template_name[template_name] + ' [' + format_file_name(time_interval, current_task_name) + '] 读取出图模板PNG异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, mode = 'a')

def read_tif_data(path, time_interval = 'hour', current_task_name = None):
    '''
        读取插值因子影像数据
        path--- tif影像路径
        time_interval--- 时间尺度
        current_task_name--- 当前任务名称
    '''

    try:
        in_ds = gdal.Open(path)
        in_band = in_ds.GetRasterBand(1)
        in_data = in_band.ReadAsArray()

        return in_data
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() + ' [' + format_file_name(time_interval, current_task_name) + '] GDAL读取TIF异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, mode = 'a')

def read_tif_data_by_img(path, time_interval = 'hour', current_task_name = None):
    '''
        读取插值因子影像数据
        path--- tif影像路径
        time_interval--- 时间尺度
        current_task_name--- 当前任务名称
    '''

    try:
        img = Image.open(path)

        return img
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() + ' [' + format_file_name(time_interval, current_task_name) + '] PIL-Image读取TIF异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, mode = 'a')

def export_png(template_img, factor_name, factor_data, time_interval = 'hour', current_task_name = None, template_name = 'state'):
    '''
        执行导出png的操作
        template_img--- 模板png影像数据
        factor_name--- 插值因子名称
        factor_data--- 插值因子tif数据(二维数组)
        time_interval--- 时间尺度
        current_task_name--- 当前任务名称
        template_name--- 模板名称(以此确定存储路径)
    '''

    try:
        # 深拷贝一份模板图像
        img = deepcopy(template_img)
        width = img.size[0] # 967
        height = img.size[1] # 707

        # 遍历所有长度的点(宽度)
        for i in range(0, width):
            # 遍历所有宽度的点(高度)
            for j in range(0, height):
                # 打印图像对应位置的RGBA值
                data = (img.getpixel((i, j)))
                # 对透明度不为0的区域进行处理
                if  data[0] != 0 and data[1] != 0:
                    # factor_value = factor_data[j, i]
                    # 用PIL - Image getpixel方式获取像元值
                    factor_value = factor_data.getpixel((i, j))
                    factor_color = get_color(factor_name, factor_value, time_interval)
                    if factor_color is not None:
                        # 给图片赋予颜色
                        img.putpixel((i, j), (factor_color[0], factor_color[1], factor_color[2], 255)) 
                    else:
                        # tif中NoData部分设置为透明
                        img.putpixel((i, j), (255, 255, 255, 0))
                else:
                    # 背景设置为透明
                    img.putpixel((i, j), (255, 255, 255, 0))

        # 把图片强制转成RGBA(背景透明的关键)
        img = img.convert("RGBA")
        #若png已存在则删除之
        png_path = get_absolute_path('png', factor_name, time_interval, current_task_name, template_name)
        delete_if_exist(png_path)
        img.save(png_path)
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() + ' ' + dict_template_name[template_name] + ' [' + format_file_name(time_interval, current_task_name) + '] 导出PNG异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, mode = 'a')

def composite_png(img, factor_name, state_png_path, time_interval, current_task_name, template_name):
    '''
        对各省插值图，采取图像合成的方式输出
        img--- 省份插值模板图像
        z_field--- 因子名称
        state_png_path--- 全国插值结果图片路径
        time_interval--- 时间尺度
        current_task_name--- 当前任务名称
        template_name--- 模板名称
    '''

    try:
        # 全国插值图
        img1 = Image.open(state_png_path)
        # 模板图片
        img2 = img
        # 获取alpha通道值
        alpha = img2.split()[3]
        
        '''
            composite参数设置:
            第一个参数，设置为全国的插值图片
            第二个参数，设置为 模板图片，该模板的省份部分透明，其他部分不透明（白色）
            第三个参数，mask，对于L类型，计算方式为 img1 * L / 255 + img2 * (1 - L / 255)
        '''
        img = Image.composite(img1, img2, alpha)
        # img.putalpha(alpha)

        #若png已存在则删除之
        png_path = get_absolute_path('png', factor_name, time_interval, current_task_name, template_name)
        delete_if_exist(png_path)
        img.save(png_path)
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() + ' ' + dict_template_name[template_name] + ' [' + format_file_name(time_interval, current_task_name) + '] 合成PNG异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, mode = 'a')


def start(time_interval = 'hour', current_task_name = None, use_history_temp = False):
    '''
        执行主方法
        time_interval--- 时间尺度
        current_task_name = 当前任务名称
    '''

    for template_name in dict_template_name.keys():
        if template_name == 'state' or template_name == 'sd':
            img = open_template_png(time_interval, current_task_name, template_name)
            for z_field in z_fields: 
                tif_path = get_absolute_path('tif', z_field, time_interval, current_task_name, use_history_temp = use_history_temp) 
                # factor_data = read_tif_data(tif_path)
                # 用PIL - Image Open方式打开TIF
                factor_data = read_tif_data_by_img(tif_path)
                export_png(img, z_field, factor_data, time_interval, current_task_name, template_name)
        else:
            # 省份模板图像
            img = open_template_png(time_interval, current_task_name, template_name)
            for z_field in z_fields:
                state_png_path = get_absolute_path('png', z_field, time_interval, current_task_name, 'state')
                composite_png(img, z_field, state_png_path, time_interval, current_task_name, template_name)
        print(u'<<<<<<<<<<<<<<<<<<' + dict_template_name[template_name] + ' ' + get_des_by_time(time_interval) + u' 导出/合成PNG完成: ' + format_time() + '>>>>>>>>>>>>>')

    print(u'<<<<<<<<<<<<<<<<<<<<<<<<3. ' + get_des_by_time(time_interval) + u' 导出全部PNG完成:' + format_time() + '>>>>>>>>>>>>>>>>>>>>')


'''
    程序入口
'''
if __name__ =='__main__':
    print(u'>>>>>>>>>>>>>导出png开始时间:', format_time(),'>>>>>>>>>>>>>>>>>>>>>>>>')
    start('day', '20181127')
    print(u'>>>>>>>>>>>>>导出png结束时间:', format_time(),'>>>>>>>>>>>>>>>>>>>>>>>>')
    print(u'>>>>>>>>>>>>>导出png成功>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

