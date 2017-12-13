#!/usr/bin/env python
#-*- coding: utf-8 -*-
from data import user_account, to_mail, stmp_code, process_names, content, subject
from utils import check_process_alive, create_msg, send_qq_mail
import time

def main():
    while True:
        for process_name in process_names:
            if(not check_process_alive(process_name)):
                msg = create_msg(content.format(name=process_name), subject, user_account)
                send_qq_mail(user_account, stmp_code, to_mail, msg)
                print("is dead")
            else:
                print("still alive")
        mins = 60
        time.sleep(60 * mins) 
    pass

if __name__ == '__main__':
    main()
