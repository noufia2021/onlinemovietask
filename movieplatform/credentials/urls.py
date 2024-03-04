from . import views
from django.urls import path

app_name = 'credentials'

urlpatterns = [
    path('registration',views.registration,name='register'),
    path('login',views.login,name='login',),
    path('logout',views.logout,name='logout'),


]
