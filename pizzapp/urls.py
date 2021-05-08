from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name="pizzalist"),
    path('update_pizza/<str:pk>', views.updatePizza, name="update_pizza"),
    path('delete/<str:pk>', views.deletePizza, name="delete"),  
    path('info_pizza/', views.showInfo, name='info_pizza'), 
    path('sortType/', views.sortType, name='sortType'), 
    path('sortSize/', views.sortSize, name='sortSize'), 

    #url(r'^search/$', views.search, name='search'), 
    #url('info_pizza/', views.showInfo)
]