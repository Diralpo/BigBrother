# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

from Webserver.config import const


def mail(sender_nickname, recipient_nickname, text_content):
    ret = True
    try:
        msg = MIMEText(text_content, 'plain', 'utf-8')
        msg['From'] = formataddr([sender_nickname, const.EMAIL_USER])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([recipient_nickname, const.EMAIL_LIST])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = const.EMAIL_ERR_TITLE  # 邮件的主题，也可以说是标题

        # 发件人邮箱中的SMTP服务器，端口是465
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 括号中对应的是发件人邮箱账号、邮箱密码
        server.login(const.EMAIL_USER, const.EMAIL_PWD)
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(const.EMAIL_USER, [const.EMAIL_LIST, ], msg.as_string())
        server.quit()  # 关闭连接
    except :  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret
