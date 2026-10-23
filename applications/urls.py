from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_application, name='add'),
    path('edit/<int:pk>/', views.edit_application, name='edit'),
    path('delete/<int:pk>/', views.delete_application, name='delete'),
        path('signup/', views.signup, name='signup'),
]