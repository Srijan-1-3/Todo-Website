"""todowoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signupuser, name='signupuser'),
    path('current/', views.current_todos, name='current_todos'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('create/', views.create_todo, name='create_todo'),
    path('detail/<int:todo_id>', views.detail, name='detail_page'),
    path('completed', views.completed, name='completed_todos'),
    path('complete_todo/<int:todo_id>', views.complete_todo, name='complete_todo'),
    path('delete_todo/<int:todo_id>', views.delete_todo, name='delete_todo'),
    path('edit_todo/<int:todo_id>' , views.edit_todo, name='edit_todo'),
    path('', views.home, name='home'),
]
