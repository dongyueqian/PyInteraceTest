import xlrd
from xlutils.copy import copy
from Config import globalconfig
import os

# =========================
# 对Excel进行封装
# 新增像Excel中写入数据
# =========================

data_path = globalconfig.data_path
# print(data_path)

class DoExcel():
    def __init__(self,filename,sheetname):
        '''

        :param filename:
        :param sheetname:
        '''
        self.Filename = os.path.join(data_path,filename)
        self.workbook = xlrd.open_workbook(self.Filename)
        self.sheet = self.workbook.sheet_by_name(sheetname)

    def get_row_num(self,cols_num,case_id):
        '''
        作用：指定检索某列中的哪个值与case_id（某列中某个单元格的值）相匹配，从而返回case_id所在的行号
        :param clos_num:检索哪一列
        :param case_id:
        :return:返回行号
        '''
        cols = self.sheet.col_values(cols_num)
        colnum = 0
        for col_data in cols:
            if col_data == case_id:
                break
            colnum += 1
        return colnum  #自增后返回case_id所在的行号


    def get_rowline_data(self,row):
        '''
        作用：根据get_row_num返回的行号，获取某行的值
        :param row:传递行号，在get_row_num返回的行号
        :return:
        '''
        rowline_data = self.sheet.row_values(row)
        return rowline_data

    def read_excel(self,rownum,colnum):
        '''
        作用：获取某个单元格的值
        :param rownum: 行号
        :param colnum: 列号
        :return: 返回单元格的值
        '''
        value = self.sheet.cell(rownum,colnum)
        return value.value

    def write_excel(self,sheetnum,row,col,value):
        '''
        作用：往Excel写数据
        :param sheetnum:sheet的编号，从0开始
        :param row:行号
        :param col:列号
        :param value:值
        :return:
        '''
        newworkbook = xlrd.open_workbook(self.Filename)
        newbook = copy(newworkbook)   #拷贝Excel
        sheet = newbook.get_sheet(sheetnum)

        sheet.write(row,col,value)
        newbook.save(self.Filename)   #保存Excel



# ================================
# 测试代码
# 验证DoExcel的正确性
# ================================

# if __name__ == '__main__':
#     excel = DoExcel('case.xls','Sheet1')
#     row = excel.get_row_num(0,'weixin-001')
#     print(row)
#     rowdata = excel.get_rowline_data(row)
#     print(rowdata)
#     print(50*'=')
#     excel.write_excel(0,5,5,'888')