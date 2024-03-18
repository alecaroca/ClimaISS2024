from django.urls import path
from .views import index,step7,step8

urlpatterns = [
    path('', index, name="index"),
    path('step7/', step7, name="step7"),
    path('step8/', step8, name="step8"),
]