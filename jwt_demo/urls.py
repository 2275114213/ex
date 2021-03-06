"""jwt_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from app01.views import index
from django.conf import settings
from django.conf.urls.static import static
from app01.views import  upload_image
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    url(r'^uploads/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    url(r'^upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    # re_path('uploads/(?<Path>.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
    # re_path('uploads/(?<path>.*)', 'django.views.static.server',{'documen_root':settings.MEDIA_ROOT})

]