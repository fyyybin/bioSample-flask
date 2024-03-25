from flask import Blueprint, request, make_response, jsonify
from pymongo import MongoClient
import datetime
import time
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
            if mongodb:
                result = []
                for i in mongodb:
                    del i['_id']
                    result.append(i)
        else:
            mongodb = client['bioSample']['examine'].find()
            result = []
            if mongodb:
                for i in mongodb:
                    del i['_id']
                    result.append(i)
        if result:
            res = {'result':result}
            status = '200 OK'
        else:
            res = {"error": "没有找到对应的数据"}
            status = '200 OK'
       
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    resp.headers['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
    return resp

@bp.route('/examine/', methods=['POST'])
def examine_data():
    ynb_num = request.form['样本编号']
    operation = request.form['操作']
    username = request.form['用户信息']
    state = request.form['样本状态']
    time = request.form['审批时间']
    now = datetime.datetime.now()
    outTime = now.strftime("%Y-%m-%d %H:%M:%S")
    client = MongoClient(host='localhost', port=27017)

    try:
        if operation == '样本入库':
            if state == '通过':
                newData = {"$set":{
                '入库状态':'已入库'
                }}
                # 审核数据库中修改state
                client['bioSample']['examine'].update_many({
                    '样本编号':ynb_num,
                    '操作':operation,
                    '用户信息':username,
                    '审批时间':time
                },newData)

                # 删除待入库数据库中的数据
                client['bioSample']['collections'].delete_one({
                    '样本编号':ynb_num,
                })
                # 将数据 加入 入库数据库中 添加入库时间
                mongo = client['bioSample']['examine'].find({
                    '样本编号':ynb_num,
                    '操作':operation,
                    '用户信息':username,
                    '审批时间':time
                })
                result = []
                for i in mongo:
                    print(i)
                    del i['_id']
                    del i['用户信息']
                    del i['操作']
                    i['入库时间'] = outTime
                    result.append(i)
                if result:
                    client['bioSample']['container'].insert_one(result[0])
            else:
                newData = {"$set":{
                '入库状态':'审核拒绝'
                }}
                # 审核数据库中修改state
                client['bioSample']['examine'].update_many({
                    '样本编号':ynb_num,
                    '操作':operation,
                    '用户信息':username
                },newData)
                client['bioSample']['collections'].update_many({
                    '样本编号':ynb_num,
                },newData)
        elif operation == '样本出库':
            if state == '通过':
                newData = {"$set":{
                '入库状态':'已出库'
                }}
                # 审核数据库中修改state
                client['bioSample']['examine'].update_many({
                    '样本编号':ynb_num,
                    '操作':operation,
                    '用户信息':username,
                    '审批时间':time
                },newData)

                mongo = client['bioSample']['examine'].find({
                    '样本编号':ynb_num,
                    '操作':operation,
                    '用户信息':username,
                    '审批时间':time
                })
                choose_data = mongo[0]
                del choose_data['_id']
                choose_data['测序状态'] = '已送样'
                # 若为验证分析即删除，若为组学分析加入 分析数据库
                if choose_data['研究用途'] == '组织细胞分子等实验验证':
                    client['bioSample']['container'].delete_one({
                        '样本编号':ynb_num,
                    })
                else:
                    client['bioSample']['container'].delete_one({
                        '样本编号':ynb_num,
                    })
                    client['bioSample']['analyze'].insert_one(choose_data)
            else:
                newData = {"$set":{
                '入库状态':'审核拒绝'
                }}
                # 审核数据库中修改state
                client['bioSample']['examine'].update_many({
                    '样本编号':ynb_num,
                    '操作':operation,
                    '用户信息':username,
                    '审批时间':time
                },newData)         
        elif operation == '样本废弃':
            if state == '通过':
                newData = {"$set":{
                '入库状态':'已废弃'
                }}
                # 审核数据库中修改state
                client['bioSample']['examine'].update_many({
                    '样本编号':ynb_num,
                    '操作':operation,
                    '用户信息':username,
                    '审批时间':time
                },newData)

                # 删除 入库数据库的数据
                client['bioSample']['container'].delete_one({
                    '样本编号':ynb_num,
                })
            else:
                newData = {"$set":{
                '入库状态':'审核拒绝'
                }}
                # 审核数据库中修改state
                client['bioSample']['examine'].update_many({
                    '样本编号':ynb_num,
                    '操作':operation,
                    '用户信息':username,
                    '审批时间':time
                },newData)
        elif operation == '样本转移':
            
            # 审核库中 状态变更
            if state == '通过':
                client['bioSample']['examine'].update_many({
                    '样本编号':ynb_num,
                    '操作':operation,
                    '用户信息':username,
                        '审批时间':time
                },{"$set":{
                    '入库状态':'已转移'
                    }})

                # 数据库中 位置变更
                mongo = client['bioSample']['examine'].find({
                        '样本编号':ynb_num,
                        '操作':operation,
                        '用户信息':username,
                        '审批时间':time
                    })
                newData = {"$set":{
                    '位置': mongo[0]['新位置']
                    }}
                    # 审核数据库中修改state
                client['bioSample']['container'].update_many({
                    '样本编号':ynb_num,
                },newData)
            else:
                newData = {"$set":{
                '入库状态':'审核拒绝'
                }}
                # 审核数据库中修改state
                client['bioSample']['examine'].update_many({
                    '样本编号':ynb_num,
                    '操作':operation,
                    '用户信息':username,
                    '审批时间':time
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
    ynb_num = request.form['样本编号']
    operation = request.form['操作']
    username = request.form['用户信息']
    client = MongoClient(host='localhost', port=27017)
    client['bioSample']['examine'].delete_one({
                    '样本编号':ynb_num,
                    '操作':operation,
                    '用户信息':username
                })
    res = {'result':'success'}
    status = '200 OK'
    resp = make_response(jsonify(res))
    resp.status = status
    resp.headers['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
    return resp


@bp.route('/hosSearch/', methods=['POST'])
def hosSearch():
    client = MongoClient(host='localhost', port=27017)
    examine = client['bioSample']['examine'].find()
    container = client['bioSample']['container'].find()
    analyse = client['bioSample']['analyse'].find()

    examine_nums, container_nums,analyse_nums = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
    for item in examine:
        if item['入库状态'] == '审核中' and item['操作'] == '样本入库':
            if item['采集医院'] == '浙江大学医学院附属第一医院':
                examine_nums[0] += 1
            elif item['采集医院'] == '浙江大学医学院附属第四医院':
                examine_nums[1] += 1
            elif item['采集医院'] == '台州医院':
                examine_nums[2] += 1
            elif item['采集医院'] == '浙江大学医学院附属儿童医院':
                examine_nums[3] += 1
    for item in container:
        if item['采集医院'] == '浙江大学医学院附属第一医院':
            container_nums[0] += 1
        elif item['采集医院'] == '浙江大学医学院附属第四医院':
            container_nums[1] += 1
        elif item['采集医院'] == '台州医院':
            container_nums[2] += 1
        elif item['采集医院'] == '浙江大学医学院附属儿童医院':
            container_nums[3] += 1
    for item in analyse:
        if item['采集医院'] == '浙江大学医学院附属第一医院':
            analyse_nums[0] += 1
        elif item['采集医院'] == '浙江大学医学院附属第四医院':
            analyse_nums[1] += 1
        elif item['采集医院'] == '台州医院':
            analyse_nums[2] += 1
        elif item['采集医院'] == '浙江大学医学院附属儿童医院':
            analyse_nums[3] += 1
    res = {'result':{'待入库':examine_nums, '已入库': container_nums, '测序中': analyse_nums}}
    status = '200 OK'
    resp = make_response(jsonify(res))
    resp.status = status
    resp.headers['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
    return resp


