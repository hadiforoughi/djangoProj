from django.conf.urls import url
from appone import views

app_name = 'appone'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('home/', views.home, name='home'),
    url('form/', views.in_form, name='form'),
    url('login/', views.user_login, name='login'),
]
