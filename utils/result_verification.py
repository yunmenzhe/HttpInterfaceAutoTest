# -*-coding:utf-8-*-
from project_const import *


def get_result(verification_method, actual_result, expected_result):
    if verification_method == const.CASE_VERIFICATION_METHOD_EQUALS:
        return assert_equals(actual_result, expected_result)
    elif verification_method == const.CASE_VERIFICATION_METHOD_CONTAINS:
        return assert_contains(actual_result, expected_result)


def assert_equals(actual_result, expected_result):
    if actual_result == expected_result:
        return True
    else:
        return False


def assert_contains(actual_result, expected_result):
    if expected_result in actual_result:
        return True
    else:
        return False
