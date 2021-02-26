import os
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from Config import globalconfig
from Public.Common.ReadConfigIni import ReadConfigIni

# [email]
# mail_server = smtp.qq.com
# sender_qq = 874974405@qq.com
# pwd = tlckctstszdibbbc
# receiver = 874974405@qq.com

#调用Config.ini文件
configpath = globalconfig.Config_path

#通过ReadConfigIni读取Config.ini文件内容
ReadConfig = ReadConfigIni(configpath).getConfigValue

def sendReport(file_new):
    with open(file_new,'rb') as f:
        mail_body = f.read()

    host_server = ReadConfig('email','mail_server')
    sender_qq = ReadConfig('email','sender_qq')
    pwd = ReadConfig('email','pwd')
    send_qq_email = sender_qq = ReadConfig('email','sender_qq')  #????????????????/
    receiver = ReadConfig('email','receiver')

    mail_title = '接口自动化测试报告' #邮件标题

    #邮件正文的内容
    msg = MIMEMultipart()
    msg['Subject'] = Header(mail_title,'utf-8')
    msg['From'] = send_qq_email

    msg.attach(MIMEText(mail_body,'html','utf-8')) # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码


    #ssl登录
    smtp = SMTP_SSL(host_server)
    smtp.ehlo(host_server)
    smtp.login(sender_qq,pwd)

    smtp.sendmail(send_qq_email,receiver,msg.as_string())

    smtp.quit()
    print('result had send out!')

def newReport(testReport):
    '''
    查找最新的测试报告
    :param testReport:
    :return:
    '''
    lists = os.listdir(testReport)
    newlists = sorted(lists)
    file_new = os.path.join(testReport,newlists[-1])
    print(file_new)
    return file_new

# =================================================
# 测试代码
# 验证以上函数的正确性
# =================================================
if __name__ == '__main__':
    testReport = '/Users/dongyueqian/PycharmProjects/InterfaceFrameWork/Report/TestReport'
    new_report = newReport(testReport)
    print(new_report)
    sendReport(new_report)