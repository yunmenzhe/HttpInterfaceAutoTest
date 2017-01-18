# -*-coding:utf-8-*-
from utils.httputil import geturl, posturl
from project_const import *
from utils.result_verification import get_result


# 执行测试用例,返回dict格式的测试结果
def execute_case(case=[], default_parameter={}, headers={}, prefix_result=[]):
    test_case = get_case(case)
    test_result = test_case
    data = default_parameter + test_case['parameter']
    if test_case['prefix_case_id'] == -1:
        test_result['test_result'] = execute_request(test_case, data, headers)
    else:
        for x in prefix_result:
            if x['id'] == test_case['prefix_case_id']:
                prefix_case_result = x['test_result']
                if prefix_case_result == "通过":
                    test_result['test_result'] = execute_request(test_case, data, headers)
                else:
                    test_result['test_result'] = x['test_result']
    return test_result


# 发送请求并验证测试结果
def execute_request(test_case={}, data={}, headers={}):
    if test_case['execution'] == "YES":
        if test_case['method'] == const.CASE_HTTP_METHOD_GET:
            http_response = geturl(test_case['url'], data, headers)
        elif test_case['method'] == const.CASE_HTTP_METHOD_POST:
            http_response = posturl(test_case['url'], data, headers)
        return http_response
        test_result_bool = get_result(test_case['verification_method'], http_response, test_case['expected_result'])
        if test_result_bool:
            return "通过"
        else:
            return "失败"
    else:
        return "跳过"


# 解析从excel读取得到的测试用例内容
def get_case(case=[]):
    # 组成http_url
    url = case[const.CASE_HTTP_URL]
    if case[const.CASE_SERVER] == const.const.CASE_SERVER_AD_SERVER:
        http_url = const.HOST_AD_SERVER + url
    elif case[const.CASE_SERVER] == const.const.CASE_SERVER_IM_SERVER:
        http_url = const.HOST_IM_SERVER + url
    else:
        http_url = url
    # prefix_id
    if case[const.CASE_PREFIX_CASE_ID]:
        prefix_id = int(case[const.CASE_PREFIX_CASE_ID])
    else:
        prefix_id = -1
    # 获取测试用例数据放入字典中
    test_case = {
        'id': int(case[const.CASE_ID]),
        'description': case[const.CASE_DESCRIPTION],
        'url': http_url,
        'method': case[const.CASE_HTTP_METHOD],
        'parameter': case[const.CASE_PARAMETER],
        'verification_method': case[const.CASE_VERIFICATION_METHOD],
        'expected_result': case[const.CASE_EXPECTED_RESULT],
        'prefix_case_id': prefix_id,
        'execution': case[const.CASE_EXECUTION],
        'comment': case[CASE_COMMENT]
    }
    return test_case


