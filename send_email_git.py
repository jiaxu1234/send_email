# !/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

def hotmail_send(subject,text):
    # 第三方 SMTP 服务
    mail_user = "*********************"  #账号
    mail_pass = "***********"#密码

    sender = '******************'#发件人地址
    receivers = ['*******']  # 接收邮件地址，可设置为你的QQ邮箱或者其他邮箱

    time_china = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print time_china

    message = MIMEText(text + '\r\n'+time_china, 'plain', 'utf-8')
    message['From'] = Header("自动发送", 'utf-8')
    message['To'] = Header("auto", 'utf-8')

    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com:587')
        # smtpObj.connect(mail_host, 587)  #SMTP 端口号
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
        flag = True
        return flag
    # except smtplib.SMTPException as e:
    except Exception as e:
        print "Error: 无法发送邮件",e
        flag = False
        return  flag

if __name__ == '__main__':
    subject = '邮件测试'
    text = '**************************************'
    flag = hotmail_send(subject, text)
    while not flag:
        flag = hotmail_send(subject, text)
