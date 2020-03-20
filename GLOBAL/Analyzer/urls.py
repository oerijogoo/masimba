from django.urls import path
from . import views

urlpatterns = [
    path('', views.Analyzer_with_pivot, name='Analyzer_with_pivot'),
    path('data', views.pivot_data, name='pivot_data'),
]