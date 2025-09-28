from django.urls import path
from . import views

urlpatterns = [
  path('', views.OrdemListView.as_view(), name='ordem-list'),
  path('new/', views.OrdemCreateView.as_view(), name='ordem-create'),
  path('editar/<int:pk>/', views.OrdemUpdateView.as_view(), name='ordem-update'),
]