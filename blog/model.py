# -*- coding: UTF-8 -*-
import threading
import traceback
from flask import Flask,request,jsonify
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

@app.route('/health')
def index():
    return 'health'

########################################
# 用于开发过程中的规则测试
########################################
@app.route('/test', methods=['POST'])
def test_controller():
    try:
        call = request.form['call']
        param = eval(request.form['param'])
        rule = request.form['rule']
        result = {}
        result["response_code"] = '00'
        result['content'] = test(rule, param, call)
        return jsonify(result)
    except:
        return traceback.format_exc()

def test(rule,params,call):
    exec (rule, params)
    return eval(call, params)


def main():
    app.run(port=11200, host='0.0.0.0', threaded=True )

if __name__ == '__main__':
    main()