from django.urls import path
from .views import *

urlpatterns = [
    path('', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('mahsulotlar/tahrirlash/<int:pk>/', MahsulotTahrirlashView.as_view(), name='tahrirlash'),
    path('mijozlar/', MijozlarView.as_view(), name='mijozlar'),
    path('mahsulotlar/delete/<int:pk>/', mahsulot_delete, name='mahsulot_delete'),
    path('mijozlar/delete/<int:pk>/', mijoz_delete, name='mijoz_delete'),
    path('mijoz/<int:pk>/tahrirlash/', MijozTahrirlash, name='tahrirlash_mijoz'),
]