# -*- coding:utf-8 -*-
from utils import httputil
from project_const import *
import json


def get_doctor_login_info():
    #  获取基本数据
    login_key = httputil.geturl(const.HOST_ENCRYPTED_SERVER_URL, {'phoneNum': const.DOCTOR_PHONE}, const.DEFAULT_HEADER)
    login_key_json_data = json.loads(login_key)
    login_key_data = login_key_json_data.get("data")
    login_key = login_key_data[0].get("loginKey")
    doctor_id_db = login_key_data[0].get("doctorId")
    # 获得密码加密结果
    encrypted_pwd = httputil.geturl(const.HOST_GEN_LOGIN_KEY_URL, {'password': const.DOCTOR_PWD})
    # 开始登录
    login_parameter = {
        'doctorId': doctor_id_db,
        'loginKey': login_key,
        'password': encrypted_pwd,
        'deviceSN': const.DEVICE_SN
    }
    login_info = httputil.geturl(const.HOST_LOGIN_URL, login_parameter, headers=const.DEFAULT_HEADER)
    login_info_json_data = json.loads(login_info)
    login_info_data = login_info_json_data.get("data")
    token = login_info_data[0].get("token")
    doctor_id = login_info_data[0].get("doctorId")
    # 医生登录结束,保存相关数据
    default_parameter = {
        'token': token,
        'id': doctor_id,
        'doctorId': doctor_id
    }
    return default_parameter
