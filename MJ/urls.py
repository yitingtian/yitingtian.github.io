"""MJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from resume.views import Resume,home
from regist.views import Register,Patients,Registermain,find,getNumber,Login,Logout,Consult


urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume/',Resume),
    path('',home),
    path('register/',Register),
    path('patients/',Patients),
    path('registermain/',Registermain),
    path('findmypatient/',find),
    path('getnumber/',getNumber),
    path('login/',Login),
    path('logout/',Logout),
    path('consult/',Consult),



]
