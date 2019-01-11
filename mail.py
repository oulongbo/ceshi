#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 邮件提醒
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


my_sender = "18811705542@163.com"   # 发件人的邮箱账号
my_user = "zhenmingzhang@sncrating.com"     # 收件人邮箱账号
#my_user = "hongweihuang@sncrating.com"     # 收件人邮箱账号

def mail(info):
    ret = True
    try:
        msg = MIMEText(info,"plain","utf-8")
        msg["Form"] = formataddr(["cammeron",my_sender])     # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg["to"] = formataddr(["小先生",my_user])      #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg["Subject"] = "交易完成"                 # 邮件的主题，也可以说是标题
        server = smtplib.SMTP("smtp.163.com",25)                ##发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, "huang1995412")     # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())    #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 这句是关闭连接的意思
    except Exception as e:
        ret = False
    return ret

#ret=mail("有bug")
#
#if ret:
#     print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
#else:
#     print("filed")  #如果发送失败则会返回filed
#


