"""
URL configuration for project_iqbal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

#-------------------MEDIA-------------------
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from . views import home,char,contacts,base,blog,detail,karakter,karakteradd, karakterupdate, karakterdelete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name= 'home'),
    path('char.html', char, name= 'char'),
    path('contacts.html', contacts, name= 'contacts'),
    path('base.html', base, name='base'),
    path('blog.html', blog, name='blog'),
    path('detail.html', detail, name='detail'),
    path('karakter.html', karakter, name="karakter"),
    path('karakteradd.html', karakteradd, name="karakteradd"),
    path('karakterupdate.html/<int:id>/', karakterupdate, name="karakterupdate"),
    path('karakterdelete/<int:id>/', karakterdelete, name="karakterdelete"),
   
]

#-------------------MEDIA-------------------
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 