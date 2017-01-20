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

    def gen_summary(self, test_summary={}):
        summary_div = self.top_div << div(id="summary")
        summary_div << h3("测试概要")
        summary_ul = summary_div << ul()
        summary_ul << li("接口版本： {0}".format(test_summary['app_version']))
        summary_ul << li("测试地址： {0}".format(test_summary['server_host']))
        summary_ul << li("测试账号： {0} : {1}".format(test_summary['doctor_phone_num'],
                         test_summary['doctor_password']))
        summary_ul << li("测试执行开始于： <b>{0}</b> , 结束于 <b>{1}</b>, 共耗时 <b>{2}</b>".
                         format(test_summary['test_start_time'],
                                test_summary['test_end_time'], test_summary['test_elapsed_time']))
        summary_ul << li("用例统计：共有 <b>{0}</b> 条测试用例，其中执行 <b>{1}</b> 条，通过 <b>{2}</b> 条，失败 <b>{3}</b> 条".
                         format(test_summary['test_case_count'], test_summary['ran_case_count'],
                                test_summary['passed_case_count'], test_summary['failed_case_count']))

    def gen_table(self, test_results=[]):
        test_result_div = self.top_div << div(id="test_result")
        test_result_div << h3("测试结果详情")
        table_group = test_result_div << table(id="results")
        title_tr_group = table_group << tr(cl="title")
        title_tr_group << th('序号')
        title_tr_group << th('描述')
        title_tr_group << th('请求地址')
        title_tr_group << th('请求参数')
        title_tr_group << th() << div('返回结果', style="width:300px;word-wrap:break-word;")
        title_tr_group << th('期望结果')
        title_tr_group << th('测试结果')
        title_tr_group << th('备注')
        for x in test_results:
            if x['test_result'] == "通过":
                result_tr_group = table_group << tr(cl="pass")
            elif x['test_result'] == "失败":
                result_tr_group = table_group << tr(cl="fail")
            else:
                result_tr_group = table_group << tr(cl="block")
            result_tr_group << td(x['id'])
            result_tr_group << td(x['description'])
            result_tr_group << td(x['http_url'])
            result_tr_group << td(x['parameter'])
            result_tr_group << td() << div(x['http_response'], style="width:300px;word-wrap:break-word;")
            result_tr_group << td(x['expected_result'])
            result_tr_group << td(x['test_result'])
            result_tr_group << td(x['comment'])

    def gen_report(self, filename='report.html'):
        self.page << br()
        self.page.printOut(filename)


def write_result_to_html(test_results=[], test_summary={}, test_result_file=""):
    result_file = ToHTML()
    result_file.add_css()
    result_file.gen_title()
    result_file.gen_summary(test_summary)
    result_file.gen_table(test_results)
    result_file.gen_report(test_result_file)
