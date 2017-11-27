# process-healthy-checker
check if the process is alive and notify with mail

## 如何使用
0. 新建并设置 `data.py` 文件
1. 运行 `python process-checker.py`

```
#!/usr/bin/env python
#-*- coding: utf-8 -*-

# qq 账号
user_account = ''

# qq 的 stmp code
stmp_code = ''

# 要检查的 process 的名字, 如：
process_name = "getReview.py"

# email 的内容，content 为内容，subject 为主题, to_mail 为收件的邮箱地址
content = "process {name} is dead, fix it right now".format(name=process_name)
subject = "Process Healthy Checker"
to_mail = 'xxxx@qq.com'
```
