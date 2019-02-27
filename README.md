# GDAL空间插值服务
    GDAL空间插值服务，依赖python 3.x环境及GDAL包，实现从请求站点及小时/日/实时数据到反距离插值并生成插值结果png图片的完成流程。

### 本地运行项目

1. 下载代码：

    ``` 
        git@git.fpi-inc.site:product/public-products/gdal-interpolation-server.git
     ```

2. 运行环境：

    ``` 
        python 3.x  
    ```

3. 安装依赖：

    ``` shell
        pip install simplejson
        pip install Pillow
        pip install gdal
        pip install apscheduler
    ```
    * 若GDAL安装失败，请参考 https://blog.csdn.net/shaxiaozilove/article/details/78975386
    
4. 新建数据保存文件夹(interpolation_result_dir路径下)

    ``` 
        log
        state
        temp
    ```
    * 若日志、临时文件及结果png存储在其他路径下，请在对应位置创建，若已存在请忽略
5. 启动项目

    ``` 
        python run_task.py
        python history_hour_data_task.py
        python history_day_data_task.py
    ```
    * 以上启动项目的方式中，根据需要选择运行，其中   
        第一个为常规的进行小时和日数据插值  
        第二个为历史小数数据插值   
        第三个为历史日数据插值


### 可自定义的配置


1. 色阶

    色阶配置在``colors``文件夹下``.py``文件夹中，针对AQI + 6因子插值，目前已有30色阶和60色阶，色阶的配置包括两部分：    
    （1）颜色  
    （2）AQI + 6因子分级  

    可根据需要，按照已有色阶进行配置。

2. 插值结果图片的宽度和高度  

    ``config.py``中的``width、height``分别代表图片的宽度和高度，会决定插值网格的行列数，也会影响插值的速度，若宽度和高度发生变化，则``common/state.png``出图模板的宽、高应与其保持一致。

3. 出图模板  

    ``config.py``中的``export_png_template``为出图模板的名称，位于``/common/``路径下，一般与插值区域的行政区划图结果一致，现在的模板是中国。

4. 插值结果输出范围  

    ``config.py``中的``output_bounds``表示插值输出范围，格式``[左上角经度, 左上角纬度, 右下角经度, 有下角纬度]``，现在的范围是中国。

5. 插值算法

    ``config.py``中的``grid_algorithm``表示插值算法，现在设置的是反距离权重，``power:3.6，smooth:0.2``，详细说明参考``https://www.gdal.org/gdal_grid.html``。

6. 站点和监测数据请求路径

    ``config.py``中的``state_station_url``表示站点请求url，现在设置的是全国所有的国控站点，``state_hourdata_recent_url、state_hourdata_url、state_daydata_url``分别表示国控站最新的数据、国控站小时数据和国控站日数据接口，它们分别应用于常规和历史的小时/日数据插值。  
    
    针对其他区域的插值，若站点和监测数据请求路径发送变化，有两种处理方式：  
    （1）替换上述路径；  
    （2）在``run_task.py``中的如下代码处指定```station_url、data_url```:
    ``` python
        structdata.start('hour', current_task_name, False, station_url=None, data_url=None)
    ```  
    历史小时、日数据中的修改与（2）中一致。

7. 工作空间

    ``config.py``中的``base_dir``表示结果图片、日志、临时文件、出图模板等的存放路径，目前设置的路径是当前路径下的```interpolation_result_dir```，应确保该路径下有``log、state、temp``目录。

### 如何应用于其他项目/区域


1. 配置该行政功能区的出图模板

    使用``EPSG:3857``坐标系下的行政区域边界对插值生成tif进行裁剪，转成png即可作为出图模板。

2. 修改站点和监测数据接口

* 站点接口返回数据格式应为标准GeoJSON格式，下面是数据格式示例：

``` json
    {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "coordinates": [
                        113.235,
                        23.1422
                    ],
                    "type": "Point"
                },
                "properties": {
                    "id": "5a13fa03e4ca2e05e4dd91dd",
                    "name": "广雅中学",
                    "type": "国控站",
                    "area": "广州市",
                    "cityCode": "440100.0",
                    "stationCode": "1345A"
                }
            }
        ]
    }
```

* 下面是监测数据格式示例：

``` json
    {
        "entries": [
            {
                "stationCode": "1071A",
                "stationName": null,
                "area": "沧州市",
                "measure": null,
                "heath": null,
                "quality": "重度污染",
                "year": "2018",
                "month": "2018-11",
                "day": "2018-11-27",
                "hours": "2018-11-27 11",
                "longitude": null,
                "latitude": null,
                "citycode": null,
                "MN": "1071A",
                "V_141": 26,
                "V_108": 54,
                "V_108_8H": 28,
                "V_121": 63,
                "V_101": 8,
                "V_AQI": 232,
                "V_107": 372,
                "V_106": 0.3,
                "V_127": null,
                "V_126": null,
                "V_129": null,
                "V_130": null,
                "V_128": null,
                "gb_hours": "2018-11-27 11",
                "MAIN_POLLUTANTS": [
                    "107"
                ]
            }
        ]
    }
```

### 项目目录结构

```
├── config.py                                   // 插值程序配置变量
├── utils.py                                    // 公共方法
├── structdata.py                               // 请求数据并对数据预处理代码
├── grid.py                                     // 插值代码
├── exportpng.py                                // 出图代码
├── run_task.py                                 // 常规定时插值代码
├── history_hour_data_task.py                   // 历史小数数据插值代码
├── history_day_data_task.py                    // 历史日数据插值代码
├── README.md                                   // 项目介绍
├── .gitignore                                  // git不需要上传的配置
├── colors                                      // 色阶配置文件目录
├── interpolation_result_dir                    // 插值结果保存目录
│   ├── common                                  // 出图模板目录
│   ├── log                                     // 日志目录
│   ├── state                                   // 结果图片目录
│   ├── temp                                    // 临时文件目录
```

### 其他说明

1. 插值结果存储路径规范
    * 小时数据:  
    ``state/yyyy/mm/dd/因子名称_yyyymmddHH.png``
    * 日数据:  
    ``state/yyyy/mm/dd/因子名称_yyyymmdd.png``  
    * 月数据:  
    ``state/yyyy/mm/因子名称_yyyymm.png``  

    如以下示例：
    ```
        /state/2018/10/20/aqi_20181020.png
        /state/2018/10/20/aqi_2018102012.png
    ```

2. 生成历史小时/日数据插值  

    修改``history_hour_data_task.py、history_day_data_task.py``代码中的如下代码:  

``` python
    str_start_time = '2018-11-24 00:00:00' #历史数据开始时间
    str_end_time = '2018-11-28 23:00:00' #历史数据结束时间
```


3. 当前时间的常规插值

    运行```run_task.py```文件，小时数据插值，设置在每小时的``50``分，  

    日数据插值，设置在``02:10``，可根据日数据获取时间进行调整，
    月数据插值，设置在``每月第1天的 03:10``，可根据月数据获取时间进行调整。

