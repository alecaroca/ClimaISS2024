from django.shortcuts import render, redirect
from .models import Persona
from django.contrib import messages
from django.db.models import Q
import tkinter as tk
# Create your views here.

def index(request):
        queryset = request.GET.get("rut") 
        datos=Persona.objects.all()
        existe = Persona.objects.filter(RUT = queryset)      
        print(existe)
      
        
        if existe:     
                        print(queryset)  
                        existe2  = Persona.objects.get(RUT = queryset)
                        print(existe2.ESTADO_ENCUESTA)
                        if existe2.ESTADO_ENCUESTA == None :
                                datos = {
                                        'personas':Persona.objects.filter(
                                        Q(RUT = queryset)
                                        )
                                }
                                return redirect(to="step1")
                        else:
                                messages.success(request, "Encuesta ya respondida")
                                datos = {
                                        'personas': Persona.objects.none()
                                
                                }            
        else:
                
                datos = {
                        'personas': Persona.objects.none()
                
                }
        return render(request, 'app/index.html', datos)

def step1(request):
    return render(request, 'app/step1.html')

def step2(request):   

    return render(request, 'app/step2.html')

def step3(request):
 
    return render(request, 'app/step3.html')

def step4(request):
    return render(request, 'app/step4.html')

def step5(request):
    return render(request, 'app/step5.html')

def step6(request):
    return render(request, 'app/step6.html')

def step7(request):
    return render(request, 'app/step7.html')

def step8(request):
    return render(request, 'app/step8.html')