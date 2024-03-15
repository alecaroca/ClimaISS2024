from django.urls import path
from .views import index,p1,p2

urlpatterns = [
    path('', index, name="index"),
    path('p1/', p1, name="p1"),
    path('p2/', p2, name="p2"),

]