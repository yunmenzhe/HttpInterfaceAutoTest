# -*-coding:utf-8-*-
from utils.excel_util import get_row_value, get_test_case_count
import case_execution
import userlogin
import result_to_html
from project_const import *
import os
import sys
import time


def get_time_str():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def get_date():
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


# 计算测试消耗时间
def get_elapsed_time(start_time, end_time):
    time_elapsed_in_milli = int(end_time - start_time)
    if time_elapsed_in_milli / 1000 >= 3600:
        time_elapsed_in_hour = time_elapsed_in_milli / 3600000
        time_elapsed_in_min = time_elapsed_in_milli / 60000 - time_elapsed_in_hour * 60
        time_elapsed_in_second = time_elapsed_in_milli / 1000 - time_elapsed_in_hour * 3600 - time_elapsed_in_min * 60
        return "测试消耗 {1} 小时 {2} 分钟 {3} 秒".format(time_elapsed_in_hour, time_elapsed_in_min, time_elapsed_in_second)
    elif time_elapsed_in_milli / 1000 >= 60:
        time_elapsed_in_min = time_elapsed_in_milli / 60000
        time_elapsed_in_second = time_elapsed_in_milli / 1000 - time_elapsed_in_min * 60
        return "测试消耗 {1} 分钟 {2} 秒".format(time_elapsed_in_min, time_elapsed_in_second)
    else:
        return "测试消耗 {1} 秒".format(time_elapsed_in_milli/1000)


def run_cases():
    # 记录测试相关数据
    test_environment = {
        "doctor_phone_num": const.DOCTOR_PHONE,
        "doctor_password": const.DOCTOR_PWD,
        "server_host": const.HOST_AD_SERVER,
        "app_version": const.const.DEFAULT_HEADER['_v']
    }
    default_parameters = userlogin.get_doctor_login_info()
    test_results = []
    case_absolute_file = os.path.abspath(const.CASE_FILE_PATH)
    test_case_count = get_test_case_count(case_absolute_file, 0)
    test_environment['test_case_count'] = test_case_count
    # 记录测试开始时间
    test_start_time = time.time()
    test_environment['test_start_time'] = get_time_str()
    for case in (1, test_case_count + 1):
        test_case = get_row_value(case_absolute_file, row_num=case, by_index=0)
        per_case_result = case_execution.execute_case(test_case, default_parameters, const.DEFAULT_HEADER, test_results)
        test_results.append(per_case_result)
    # 记录测试结束时间
    test_end_time = time.time()
    test_environment['test_end_time'] = get_time_str()
    # 测试消耗时间
    test_environment['test_elapsed_time'] = get_elapsed_time(test_start_time,test_end_time)
    # 统计测试用例执行结果
    passed_case_count = 0
    failed_case_count = 0
    blocked_case_count = 0
    for case_result in test_results:
        if case_result['test_result'] == '通过':
            passed_case_count += 1
        elif case_result['test_result'] == '失败':
            failed_case_count += 1
        else:
            blocked_case_count += 1
    test_environment['ran_case_count'] = passed_case_count + failed_case_count
    test_environment['passed_case_count'] = passed_case_count
    test_environment['failed_case_count'] = failed_case_count
    # 测试结果html文件绝对路径，在项目的根目录下面
    try:
        jenkins_version = sys.argv[0]
    except:
        print('无默认参数，使用自动的文件路径')
    test_result_html_file = "{1}/doctor_auto_test{2}-{3}.html".format(os.getcwd(), get_date(), jenkins_version)
    # 生成测试结果html文件
    result_to_html.write_result_to_html(test_results, test_environment, test_result_html_file)


def main():
    run_cases()


if __name__ == "__main__":
    main()

