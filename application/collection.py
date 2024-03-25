from pymongo import MongoClient
from flask import Blueprint, current_app, request, make_response, jsonify
from .util.util_collection import transform_cols, transform_detail, transform_static,transform_id

bp = Blueprint('collection', __name__, url_prefix='/collection')

# 所有采集需求
@bp.route('/',methods=['GET'])
def all_collections():
    """
        {
            "年龄": "34",
            "性别": "男",
            "接收人": "张**",
            "接收人联系方式": "13244658712",
            "接收时间": "20240404",
            "接收状态": "已完成",
            "样本创建时间": "20240321",
            "样本数量": "1管",
            "样本源姓名": "赵**",
            "样本源类型": "肾癌",
            "样本源编号": "ZSFY-TT-21000009-K-01",
            "样本编号": "-",
            "样本量": "100ul",
            "知情同意": "是",
            "研究用途": "miRNA测序",
            "负责人": "李**",
            "负责人联系方式": "15522471452",
            "运出时间": "20240331",
            "运输方": "医药专运",
            "运输状态": "已完成",
            "采集医院": "浙江大学医学院附属第四医院",
            "采集时间": "20240321",
            "采集状态": "已完成",
            "预处理": "是"
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
                "样本编号": "TZYY-QT1-20240328-1"
            }
        2、修改采集状态
    """
    doc = {}
    doc["样本编号"] = request.form["样本编号"]
    date = request.form["采集时间"]
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        newvalues = { "$set": { "采集状态":"已完成","采集时间": date } }
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
            "创建时间": "20240318",
            "年龄": "34",
            "性别": "男",
            "样本源姓名": "赵**",
            "样本源类型": "肾癌",
            "样本源编号": "ZJU4H-QX2",
            "样本编号": "ZJU4H-QX2-20240321-1/2/3"
            "知情同意": "是",
            "采集时间": "20240321",
            "研究用途":"组织细胞分子等实验验证",
            "其他":"",
            "体积":"300",
            "体积单位":"ul",
            "数量":"3",
            "数量单位":"管",
            "采集医院": "浙江大学医学院附属第四医院",
            "预处理": "是",
        }
        更新collection表
    """
    doc = {}
    id = request.form["样本源编号"]
    doc["样本源编号"] = id
    doc["样本创建时间"] = request.form["样本创建时间"]
    doc["年龄"] = request.form["年龄"]
    doc["性别"] = request.form["性别"]
    doc["样本源姓名"] = request.form["样本源姓名"]
    doc["样本源类型"] = request.form["样本源类型"]
    doc["知情同意"] = request.form["知情同意"]
    valume1 = request.form["体积"]
    valume2 = request.form["体积单位"]
    doc["样本量"] = valume1+valume2
    number1 = request.form["数量"]
    number2 = request.form["数量单位"]
    doc["样本数量"] = number1+number2
    doc["研究用途"] = request.form["研究用途"]
    doc["其他"] = request.form["其他"]
    doc["采集时间"] = request.form["采集时间"]
    date = request.form["采集时间"]
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
        for item in range(int(number1)):
            doc["_id"] = transform_id(id,item,date)
            doc["样本编号"] = transform_id(id,item,date)
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
        2、通过样本编号查找要修改的样本源
            {
                "样本编号": "TZYY-QT1-20240328-1"
            }
        2、更新运输信息并修改运输状态
    """
    query = {}
    query["样本编号"] = request.form["样本编号"]
    doc = {}
    doc["运输方"] = request.form["运输方"]
    doc["负责人"] = request.form["负责人"]
    doc["负责人联系方式"] = request.form["负责人联系方式"]
    doc["运出时间"] = request.form["运出时间"]
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
        2、通过样本源编号查找要修改的样本源
            {
                "样本编号": "TZYY-QT1-20240328-1",
            }
        2、更新接收信息并修改运输状态、接收状态
    """
    query = {}
    query["样本编号"] = request.form["样本编号"]
    doc = {}
    doc["接收人"] = request.form["接收人"]
    doc["接收人联系方式"] = request.form["接收人联系方式"]
    doc["接收时间"] = request.form["接收时间"]
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
            "采集医院": "浙江大学医学院附属第四医院"
        }
    """
    doc = {}
    doc["样本源编号"] = request.form["样本源编号"]
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
            "样本源编号": "	TZYY-QT1",
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

# 按医院统计样本总数
@bp.route('/hospital/', methods=['GET'])
def hospitalInfo():
    """
        通过采集医院查找要展示的样本
        {
            "采集医院": "台州医院",
        }
    """
    result1=[]
    result2=[]
    result3=[]
    result4=[]
    query1 = { "采集医院": "浙江大学医学院附属第一医院" }
    query2 = { "采集医院": "浙江大学医学院附属第四医院" }
    query3 = { "采集医院": "台州医院" }
    query4 = { "采集医院": "浙江大学医学院附属儿童医院" }
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        col = client['bioSample']['collections']
        result1 = transform_static(col.find(query1,{"_id":0}),"浙江大学医学院附属第一医院")
        result2 = transform_static(col.find(query2,{"_id":0}),"浙江大学医学院附属第四医院")
        result3 = transform_static(col.find(query3,{"_id":0}),"台州医院")
        result4 = transform_static(col.find(query4,{"_id":0}),"浙江大学医学院附属儿童医院")
        res = {"data": [
            result1,
            result2,
            result3,
            result4,
        ] }
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    return resp