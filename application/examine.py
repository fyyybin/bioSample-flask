from flask import Blueprint, request, make_response, jsonify
from pymongo import MongoClient
import datetime
import json
bp = Blueprint('examine_bp', __name__, url_prefix='')

# 查询cell
@bp.route('/examineSearch/', methods=['POST'])
def get_container_data():
    """
        获取审核数据库样本
    """
    name = request.form['username']
        
    try:
        
        client = MongoClient(host='localhost', port=27017)
        if name != 'administrator':
            mongodb = client['bioSample']['examine'].find({
                '用户信息':name,
            })
            result = []
            for i in mongodb:
                del i['_id']
                result.append(i)
        else:
            mongodb = client['bioSample']['examine'].find()
            result = []
            for i in mongodb:
                del i['_id']
                result.append(i)
        if result:
            res = {'result':result}
            status = '200 OK'
        else:
            res = {"error": "没有找到对应的数据"}
            status = '403 Forbidden'
       
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    resp.headers['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
    return resp

@bp.route('/examine/', methods=['POST'])
def examine_data():
    ynb_num = request.form['样本源编号']
    operation = request.form['操作']
    username = request.form['用户信息']
    state = request.form['样本状态']
    try:
        client = MongoClient(host='localhost', port=27017)
        if state == '已入库':
            newData = {"$set":{
            '入库状态':'已入库'
            }}
            # 审核数据库中修改state
            client['bioSample']['examine'].update_many({
                '样本源编号':ynb_num,
                '操作':operation,
                '用户信息':username
            },newData)
            # 删除待入库数据库中的数据
            client['bioSample']['collections'].delete_one({
                '样本源编号':ynb_num,
            })
            # 将数据 加入 入库数据库中 添加入库时间
            mongo = client['bioSample']['examine'].find({
                '样本源编号':ynb_num,
                '操作':operation,
                '用户信息':username
            })

            result = []
            for i in mongo:
                del i['_id']
                i['入库时间'] = datetime.datetime.fromtimestamp(1234567896)
                result.append(i)
            if result:
                client['bioSample']['container'].insert_one(result[0])
                res = {'result':'success'}
                status = '200 OK'
            else:
                res = {"error": "没有找到对应的数据"}
                status = '403 Forbidden'
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    resp.headers['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
    return resp
