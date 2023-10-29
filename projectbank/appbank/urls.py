from  . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('application/',views.application,name='application'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]