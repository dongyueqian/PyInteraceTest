import os
from Public.Common.ReadConfigIni import ReadConfigIni

# 配置文件的读取
# 获取当前目录的路径
file_path = os.path.split(os.path.realpath(__file__))[0]
# print(file_path)

# 获取Config.ini文件
read_config = ReadConfigIni(os.path.join(file_path,'Config.ini') )
# print(read_config)

# 获取Config.ini文件的路径
Config_path = os.path.join(file_path,'Config.ini')
# print(Config_path)

# 读取工程的路径
project_path = read_config.getConfigValue('project','project_path')
# print(project_path)

# 日志路径
log_path = os.path.join(project_path,'Report','Log')
# print(log_path)

# 测试报告路径
report_path = os.path.join(project_path,'Report','TestReport')
# print(report_path)

# 测试数据路径
testCase_path = os.path.join(project_path,'TestCase')
# print(testCase_path)

data_path = os.path.join(project_path,'Data','TestData')
# print(data_path)

