# -*-coding:utf-8-*-
from utils.excel_util import get_row_value,get_test_case_count
import case_execution, userlogin, sys, result_to_html

# 获得测试用例文件绝对路径
# 读取测试用例数量
# 逐条读取测试用例
# 执行单条测试用例
# 测试用例保存到测试结果中(用于发送的结果，用于执行前置用例的结果)
# 生成测试报告
