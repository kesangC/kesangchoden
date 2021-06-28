from django.contrib import admin
from django.urls import path
from myapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserLogin, name="assignment"),
    path('Signup',views.Register, name="Signup"),
    path('homepage/', views.homepage, name="homepage"),
    path('guidelines/', views.rules, name="guidelines"),
    path('notification/', views.notiff, name="notification"),
    path('logout/', views.logout, name="logout"),
    path('setting/', views.setting, name="setting"),
    path('room_allocation/', views.studentinfo, name="roomAllocation"),
    path('maintenance_service', views.Insertrecord, name="Mservice"),
]
