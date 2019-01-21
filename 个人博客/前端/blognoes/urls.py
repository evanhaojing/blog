from django.urls import path

from blognoes import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('info/<int:id>', views.info, name='info'),
    path('fengmian/', views.fengmian, name='fengmian'),
    path('list/', views.list, name='list'),
    path('time/', views.time, name='time'),
]