#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2020/4/29 10:47

import time
import numpy as np
from backend.tr import tr
import tornado.web
import tornado.gen
import tornado.httpserver
import base64
from PIL import Image, ImageDraw
from io import BytesIO
import json
import re
from backend.tools.np_encoder import NpEncoder
from backend.tools import log
from loguru import logger

logger.add("trrun2_log_{time}.log",
           rotation="500MB",
           encoding="utf-8",
           enqueue=True,
           compression="zip",
           retention="10 days")


class TrRunMy(tornado.web.RequestHandler):
    '''
    使用 tr 的 run 方法
    '''

    def pick_number(numstr):
        regex_val = re.findall(r"\d+\.?\d*", numstr)
        if len(regex_val) == 0:
            return 0
        else:
            np_arr = np.array(regex_val)
            return np_arr.astype(float)[0]

    def convert_readable(raw_data):
        pattern = re.compile(r'[^\u4e00-\u9fa5]')
        arrdic = []
        for i in range(0, len(raw_data)):
            item = {
                "Point": raw_data[i][0][:-1],
                "Text": re.sub(pattern, '', raw_data[i][1]),
                "Score": raw_data[i][2]
            }
            arrdic.append(item)
        return arrdic

    def get(self):
        self.set_status(404)
        self.write("404 : Please use POST")

    @tornado.gen.coroutine
    def post(self):
        '''

        :return:
        报错：
        400 没有请求参数

        '''
        start_time = time.time()
        MAX_SIZE = 1600

        img_up = self.request.files.get('file', None)
        img_b64 = self.get_argument('img', None)
        rotate_type = int(self.get_argument("rotate_type", "0"))
        isfumo = int(self.get_argument("isfumo", "0"))

        # 判断是上传的图片还是base64
        self.set_header('content-type', 'application/json')
        up_image_type = None
        if img_up is not None and len(img_up) > 0:
            img_up = img_up[0]
            up_image_type = img_up.content_type
            up_image_name = img_up.filename
            img = Image.open(BytesIO(img_up.body))
        elif img_b64 is not None:
            raw_image = base64.b64decode(img_b64.encode('utf8'))
            img = Image.open(BytesIO(raw_image))
        else:
            self.set_status(400)
            logger.error(json.dumps(
                {'code': 400, 'msg': '没有传入参数'}, cls=NpEncoder))
            self.finish(json.dumps(
                {'code': 400, 'msg': '没有传入参数'}, cls=NpEncoder))
            return

        # 旋转图片
        try:
            if rotate_type > 0:
                if rotate_type == 3:
                    img = img.rotate(180, expand=True)
                elif rotate_type == 6:
                    img = img.rotate(270, expand=True)
                elif rotate_type == 8:
                    img = img.rotate(90, expand=True)
        except Exception as ex:
            error_log = json.dumps({'code': 400, 'msg': '旋转图片产生了一点错误，请检查日志', 'err': str(
                ex)}, ensure_ascii=False, cls=NpEncoder)
            logger.error(error_log, exc_info=True)
            self.finish(error_log)
            return
        img = img.convert("RGB")

        if img.height > MAX_SIZE or img.width > MAX_SIZE:
            scale = max(img.height / MAX_SIZE, img.width / MAX_SIZE)

            new_width = int(img.width / scale + 0.5)
            new_height = int(img.height / scale + 0.5)
            img = img.resize((new_width, new_height), Image.ANTIALIAS)

        # 进行ocr
        res = tr.run2(img.copy().convert("L"), flag=tr.FLAG_ROTATED_RECT)
        if isfumo == 1:
            res = TrRunMy.convert_readable(res)
        response_data = {'code': 200, 'message': 'success', 'data': res}

        self.finish(json.dumps(response_data,
                               ensure_ascii=False, cls=NpEncoder))
        return
