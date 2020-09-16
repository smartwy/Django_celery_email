#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    Data_Analysis
#F-Name:    tasks.py
#Login:     Administrator   
#Descripton:
#__Author__  Smartwy
#Date:      2020/5/22 15:12:32
#Version:

'''
    
'''

from django_celery_email.celery import app
import datetime
from email.mime.text import MIMEText
from .code_m import create_code

@app.task
def send_email(toaddr):
	print(toaddr)
	code = create_code()
	msg = MIMEText('Hello SuperMan ,This is by python celery email.{}.\ncode number :{}'.format(datetime.datetime.now(),code), 'plain', 'utf-8')

	from_addr = '******@163.com'
	password = '******'
	to_addr = toaddr
	smtpserver = 'smtp.163.com'
	# 下面三行表示 发送地址，接收地址，邮件主题，不写报554 DT.SPM错误，不支持中文
	msg['from'] = from_addr
	msg['to'] = to_addr
	msg['subject'] = 'Verification code mail'

	import smtplib
	server = smtplib.SMTP(smtpserver, 25)
	server.set_debuglevel(3)
	server.login(from_addr, password) # 登录

	server.sendmail(from_addr, to_addr, msg.as_string()) # 源地址，目标地址，内容
	server.quit()
	print('tasks.py ', code)
	return code