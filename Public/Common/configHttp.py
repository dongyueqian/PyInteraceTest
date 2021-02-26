import requests
from Public.Common.ReadConfigIni import ReadConfigIni
from Config import globalconfig

configPath = globalconfig.Config_path
# print(configPath)

# 通过ReadConfigIni读取全局配置文件
# ReadConfig指向ReadConfigIni类中的getConfigValue
ReadConfig = ReadConfigIni(configPath).getConfigValue
# print(ReaConfig('Http','baseurl'))

class ConfigHttp():
    def __init__(self,section,host,port,timeout):
        '''
        读取配置config.ini文件中的全局配置信息。如baseurl、端口、timeout
        :param section:Config.ini文件中的【节】
        :param host:Config.ini文件中的section节点下的name
        :param port:Config.ini文件中的section节点下的port
        :param jtimeout:Config.ini文件中的section节点下的timeout
        '''
        self.host = ReadConfig(section,host)
        self.port = ReadConfig(section,port)
        self.timeout = ReadConfig(section,timeout)
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self,url):
        ''' 拼接完整的接口测试地址'''
        self.url = self.host + url

    def set_headers(self,header):
        ''' '''
        self.headers = header

    def set_params(self,param):
        ''' '''
        self.params = param

    def set_data(self,data):
        ''' '''
        self.data = data

    def set_files(self,files):
        ''' '''
        self.files = files

    def get(self):
        '''重写get方法'''
        try:
            response = requests.get(self.url,params=self.params,headers=self.headers,timeout=float(self.timeout))
            return response
        except TimeoutError:
            return None

    def post(self):
        '''重写post方法'''
        try:
            response = requests.get(self.url,params=self.params,headers=self.headers,json=self.data,files=self.files,timeout=float(self.timeout))
            return response
        except TimeoutError:
            return None


# ===================================
# 测试代码
# ===================================

# # # host = 'https://www.baidu.com/'
# # # port = 80
# # # timeout = 2
# url = '/s'
# params = {'wd':'bela'}
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/201 00101 Firefox/66.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
#     'Accept-Encoding': 'gzip, deflate, br'
# }
#
# new = ConfigHttp('Http','baseurl','port','timeout')
# new.set_url(url)
# new.set_headers(headers)
# new.set_params(params)
#
# r = new.get()
# # print(r.text)
# print(r.status_code)