from django.urls import path
from emp import views

urlpatterns = [
    path('', views.allemplyoees, name='allemplyoees'),
    path('allemplyoees', views.allemplyoees, name='allemplyoees'),
    path('singleemployee', views.singleemployee, name='singleemployee'),
    path('addemployee', views.addemployee, name='addemployee'),
    path('deleteemployee/<int:empid>', views.deleteemployee, name='deleteemployee'),
    path('updateemployee/<int:empid>/', views.updateemployee, name='updateemployee'),
    path('doupdateemployee/<int:empid>/', views.doupdateemployee, name='doupdateemployee'),  # Add this line
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
]
