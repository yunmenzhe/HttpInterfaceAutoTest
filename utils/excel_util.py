# -*-coding:utf-8-*-
import xlrd


def open_excel(file='file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))


# 根据索引获取用例总数:file：Excel文件路径; by_index：表的索引
def get_test_case_count(file='file.xls', by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    return table.nrows - 1


# 根据行id获取单行数据
def get_row_value(file='file.xls', row_num=1, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    row = table.row_values(row_num)
    return row


def main():
    get_row_value()

if __name__ == "__main__":
    main()
