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
    client = MongoClient(host='localhost', port=27017)

    try:
        if operation == '样本入库':
            if state == '通过':
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
                    del i['采集状态']
                    del i['运输状态']
                    del i['接收状态']
                    del i['负责人']
                    del i['负责人联系方式']
                    del i['运出时间']
                    del i['运输方']
                    del i['接收人']
                    del i['接收人联系方式']
                    del i['接收时间']
                    del i['用户信息']
                    del i['操作']

                    i['入库时间'] = datetime.datetime.fromtimestamp(1234567896)
                    result.append(i)
                if result:
                    client['bioSample']['container'].insert_one(result[0])
                    
            else:
                newData = {"$set":{
                '入库状态':'审核拒绝'
                }}
                # 审核数据库中修改state
                client['bioSample']['examine'].update_many({
                    '样本源编号':ynb_num,
                    '操作':operation,
                    '用户信息':username
                },newData)
        elif operation == '样本出库':
            if state == '通过':
                newData = {"$set":{
                '入库状态':'已出库'
                }}
                # 审核数据库中修改state
                client['bioSample']['examine'].update_many({
                    '样本源编号':ynb_num,
                    '操作':operation,
                    '用户信息':username
                },newData)

                # 删除 入库数据库的数据
                client['bioSample']['container'].delete_one({
                    '样本源编号':ynb_num,
                })
            else:
                newData = {"$set":{
                '入库状态':'审核拒绝'
                }}
                # 审核数据库中修改state
                client['bioSample']['examine'].update_many({
                    '样本源编号':ynb_num,
                    '操作':operation,
                    '用户信息':username
                },newData)
        elif operation == '样本废弃':
            if state == '通过':
                newData = {"$set":{
                '入库状态':'已废弃'
                }}
                # 审核数据库中修改state
                client['bioSample']['examine'].update_many({
                    '样本源编号':ynb_num,
                    '操作':operation,
                    '用户信息':username
                },newData)

                # 删除 入库数据库的数据
                client['bioSample']['container'].delete_one({
                    '样本源编号':ynb_num,
                })
            else:
                newData = {"$set":{
                '入库状态':'审核拒绝'
                }}
                # 审核数据库中修改state
                client['bioSample']['examine'].update_many({
                    '样本源编号':ynb_num,
                    '操作':operation,
                    '用户信息':username
                },newData)
        elif operation == '样本转移':
            
            # 审核库中 状态变更
           
            client['bioSample']['examine'].update_many({
                '样本源编号':ynb_num,
                '操作':operation,
                '用户信息':username
            },{"$set":{
                '入库状态':'已转移'
                }})

            # 数据库中 位置变更
            mongo = client['bioSample']['examine'].find({
                    '样本源编号':ynb_num,
                    '操作':operation,
                    '用户信息':username
                })
            newData = {"$set":{
                '位置': mongo[0]['新位置']
                }}
                # 审核数据库中修改state
            client['bioSample']['container'].update_many({
                '样本源编号':ynb_num,
            },newData)
            
            

        res = {'result':'success'}
        status = '200 OK'
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    resp.headers['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
    return resp

@bp.route('/examine/del', methods=['POST'])
def examine_del():
    ynb_num = request.form['样本源编号']
    operation = request.form['操作']
    username = request.form['用户信息']
    client = MongoClient(host='localhost', port=27017)
    client['bioSample']['examine'].delete_one({
                    '样本源编号':ynb_num,
                    '操作':operation,
                    '用户信息':username
                })
    res = {'result':'success'}
    status = '200 OK'
    resp = make_response(jsonify(res))
    resp.status = status
    resp.headers['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
    return resp