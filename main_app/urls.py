from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('makes/', views.MakeList.as_view(), name="make_list"),
    path('makes/new/', views.MakeCreate.as_view(), name="make_create"),
    path('makes/<int:pk>/', views.MakeDetail.as_view(), name="make_detail"),
    path('makes/<int:pk>/update', views.MakeUpdate.as_view(), name="make_update"),
    path('makes/<int:pk>/delete', views.MakeDelete.as_view(), name="make_delete"),
]