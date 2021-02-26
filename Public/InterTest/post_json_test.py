import requests

# ====================================
# 1、常规方式群发消息
# ====================================
# url = 'https://api.weixin.qq.com/cgi-bin/message/mass/sendall'
# data = {
#     "filter": {
#         "is_to_all": True
#     },
#     "text": {
#         "content": "9909"
#     },
#     "msgtype": "text"
# }
# params = {
#     'access_token':'20_ysBlPTpD890TAK1btHfS7tj_xaYDuL-r0cGAUYETXMkE6_x7fJKGFjTiuS6fZaa5D-Dp78npWdKXtmjX7fvMGofu5vViT8JBm5fO0op4NbGRtmezwwd6kZf_FdILWNjABAZKB'
# }
#
# r= requests.post(url=url,json=data,params=params)
# print(r.text)

# ====================================
# 2、用测试框架 群发消息，封装
# ====================================
from Public.Common.configHttp import ConfigHttp
from Public.Common.DoExcel import DoExcel

url = '/cgi-bin/message/mass/sendall'
data = {
    "filter": {
        "is_to_all": True
    },
    "text": {
        "content": "9909"
    },
    "msgtype": "text"
}
params = {
    'access_token':'20_ysBlPTpD890TAK1btHfS7tj_xaYDuL-r0cGAUYETXMkE6_x7fJKGFjTiuS6fZaa5D-Dp78npWdKXtmjX7fvMGofu5vViT8JBm5fO0op4NbGRtmezwwd6kZf_FdILWNjABAZKB'
}

excel = DoExcel('case.xls', 'Sheet1')  # 实例化DoExcel
rownum = excel.get_row_num(0, 'weixin-002') #获取行号
newquest = ConfigHttp('Http2', 'baseurl', 'port', 'timeout')

newquest.set_url(url)
newquest.set_params(params)
newquest.set_data(data)
r = newquest.post()
print(r.json())
