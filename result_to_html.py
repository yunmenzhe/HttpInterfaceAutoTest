# -*-coding:utf-8-*-
from pyh import *


class ToHTML:
    def __init__(self):
        self.page = PyH('医生端接口自动化测试结果')
        self.top_div = self.page << div(align="center")

    def add_css(self):
        self.page.addCSS("test_result.css")

    def gen_title(self):
        self.top_div << div(id="title") << h2("医生端接口自动化测试结果")

    def gen_summary(self, test_environment={}):
        summary_div = self.top_div << div(id="summary")
        summary_div << h3("测试结果详情")
        summary_dict = {
            'doctor_phone_num': "医生手机号",
            'doctor_password': "登录用密码",
            'server_host': "服务器端口",
            'app_version': "系统版本",
            'test_start_time': "测试开始时间",
            'test_end_time': "测试结束时间",
            'test_elapsed_time': "测试耗时",
            'ran_case_count': "测试执行用例数",
            'test_case_count': "测试用例总数",
            'passed_case_count': "通过用例数",
            'failed_case_count': "失败用例数"
        }
        summary_ul = summary_div << ul
        for k, v in summary_dict:
            summary_ul << li("{1}：{2}".format(v, test_environment[k]))

    def gen_table(self, test_results=[]):
        test_result_div = self.top_div << div(id="test_result")
        test_result_div << h3("测试结果详情")
        table_group = test_result_div << table(id="results")
        title_tr_group = table_group << tr(cl="title")
        title_tr_group << td('序号')
        title_tr_group << td('描述')
        title_tr_group << td('请求地址')
        title_tr_group << td('请求参数')
        title_tr_group << td('返回结果')
        title_tr_group << td('期望结果')
        title_tr_group << td('测试结果')
        title_tr_group << td('备注')
        for x in test_results:
            if x['test_result'] == "通过":
                result_tr_group = table_group << tr(cl="pass")
            elif x['test_result'] == "失败":
                result_tr_group = table_group << tr(cl="fail")
            else:
                result_tr_group = table_group << tr(cl="block")
            result_tr_group << td(x['id'])
            result_tr_group << td(x['description'])
            result_tr_group << td(x['url'])
            result_tr_group << td(x['parameter'])
            result_tr_group << td(x['http_response'])
            result_tr_group << td(x['expected_result'])
            result_tr_group << td(x['test_result'])
            result_tr_group << td(x['test_result_comment'])

    def gen_report(self, filename='report.html'):
        self.page << '结束:'
        try:
            self.page << 'finished'
        except:
            self.page << 'unfinished'
        self.page << br()
        self.page.printOut(filename)


def write_result_to_html(test_results=[], test_environment={}, test_result_html_file=""):
    result_file = ToHTML()
    result_file.add_css()
    result_file.gen_title()
    result_file.gen_summary(test_environment)
    result_file.gen_table(test_results)
    result_file.gen_report(test_result_html_file)
