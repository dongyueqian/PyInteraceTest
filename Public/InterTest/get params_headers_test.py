import requests
from Public.Common.configHttp import ConfigHttp
from Public.Common.DoExcel import DoExcel

# ==================================
# 1、原有接口的测试用例
# ==================================
# url = 'https://www.baidu.com/s'
# params = {'wd':'bela'}
# headers = {
#             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0",
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#             "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#             "Accept-Encoding": "gzip, deflate, br"
#         }
#
# r = requests.get(url,params=params,headers=headers)
# print(r.status_code)


# =======================================
# 2、通过测试框架测试
# =======================================
# url = '/s'
# params = {'wd':'bela'}
# headers = {
#             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0",
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#             "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#             "Accept-Encoding": "gzip, deflate, br"
#         }
# newrequest = ConfigHttp('Http','baseurl','port','timeout')
# newrequest.set_params(params)
# newrequest.set_headers(headers)
# newrequest.set_url(url)
# r = newrequest.get()
# print(r.status_code)
# print(r.text)


# =======================================
# 3、从excel中读取数据，读取url
# =======================================
# params = {'wd':'bela'}
# headers = {
#             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0",
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#             "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#             "Accept-Encoding": "gzip, deflate, br"
#         }
#
# excel = DoExcel('case.xls','Sheet1')
#
# rownum = excel.get_row_num(0,'bd-001') #行号
# url = excel.read_excel(rownum,2)
#
# newrequest = ConfigHttp('Http','baseurl','port','timeout')
# newrequest.set_url(url)
# newrequest.set_params(params)
# newrequest.set_headers(headers)
# r = newrequest.get()
# print(r.status_code)
#
# print('=====================================')
# # 将实际结果写入Excel
# excel.write_excel(0,rownum,10,r.status_code)


# =======================================
# 4、目标：判断写入实际结果的单元格是否为空，为空则写入，不为空则不写入
# =======================================
# params = {'wd':'bela'}
# headers = {
#             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0",
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#             "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#             "Accept-Encoding": "gzip, deflate, br"
#         }
# excel = DoExcel('case.xls','Sheet1')
# rownum = excel.get_row_num(0,'bd-001') #行号
# url = excel.read_excel(rownum,2)
#
# newrequest = ConfigHttp('Http','baseurl','port','timeout')
# newrequest.set_url(url)
# newrequest.set_params(params)
# newrequest.set_headers(headers)
# r = newrequest.get()
# # print(r.status_code)
#
# cell_value = excel.read_excel(rownum,10)
# if cell_value:
#     print('不为空',cell_value)
#     excel.write_excel(0,rownum,10,r.status_code)
#
# else:
#     print('为空')
#     excel.write_excel(0,rownum,10,r.status_code)

# =======================================
# 4、目标：封装成类
# =======================================
url = '/s'
params = {'wd':'bela'}
headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br"
        }

class BaiduGet():
    def __init__(self):
        '''
        实例化DoExcel、ConfigHttp
        '''
        self.excel = DoExcel('case.xls','Sheet1')
        self.rownum = self.excel.get_row_num(0,'bd-001') #行号
        # self.excel.write_excel(0,self.rownum,10,None)
        self.newrequest = ConfigHttp('Http','baseurl','port','timeout')
        self.url = self.excel.read_excel(self.rownum,2)

    def baidu_get(self):
        self.newrequest.set_url(self.url)
        self.newrequest.set_headers(headers)
        self.newrequest.set_params(params)
        r = self.newrequest.get()
        self.excel.write_excel(0,self.rownum,10,r.status_code)
        return r.status_code

baidu = BaiduGet()
print(baidu.baidu_get())