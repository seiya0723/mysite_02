from django.contrib import admin

#モデルをimportする。
from .models import Topic

# Register your models here.
#TODO:ここに管理サイトで操作したいモデルを追加する
admin.site.register(Topic)


#TODO:下記コマンドで管理ユーザーを追加する
# python3 manage.py createsuperuser
