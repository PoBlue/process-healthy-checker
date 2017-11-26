#!/usr/bin/env python
#-*- coding: utf-8 -*-
from data import user_account, to_mail, stmp_code, process_name, content, subject
from utils import check_process_alive, create_msg, send_qq_mail

def main():
    if(not check_process_alive(process_name)):
        msg = create_msg(content, subject, user_account)
        send_qq_mail(user_account, stmp_code, to_mail, msg)
        print("is dead")
    else:
        print("still alive")
    pass

if __name__ == '__main__':
    main()