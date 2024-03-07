#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
auth.py
实现登录功能和密码修改功能
"""

from flask import Blueprint, request, current_app, make_response, jsonify, g
from flask.views import MethodView
from pymongo import MongoClient
import time
from application.util.util_auth import create_md5, create_token, require_token

# blueprint前缀， 该文件下的接口地址修改为 ~/auth
bp = Blueprint("auth", __name__, url_prefix="/auth")


class Auth(MethodView):
    def post(self):
        """用户登录

        @@@
        ### form表单
        |  form | nullable | request type | type |  remarks |
        |-------|----------|--------------|------|----------|
        | username    |  false   |    body      | str  | 用户id    |
        | password  |  false   |    body   | str  | 用户密码 |

        ### request
        ```json
        {"id": "xxx", "password": "xxx"}
        ```

        ### return
        ```json
        -   200 OK 登录成功
        {'uid': xxx, 'name': xxx, 'token': xxx, 'expire': xxx}
        -   401 Unauthorized 登录失败
        -   500 ServerError 服务器错误
        {'error': xxx}
        ```
        @@@
        """
        user_id = request.form["username"]
        password = request.form["password"]
        password_md5 = create_md5(password)  # md5加密，mongodb中存储密码md5形式，防止被盗取
        print(password_md5)
        try:
            client = MongoClient(host='localhost', port=27017)
            db = client['bioSample']
            doc = db["users"].find_one({"uid": user_id})
            if doc and password_md5 == doc["password"]:
                ut = int(time.time()) + current_app.config["TOKEN_EXPIRE"]
                expire = str(ut) + "000"  # 超时时间的时间戳，以毫秒为单位，在token中相应的字段是以秒为单位
                token = create_token(
                    user_id,
                    doc["name"],
                    doc["granted"],
                    current_app.config["TOKEN_EXPIRE"],
                    current_app.config["TOKEN_SECRET"],
                )
                res = {
                    "uid": user_id,
                    "name": doc["name"],
                    "token": token,
                    "expire": expire,
                }
                status = "200 OK"  # 登录成功
            else:
                status = "401 Unauthorized"  # 登录失败
                res = {}
        except Exception as err:
            status = "500 ServerError"  # 服务器错误
            res = {"error": str(err)}

        resp = make_response(jsonify(res))
        resp.status = status
        return resp

    @require_token
    def put(self):
        """修改密码

        @@@
        ### form表单
        |  form | nullable | request type | type |  remarks |
        |-------|----------|--------------|------|----------|
        | Authorization |  false   |    header   | str  | token   |
        | password    |  false   |    body   | str  | 旧密码   |
        | new_password  |  false   |    body   | str  | 新密码 |

        ### request
        ```json
        header:
        {"Authorization": "xxx"}
        body:
        {"password": "xxx", "new_password": "xxx"}
        ```

        ### return
        ```json
        -   200 OK 修改成功
        -   403 Password error 新密码与原密码相同
            {'error': "Password error"}
        -   500 ServerError 服务器错误
            res = {'error': "ServerError"}
        ```
        @@@
        """
        user_id = g.token_info["user_id"]
        password = request.form.get("password")
        new_password = request.form.get("new_password")
        if password == new_password:
            resp = make_response(jsonify({"error": "新密码与原密码相同"}))
            resp.status = "403 Password error"
            return resp
        password_md5 = create_md5(password)  # md5加密，防止密码被盗取
        new_password_md5 = create_md5(new_password)

        try:
            client = MongoClient(
                host=current_app.config["DB_HOST"], port=current_app.config["DB_PORT"]
            )  # 连接mongodb
            db = client["emr"]
            doc = db["users"].find_one({"uid": user_id})
            if doc and password_md5 == doc["password"]:  # 判断密码是否正确
                db["users"].update_one(
                    {"uid": user_id}, {"$set": {"password": new_password_md5}}
                )
                resp = make_response(jsonify({}))
                resp.status = "200 OK"
                return resp
            else:
                status = "403 Password error"
                res = {"error": "Password error"}

        except Exception as err:
            status = "500 ServerError"
            res = {"error": str(err)}
        resp = make_response(jsonify(res))
        resp.status = status
        return resp


bp.add_url_rule("/", view_func=Auth.as_view("/"))
