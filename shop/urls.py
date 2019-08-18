from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views

register_converter(FourDigitYearConverter, 'yyyy')

# url reverse에서 namespace
app_name = 'shop'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<int:pk>/', views.item_detail, name='item_detail')
    # re_path(r'^(?P<pk>\d+)/$', views.item_detail) : 옛날 url 방식
]
