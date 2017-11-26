#!/usr/bin/env python
#-*- coding: utf-8 -*-
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
import subprocess


def send_qq_mail(_user, _stmp_code, _to_mail, _msg):
    #Auth and Login
    smtp_server = 'smtp.qq.com'
    smtp_auth_username = _user   # QQ号，非邮箱
    smtp_auth_password = _stmp_code       #! 换成自己的SMTP授权码，而不是QQ登录密码

    smtp = SMTP_SSL(smtp_server)
    smtp.login(smtp_auth_username, smtp_auth_password)

    # Send mail
    from_addr = '{qq}@qq.com'.format(qq=_user)      #实际用来发送的邮箱
    smtp.sendmail(from_addr, _to_mail, _msg)
    smtp.quit()


def create_msg(_msg, _subject, _user):
    msg = '''\
From: {user}@qq.com
Subject: {subject}

{content}
    '''.format(user=_user,
               subject=_subject,
               content=_msg)
    return msg


def excute_cmd(_cmd):
    """
        excute cmd and return the out put string
    """
    code = 0
    try:
        out_bytes = subprocess.check_output(_cmd, shell=True)
    except subprocess.CalledProcessError as e:
        out_bytes = e.output
        code = e.returncode
    return out_bytes.decode('utf-8'), code


def check_process_alive(_name):
    """
    check if process is alive
    """
    cmd = 'bash check-process.sh {name}'.format(name=_name)
    output, code = excute_cmd(cmd)
    if code == 1:
        return False
    else:
        return True

    