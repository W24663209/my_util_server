"""
@Description: TODO

@Author: weizongtang

@Create: 2020-07-29 23:07
"""
from flask import Flask, request, json
import logging
from util import Util

app = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)


@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return environ


@app.route('/util', methods=['POST'])
def method():
    """
    我的工具
    :return:
    """
    util = Util()
    # getattr根据字符串调用方法 request.args['type']方法名,json返回值
    c = getattr(util, request.args['type'], json)
    return c(json.loads(request.data))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
