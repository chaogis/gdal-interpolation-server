from flask import Flask, request, render_template, make_response
import json
import traceback
import os

from config import base_dir
from config import png_path

from utils import get_absolute_path
from utils import format_time
from utils import write_content
from utils import make_dir_by_date

from history_hour_data_task import do_hour_task
from history_day_data_task import do_day_task
from history_month_data_task import do_month_task


app = Flask(__name__)

@app.route('/city-interpolation-server/public/interpolate/api/v1.0/do-interpolation', methods=['POST'])
def do_interpolation():
    data = json.loads(request.form.get('params'))
    interpolation_type = data['type']
    time_interval = data['timeInterval']
    start_time = data['startTime']
    end_time = data['endTime']
    try:
        do_task = do_hour_task
        if time_interval == 'day':
            do_task = do_day_task
        elif time_interval == 'month':
            do_task = do_month_task
        do_task(start_time, end_time, interpolation_type, True)
        msg = {"status": 1, "msg": "处理成功!"}
        return json.dumps(msg)
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() + '执行历史数据/重新插值任务异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, mode = 'a')
        return json.dumps({"status": 0, "msg": str(msg)})

@app.route('/city-interpolation-server/public/interpolate/api/v1.0/show-interpolation/<string:filename>', methods=['GET'])
def show_photo(filename):
    try:
        png_dir = os.path.join(base_dir, png_path)
        if request.method == 'GET':
            if filename is None:
                return make_response('<h2>传入的图片文件名为null!</h2>', 412)
            else:
                str_date = (filename.split('_')[1]).split('.')[0]
                relative_path = make_dir_by_date(str_date)
                if relative_path.find('/') != -1:
                    png_abs_path = (os.path.join(png_dir, relative_path, '%s' % filename))
                    if os.path.exists(png_abs_path):
                        image_data = open(png_abs_path, "rb").read()
                        response = make_response(image_data)
                        response.headers['Content-Type'] = 'image/png'
                        return response
                    else:
                        return make_response('<h2>请求的图片不存在!</h2>', 404)
                else:
                    return make_response('<h2>{}!</h2>'.format(relative_path), 406)
        else:
            return make_response('<h2>请使用GET请求获取插值图片!</h2>', 400)
    except Exception:
        log = []
        log.append('>>>>>>>>>>' + format_time() + '请求插值图片异常:\n')
        msg = traceback.format_exc()
        log.append(str(msg) + '\n')
        print(log)
        write_content(get_absolute_path('log'), log, mode = 'a')
        return make_response('<h2>请求插值图片异常!</h2>', 400)

@app.route('/city-interpolation-server/public/interpolate/api/v1.0/index.do', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
