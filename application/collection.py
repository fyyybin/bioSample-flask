from pymongo import MongoClient
from flask import Blueprint, current_app, request, make_response, jsonify
from .util.util_collection import transform_cols, transform_detail

bp = Blueprint('collection', __name__, url_prefix='/collection')

# 所有采集需求
@bp.route('/',methods=['GET'])
def all_collections():
    """
        {
            "创建时间": "20240313",
            "年龄": "34",
            "性别": "男",
            "采集时间": "2024/03/29 12:00:00",
            "样本源姓名": "赵*",
            "样本源类型": "肾癌",
            "样本源编号": "ZSFY-TT-21000009-K-03",
            "知情同意": "是",
            "编号类型": "住院",
            "采集状态": "是",
            "运输方名称": "医院",
            "运出时间": "2024/3/30 8:06:08",
            "运输状态": "已接收",
            "接收人名称": "王*",
            "接收时间": "2024/04/12 14:00:05",
            "联系方式": "13688564458"
        }
    """
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        document = client['bioSample']['collections'].find()
        result = transform_cols(document)
        res = { "data": result, "total": len(result) }
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'
    resp = make_response(jsonify(res))
    resp.status = status
    return resp

# 采集完成
@bp.route('/complete/', methods=['POST'])
def complete():
    """
        1、通过样本源编号、采集内容、采集医院查找要修改的样本源
            {
                "样本源编号": "ZSFY-TT-21000009-K-03",
                "样本类型": "细胞",
                "采集医院": "台州医院"
            }
        2、修改采集状态
    """
    doc = {}
    doc["样本源编号"] = request.json["样本源编号"]
    doc["样本类型"] = request.json["样本类型"]
    doc["采集医院"] = request.json["采集医院"]
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        newvalues = { "$set": { "采集状态":"已完成" } }
        col = client['bioSample']['collections']
        col.update_one(doc, newvalues)
        res = {"result": "修改数据成功"}
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    return resp 

# 采集发布
@bp.route('/add/', methods=['POST'])
def add():
    """
        {
            "创建时间": "2024/03/21 12:00:00",
            "年龄": "34",
            "性别": "男",
            "样本源姓名": "赵**",
            "样本源类型": "肾癌",
            "样本源编号": "ZSFY-TT-21000009-K-03",
            "知情同意": "是",
            "编号类型": "住院",
            "样本类型": "DNA",
            "样本量":"300ul",
            "采集时间": "2024/03/21 12:00:00",
            "采集医院": "浙江大学医学院附属第四医院",
            "预处理": "是",
        }
        更新collection表
    """
    doc = {}
    doc["创建时间"] = request.form["创建时间"]
    doc["年龄"] = request.form["年龄"]
    doc["性别"] = request.form["性别"]
    doc["样本源姓名"] = request.form["样本源姓名"]
    doc["样本源类型"] = request.form["样本源类型"]
    doc["样本源编号"] = request.form["样本源编号"]
    doc["知情同意"] = request.form["知情同意"]
    doc["编号类型"] = request.form["编号类型"]
    doc["样本类型"] = request.form["样本类型"]
    doc["样本量"] = request.form["样本量"]
    doc["采集时间"] = request.form["采集时间"]
    doc["采集医院"] = request.form["采集医院"]
    doc["预处理"] = request.form["预处理"]
    doc["采集状态"] = "未知"
    doc["运输状态"] = "未知"
    doc["接收状态"] = "未知"
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        col = client['bioSample']['collections']
        col.insert_one(doc)
        res = {"result": "发布成功"}
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    return resp 


# 运输发布
@bp.route('/transport/', methods=['POST'])
def transport():
    """
        1、填写表单信息
            {
                "运输方": "***公司",
                "负责人": "李**",
                "联系方式": "18622478892",
                "运出时间": "2024/03/29 12:00:00"
            }
        2、通过样本源编号、采集内容、采集医院查找要修改的样本源
            {
                "样本源编号": "ZSFY-TT-21000009-K-03",
                "样本类型": "细胞",
                "采集医院": "台州医院"
            }
        2、更新运输信息并修改运输状态
    """
    query = {}
    query["样本源编号"] = request.json["样本源编号"]
    query["样本类型"] = request.json["样本类型"]
    query["采集医院"] = request.json["采集医院"]
    doc = {}
    doc["运输方"] = request.json["运输方"]
    doc["负责人"] = request.json["负责人"]
    doc["负责人联系方式"] = request.json["负责人联系方式"]
    doc["运出时间"] = request.json["运出时间"]
    doc["运输状态"] = "运输中"
    doc["接收状态"] = "未接收"
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        newvalues = { "$set": doc }
        col = client['bioSample']['collections']
        col.update_one(query, newvalues)
        res = {"result": "修改数据成功"}
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    return resp 

# 接收样本
@bp.route('/accept/', methods=['POST'])
def accept():
    """
        1、填写表单信息
            {
                "接收人": "李**",
                "联系方式": "18622478892",
                "接收时间": "2024/03/29 12:00:00"
            }
        2、通过样本源编号、采集内容、采集医院查找要修改的样本源
            {
                "样本源编号": "ZSFY-TT-21000009-K-03",
                "样本类型": "细胞",
                "采集医院": "台州医院"
            }
        2、更新接收信息并修改运输状态、接收状态
    """
    query = {}
    query["样本源编号"] = request.json["样本源编号"]
    query["样本类型"] = request.json["样本类型"]
    query["采集医院"] = request.json["采集医院"]
    doc = {}
    doc["接收人"] = request.json["接收人"]
    doc["接收人联系方式"] = request.json["接收人联系方式"]
    doc["接收时间"] = request.json["接收时间"]
    doc["运输状态"] = "已完成"
    doc["接收状态"] = "已完成"
    doc["入库状态"] = "待入库"
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        newvalues = { "$set": doc }
        col = client['bioSample']['collections']
        col.update_one(query, newvalues)
        res = {"result": "修改数据成功"}
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    return resp 

# 展示样本信息
@bp.route('/info/', methods=['POST'])
def singleInfo():
    """
        通过样本源编号、采集内容、采集医院查找要展示的样本
        {
            "样本源编号": "ZSFY-TT-21000009-K-01",
            "样本类型": "DNA",
            "采集医院": "浙江大学医学院附属第四医院"
        }
    """
    doc = {}
    doc["样本源编号"] = request.json["样本源编号"]
    doc["样本类型"] = request.json["样本类型"]
    doc["采集医院"] = request.json["采集医院"]
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        col = client['bioSample']['collections']
        document = col.find_one(doc,{"_id":0})
        res = {"data": transform_detail(document) }
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    return resp 


# 某个样本源的所有样本
@bp.route('/<fromid>/', methods=['GET'])
def fromInfo(fromid):
    """
        通过样本源编号、采集内容、采集医院查找要展示的样本
        {
            "样本源编号": "ZSFY-TT-21000009-K-01",
        }
    """
    query = { "样本源编号": fromid }
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        col = client['bioSample']['collections']
        document = col.find(query)
        res = {"data": transform_cols(document) }
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    return resp 
