from django.urls import path
from . import views

urlpatterns = [ path('', views.Home.as_view(), name='homepage'),
                path('test', views.New.as_view(), name='test'), ]
