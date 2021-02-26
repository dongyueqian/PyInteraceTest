import configparser
import os
import codecs

class ReadConfigIni():
    '''
    作用：读取Config配置文件
    '''
    def __init__(self,filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    def getConfigValue(self,section,name):
        value = self.cf.get(section,name)
        return value #返回name的值


# ===============================
# 测试代码,验证ReaConfigIni的正确性
# ===============================
# file_path = os.path.split(os.path.realpath(__file__))[0]
# print(file_path)
#
# read_config = ReaConfigIni(os.path.join(file_path,'Config.ini'))
# # print(os.path.join(file_path,'Config.ini'))
# print(read_config)
#
# value = read_config.getConfigValue('Http','baseurl')  #获取baseurl的值
# print(value)