from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.home_view,name='blog'),
    path('newpost',views.newpost_view,name='newpost'),
    path('addpost/', views.addpost_view, name='addpost'),
    path('<int:pk>/', views.delete_project, name="delete"),



]