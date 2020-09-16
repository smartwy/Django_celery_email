from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_email
from redis import StrictRedis,ConnectionPool

# Create your views here.
# red = StrictRedis(host='127.0.0.1', port=6379, db=0)
pool = ConnectionPool(host='127.0.0.1', port=6379, db=0)
red = StrictRedis(connection_pool=pool)

def index(request):
	return render(request,'index.html')

def code_echo(request):
	email = request.POST.get('email')
	# print(email)
	# rend_code = send_email.delay(email)
	# 实际上 delay 是 apply_async 的一个快捷方式，而相较于 delay，apply_aysnc 支持对于任务执行过程的更精确的控制
	# 在Celery	中执行任务的方法一共有三种：
	# 1.	delay， 用来进行最简单便捷的任务执行；
	# 2.	apply_async， 对于任务的执行附加额外的参数，对任务进行控制；
	# 3.	app.send_task， 可以执行未在	Celery中进行注册的任务。
	rend_code = send_email.apply_async(args=(email,))
	rend_code = rend_code.get()  # rend_code.ready()返回任务是否执行完毕
	red.set('code',str(rend_code))
	print('views.py ', rend_code)
	return render(request, 'index.html')

def sigin(request):
	messages = '注册失败！'
	qcode = request.POST.get('code1')
	code_red = red.get('code').decode('utf-8')
	# print(qcode,red.get('cd').decode('utf-8'))
	if code_red == qcode:
		messages = '注册成功'
	return HttpResponse(messages)
