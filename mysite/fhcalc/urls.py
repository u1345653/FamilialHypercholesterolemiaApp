from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name = 'index'),
    path('results/', views.results_view, name = 'results')
]