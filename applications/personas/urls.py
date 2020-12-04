from django.contrib import admin
from django.urls import path

from . import views

app_name = 'persona_app' #se dede dar un nombre si se usa reverse_lazy

urlpatterns = [
    path('', views.InivioViews.as_view(), name='inicio'),
    path('listar-todo-empleados/',views.LitsAllEmpleados.as_view(),name='empleados'),
    path('listar-empleados-admin/', views.LitsEmpleadosAdmin.as_view(), name='empleados_admin'),
    path('listar-by-area/<shortname>/', views.LitsByAreaEmpleado.as_view(), name='empleados_area'),
    path('list_by_trabajo/<shortname>/', views.LitsByAreaTrabajo.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('habilidades/', views.ListHabiliadesEmpleado.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='empleado_add'),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleados'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleados'),
]
