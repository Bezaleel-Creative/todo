from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.log_out, name='logout'),
    path('todo_list', views.todo_list, name='todo_list'),
    path('addtask', views.addtask, name='addtask'),
    path('viewtask/<str:pk>', views.viewtask, name='viewtask'),
    path('edit/<str:pk>', views.edit, name='edit'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('completed', views.completed, name='completed'),
]