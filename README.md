Django==2.1.1
mysqlclient==1.3.8
celery==4.2.1
django-celery-beat==1.1.1

--新建初始化项目:
django-admin.py startproject pythonweb

--运行:
python manage.py runserver 0.0.0.0:8000

--测试访问:
http://127.0.0.1:8000/hello