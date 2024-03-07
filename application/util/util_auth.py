#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
util_auth.py
实现token的打包和解包，用户密码加密
"""
import hashlib
import time
import functools
import jwt
from flask import request, current_app, make_response, g


def create_md5(source):
    """
    生成一个字符串的md5码
    :param source: 原始字符串
    :return: 生成的md5码
    """

    m = hashlib.md5()
    m.update(source.encode("utf-8"))
    return m.hexdigest()


def create_token(uid, user_name, scopes, expire_interval, secret):
    """
    创建token
    :param uid: 用户ID
    :param user_name: 用户名
    :param scopes: 权限范围
    :param expire_interval: token的超时时间
    :param secret: token的加密密码
    :return: 生成的token
    """
    now_time = int(time.time())
    payload = {
        "iss": "BIT Lab, ZUST",
        "iat": now_time,  # 当时的时间戳，以秒为单位
        "exp": now_time + expire_interval,  # token的超时期限，以秒为单位
        "aud": "bit.zust.edu.cn",
        "user_id": uid,
        "nickname": user_name,
        "username": user_name,
        "scopes": scopes,
    }
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token


def require_token(func):
    """
    需要验证token请求的装饰器。
    :param func: 被装饰的函数
    :return: 直接生成响应返回，或调用原请求函数返回
    """

    @functools.wraps(func)
    def wrapper(*args, **kw):
        try:
            if current_app.config["TOKEN_CHECK"]:
                token = request.headers.get("Authorization")
                g.token_info = decode_token(
                    token, current_app.config["TOKEN_SECRET"]
                )  # 解码得到全局的用户信息

                now_time = int(time.time())
                if now_time > g.token_info["exp"]:
                    resp = make_response("TOKEN过期", 401)
                    return resp
        except Exception as err:
            resp = make_response("TOKEN错误：" + str(err), 401)
            return resp

        return func(*args, **kw)

    return wrapper


def decode_token(token, secret):
    """
    使用token和秘钥对用户的全局信息进行解码
    :param token: 前端传回的token
    :param secret: config.py文件中的秘钥
    :return: 用户的全局信息
    """
    result = jwt.decode(token, secret, audience="bit.zust.edu.cn", algorithms=["HS256"])
    return result
