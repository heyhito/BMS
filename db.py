import os
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','BMS.settings') #第二的参数写项目名+.settings
    import django
    django.setup()
    from app01 import models
#往数据库中添加信息
    models.Book_Messages.objects.create(
        name='c',
        price=996,
        data='2015-10-11',
        press='北京出版社'
    )