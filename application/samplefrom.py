from pymongo import MongoClient
from flask import Blueprint,current_app, request, make_response, jsonify
from .util.util_samplefrom import transform_from, sampleID
from .util.util_collection import transform_cols

bp = Blueprint('samplefrom', __name__, url_prefix='/samplefrom')

# 所有样本源
@bp.route('/',methods=['GET'])
def all_sampleFrom():
    """
        读取数据库中的样本源
        {
            "样本源编号": "ZSFY-TT-21000009-K-01",
            "样本源姓名": "王*",
            "性别": "男",
            "年龄": "45",
            "样本创建时间": "20240102",
            "样本源类型": "肥胖症",
            "知情同意": "是"
        }
    """
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        document = client['bioSample']['samplefrom'].find()
        result = transform_from(document)
        res = { "data": result, "total": len(result) }
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'
    resp = make_response(jsonify(res))
    resp.status = status
    return resp

# 所有可进行采集的样本源
@bp.route('/agree/',methods=['GET'])
def all_agreeFrom():
    """
        读取数据库中的所有知情同意为 “是” 的样本源
        {
            "样本源编号": "ZSFY-TT-21000009-K-01",
            "样本源姓名": "王*",
            "性别": "男",
            "年龄": "45",
            "样本创建时间": "20240102",
            "样本源类型": "肥胖症",
            "知情同意": "是"
        }
    """
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        document = client['bioSample']['samplefrom'].find({"知情同意":"是"})
        result = transform_from(document)
        res = { "data": result, "total": len(result) }
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'
    resp = make_response(jsonify(res))
    resp.status = status
    return resp

# 知情同意更新数据
@bp.route('/agree/add/', methods=['POST'])
def add_agreeFrom():
    """
        1、通过样本源编号查找要修改的样本源
            { 样本源编号: fromId }
        2、更新集合中的数据
        {
            "性别": "男",
            "年龄": "34",
            "知情同意": "是",
            "样本创建时间": "20240313",
        }
    """
    fromId = request.json["样本源编号"]
    doc = {}
    doc["性别"] = request.json["性别"]
    doc["年龄"] = request.json["年龄"]
    doc["知情同意"] = "是"
    doc["样本创建时间"] = request.json["样本创建时间"]
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        query = { "样本源编号": fromId }
        newvalues = { "$set": doc }
        col = client['bioSample']['samplefrom']
        col.update_one(query, newvalues)
        res = {"result": "上传数据成功"}
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    return resp  
    
# 样本源所有采集信息
@bp.route('/info/', methods=['GET'])
def singleInfo():
    """
        通过样本源编号、采集内容、采集医院查找要展示的样本
        {
            "样本源编号": "ZSFY-TT-21000009-K-01",
            "样本源姓名": "张**",
        }
    """
    doc = {}
    doc["样本源编号"] = request.json["样本源编号"]
    doc["样本源姓名"] = request.json["样本源姓名"]
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        col = client['bioSample']['collections']
        document = col.find(doc,{"_id":0})
        res = {"result": transform_cols(document) }
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    return resp 


# 新增样本源
@bp.route('/add/', methods=['POST'])
def add_sampleFrom():
    """
        加入数据库样本源
        {
            样本源编号: 'xxxxxx',
            样本源姓名: '王*',
            样本源类型: 'xxxx',
            采集医院： 'xxxxxx',
            知情同意：'否'
        }
        1. 先加入到样本源列表中，需要签订知情同意书（是否签订同意书：否）;
        2. 签订时补充个人信息，添加到知情同意列表（样本状态:'正常');
    """
    doc = {}
    name = request.json["样本源姓名"]
    type = request.json["样本源类型"]
    hospital = request.json["采集医院"]
    id = sampleID(name,type,hospital)
    doc["样本源编号"] = id
    doc['样本源姓名'] = name
    doc['样本源类型'] = type
    doc['采集医院'] = hospital
    doc['知情同意'] = "否"
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        client['bioSample']['samplefrom'].insert_one(doc)
        res = {"result": "上传数据成功"}
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    return resp

# 样本源筛选
@bp.route('/<fromtype>/', methods=["GET"])
def get_fromtype(fromtype):
    """
        样本源类型: fromtype
    """
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        query = { "样本源类型": fromtype }
        document = client['bioSample']['samplefrom'].find(query,{ "_id":0 })
        result = transform_from(document)
        res = { "data": result, "total": len(result) }
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    return resp

# 删除样本源
@bp.route('/delete/<fromId>/', methods=["DELETE"])
def del_from(fromId):
    """
        通过样本源编号删除样本源
        {
            样本源编号: fromId
        }
    """
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        client['bioSample']['samplefrom'].delete_one({"样本源编号": fromId})
        client['bioSample']['collections'].delete_many({"样本源编号": fromId})
        res = {"result": "删除数据成功"}
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    return resp

# 按编号查找样本源
@bp.route('/query/<fromId>/', methods=["GET"])
def query_Byid(fromId):
    """
        通过样本源编号删除样本源
        {
            样本源编号: fromId
        }
    """
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        document = client['bioSample']['samplefrom'].find_one({"样本源编号": fromId},{"_id":0})
        res = {"data": document}
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    return resp
