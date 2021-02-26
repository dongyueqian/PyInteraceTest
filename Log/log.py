import logging
import os
import time
from Config import globalconfig

log_path = globalconfig.log_path
print(log_path)

class Logger():

    def __init__(self,logger,CmdLogLevel,FileLogLevel):
        '''
        日志模块:对日志的操作进行封装，对日志的级别再次封装
        :param logger:
        :param CmdLogLevel: 设定控制台输出日志的级别
        :param FileLogLevel: 设定文件输出日志的级别
        '''
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

        #设定日志文件的名称
        self.LogFileName = os.path.join(log_path,'{0}.log'.format(time.strftime('%Y-%m-%d')))

        #设置控制台日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(CmdLogLevel)

        #设置文件日志
        fh = logging.FileHandler(self.LogFileName)
        fh.setFormatter(fmt)
        fh.setLevel(FileLogLevel)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)

# ==============================================
# 测试代码
# 验证以上代码的正确性
# ==============================================
if __name__ == '__main__':
    logger = Logger('fox',CmdLogLevel=logging.INFO,FileLogLevel=logging.ERROR)
    logger.debug('debug message')
    logger.info('info message')
    logger.war('war message')
    logger.error('error message')
    logger.cri('critical message')