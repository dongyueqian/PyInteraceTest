import requests

# ==========================================
# 1、常规方式获得access_token
# ==========================================
url = 'https://api.weixin.qq.com/cgi-bin/token'
params = {
    'grant_type':'client_credential',
    'appid':'wx7fd8b53eacf391af',
    'secret':'fca5eae150a05d2a3e95c9399c0d7500'
}

r = requests.get(url=url,params=params)
print(r.text)

# ==========================================
# 2、用框架获得access_token
# ==========================================

# from Public.Common.configHttp import ConfigHttp
# from Public.Common.DoExcel import DoExcel
#
# url = '/cgi-bin/token'
# params = {
#     'grant_type':'client_credential',
#     'appid':'wx7fd8b53eacf391af',
#     'secret':'fca5eae150a05d2a3e95c9399c0d7500'
# }
#
# class GetToken():
#     '''
#     将access_token存放在外部Excel
#     '''
#     def __init__(self):
#
#         # 初始化，获得Excel
#
#         self.excel = DoExcel('case.xls','Sheet1') #实例化DoExcel
#         self.rownum = self.excel.get_row_num(0,'weixin-001')
#         self.newquest = ConfigHttp('Http2','baseurl','port','timeout')
#
#     def get_token(self):
#         self.newquest.set_url(url)
#         self.newquest.set_params(params)
#         r = self.newquest.get()
#         self.excel.write_excel(0,self.rownum,6,r.json()['access_token'])
#         return r.json()['access_token']
#
# WeiXinGetToken = GetToken()
# print(WeiXinGetToken.get_token())

