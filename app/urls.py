from django.urls import path

from app import views

urlpatterns = [
  path('', views.index, name = 'index'),
  path('<str:department_id>/', views.department, name = 'department'),
  path('<str:department_id>/inventory', views.inventory, name = 'inventory'),
  path('<str:department_id>/employee', views.employee, name = 'employee'),
]