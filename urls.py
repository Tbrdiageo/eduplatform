from django.contrib import admin
from django.urls import path
from .views import home, course_list, course_detail
from .views.auth import user_login, admin_login, user_logout, admin_dashboard

urlpatterns = [
    path('', home, name='home'),
    path('courses/', course_list, name='course_list'),
    path('courses/<int:course_id>/', course_detail, name='course_detail'),

    # Authentication URLs
    path('accounts/login/', user_login, name='login'),
    path('accounts/logout/', user_logout, name='logout'),
    path('admin/login/', admin_login, name='admin_login'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
]
