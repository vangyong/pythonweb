--新建初始化项目:
django-admin.py startproject pythonweb

1、导出依赖包
pip freeze > requires

2、安装依赖包
pip install -r requires

-- 定义模型 
django-admin startapp system

--生成表结构
python manage.py makemigrations system  # 清理库表
python manage.py migrate system

--运行:
python manage.py runserver 0.0.0.0:8000

--测试访问:
http://127.0.0.1:8000/hello