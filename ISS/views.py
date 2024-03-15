from django.shortcuts import render
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
                        else:
                                messages.success(request, "Encuesta ya respondida")
                                datos = {
                                        'personas': Persona.objects.none()
                                
                                }            
        else:
                messages.warning(request, "usuario no existe")
                datos = {
                        'personas': Persona.objects.none()
                
                }
        return render(request, 'app/index.html', datos)

def p1(request):
    return render(request, 'app/p1.html')

def p2(request):
    return render(request, 'app/p2.html')