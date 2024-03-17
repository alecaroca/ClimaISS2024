from django.urls import path
from .views import index,step1,step2,step3,step4,step5,step6,step7,step8

urlpatterns = [
    path('', index, name="index"),
    path('step1/', step1, name="step1"),
    path('step2/', step2, name="step2"),
    path('step3/', step3, name="step3"),
    path('step4/', step4, name="step4"),
    path('step5/', step5, name="step5"),
    path('step6/', step6, name="step6"),
    path('step7/', step7, name="step7"),
    path('step8/', step8, name="step8"),
]