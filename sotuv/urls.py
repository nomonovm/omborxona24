from django.urls import path
from .views import *

urlpatterns = [
    path('', SotuvlarView.as_view(), name='sotuvlar'),
    path('ogohlantirish/', ogohlantirish_view, name='ogohlantirish'),
    path('<int:pk>/tahrirlash/', SotuvTahrirlashView.as_view(), name='sotuv_tahrirlash'),
    path('<int:pk>/delete/', sotuv_delete, name='sotuv_delete'),
]
