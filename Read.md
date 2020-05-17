
#
数据库要手动建一下

    create database shopping;
# 
 通过 DJango 自带的 管理工具创建表
 
    python manage.py makemigrations
    python manage.py migrate
 
 #
自行创建超级用户 

    python manage.py createsuperuser                       #输入
    Username (leave blank to use 'root'): admin            #输入用户名
    Email address: admin@runoob.com                        #输入邮箱
    Password:                                              #输入新建的用户密码
    Password (again):                                      #再次输入
    Superuser created successfully.                        #出现这个，表明创建成功
