from django.contrib import admin
from django.urls import path

from . views import karakteradmin, karakteradd, karakterupdate, karakterdelete, dashboard, baseadmin, charadmin, charadd, charupdate, chardelete
from . autentikasi import login_form, signup_form

urlpatterns = [
    # Dashboard
    path('', dashboard),
    path('karakter-admin', karakteradmin, name="karakteradmin"),
    path('karakteradd', karakteradd, name="karakteradd"),
    path('karakterupdate/<int:id>/', karakterupdate, name="karakterupdate"),
    path('karakterdelete/<int:id>/', karakterdelete, name="karakterdelete"),
    path('baseadmin', baseadmin, name="baseadmin"),
    path('login', login_form, name="login"),
    path('signup', signup_form, name="signup"),
    path('char-admin', charadmin, name="charadmin"),
    path('char-add', charadd, name="charadd"),
    path('charupdate/<int:id>/', charupdate, name="charupdate"),
    path('chardelete/<int:id>/', chardelete, name="charudelete")
  
]
 