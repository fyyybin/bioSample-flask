from pymongo import MongoClient
from flask import Blueprint, current_app, request, make_response, jsonify
from .util.util_analyse import transform_analyse

bp = Blueprint('analyse', __name__, url_prefix='/analyse')

# 所有采集需求
@bp.route('/',methods=['GET'])
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
    client = MongoClient(
        host = current_app.config["DB_HOST"], port = current_app.config["DB_PORT"]
    )
    try:
        document = client['bioSample']['analyse'].find()
        result = transform_analyse(document)
        res = { "data": result, "total": len(result) }
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'
    resp = make_response(jsonify(res))
    resp.status = status
    return resp
