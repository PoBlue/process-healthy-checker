#!/usr/bin/env python
#-*- coding: utf-8 -*-
from data import user_account, password, to_mail, stmp_code
from utils import check_process_alive, create_msg, send_qq_mail

def main():
    process_name = "getReview.py"
    content = "process {name} is dead, fix it right now".format(name=process_name)
    subject = "Process Healthy Checker"

    if(not check_process_alive(process_name)):
        msg = create_msg(content, subject, user_account)
        send_qq_mail(user_account, stmp_code, to_mail, msg)
        print("is dead")
    else:
        print("still alive")
    pass

if __name__ == '__main__':
    main()