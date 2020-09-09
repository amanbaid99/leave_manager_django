from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='leaveApp/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',views.register,name='register'),
    path('leave/',views.applyforleave,name='leave'),
    path('approve/<int:pk>/',views.approve,name='approve'),
    path('decline/<int:pk>/',views.decline,name='decline'),
]