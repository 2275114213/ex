from django.contrib import admin
from app01.models import  Test
# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.

#admin.site.register(Test)

@admin.register(Test)
class PostAdmin(admin.ModelAdmin):
    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            '/static/kindeditor/kindeditor-all-min.js',
            #'/static/kindeditor/zh_CN.js',
            '/static/kindeditor/config.js',
        )
