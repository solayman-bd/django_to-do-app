from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
     path('signUp', views.signUp,name='signUp'),
    path('login', views.loginView,name='login'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logoutView,name='logout'),
    path('passChange',views.changePassword,name='passChange'),
    path('passSet',views.setPassword,name='passSet'),
    path('userUpdate/', views.userUpdate, name='userUpdate'),
    path('addTask/', views.addTask, name='addTask'),
    path('showTasks/', views.showTasks, name='showTasks'),
    path('deleteTask/<int:task_id>/', views.deleteTask, name='deleteTask'),
    path('editTask/<int:task_id>/', views.editTask, name='editTask'),
    path('completeTask/<int:task_id>/', views.completeTask, name='completeTask'),
    path('completedTasks/', views.completedTasks, name='completedTasks'),
    path('deleteCompletedTask/<int:task_id>/', views.deleteCompletedTask, name='deleteCompletedTask'),
    
]
