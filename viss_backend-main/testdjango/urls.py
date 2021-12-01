"""testdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# work 4: urls
# rest API로 들어오는 요청 처리 -> views.py로 넘겨줌
from django.urls import path, include, re_path
#from rest_framework_simplejwt import views as jwt_views

from django.contrib import admin
from viss.views import Vehicle_Battery, Vehicle_Gposition, Vehicle_temper
#from viss.views import Vehicle_AverageSpeed

app_name='viss'
urlpatterns = [
    path('admin', admin.site.urls),
    path('Vehicle/Battery',  Vehicle_Battery, name='Vehicle_Battery'),
    path('Vehicle/Temperature',  Vehicle_temper, name='Vehicle_Temper'),
    path('Vehicle/Gposition',  Vehicle_Gposition, name='Vehicle_Gposition'),
    #re_path(r'Vehicle*', Vehicle, name='Vehicle')
]

