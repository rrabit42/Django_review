from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views

register_converter(FourDigitYearConverter, 'yyyy')

# url reverse에서 namespace
app_name = 'shop'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('new/', views.item_new, name='item_new'),
    path('<int:pk>/edit/', views.item_edit, name='item_edit'),
]
