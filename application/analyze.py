from pymongo import MongoClient
from flask import Blueprint, current_app, request, make_response, jsonify
from .util.util_analyse import transform_analyse

bp = Blueprint('analyse', __name__, url_prefix='/analyze')

# 所有采集需求
@bp.route('/',methods=['POST'])
def all_analyse():
    """
        {
            "样本编号": "TZYY-QT1-20240327-1",
            "采集医院": "台州医院",
            "样本源类型": "DNA",
            "样本源姓名": "刘佳怡",
            "研究用途": "组织细胞分子等实验验证",
            "入库时间": "20240328",
            "是否测序": "是",
            "测序公司": "**********生物医学",
            "测序平台": "******测序平台",
            "测序数据": "无",
            "测序状态": "测序中"
        }
    """
    name = request.form['username']
    client = MongoClient(host='localhost', port=27017)
    try:
        if name != 'administrator':
            mongodb = client['bioSample']['analyze'].find({
                '用户信息':name,
            })
            if mongodb:
                result = []
                for i in mongodb:
                    del i['_id']
                    result.append(i)
        else:
            mongodb = client['bioSample']['analyze'].find()
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
    return resp

@bp.route('/change/',methods=['POST'])
def change_seq():
    company = request.form['测序公司']
    plat = request.form['测序平台']
    data = request.form['测序数据']
    name = request.form['username']
    num = request.form['样本编号']
    client = MongoClient(host='localhost', port=27017)
    try:
        if name != 'administrator':
            newData = { "$set": { 
                    '测序公司':company,
                    '测序平台': plat,
                    '测序数据':data,
                    '测序状态':'测序中'
            }}
            client['bioSample']['analyze'].update_many({
                    '样本编号':num,
                    '用户信息':name,
                },newData)
        else:
            newData = { "$set": { 
                    '测序公司':company,
                    '测序平台': plat,
                    '测序数据':data,
                    '测序状态':'测序中'
            }}
            client['bioSample']['analyze'].update_many({
                    '样本编号':num,
                },newData)
        res = {'result':'success'}
        status = '200 OK'
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'
    resp = make_response(jsonify(res))
    resp.status = status
    return resp


@bp.route('/finish/',methods=['POST'])
def change_finish_seq():
    name = request.form['username']
    num = request.form['样本编号']
    client = MongoClient(host='localhost', port=27017)
    try:
        if name != 'administrator':
            newData = { "$set": { 
                    '测序状态':'已完成'
            }}
            client['bioSample']['analyze'].update_many({
                    '样本编号':num,
                    '用户信息':name,
                },newData)
        else:
            newData = { "$set": { 
                    '测序状态':'已完成'
            }}
            client['bioSample']['analyze'].update_many({
                    '样本编号':num,
                },newData)
        res = {'result':'success'}
        status = '200 OK'
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'
    resp = make_response(jsonify(res))
    resp.status = status
    return resp

            