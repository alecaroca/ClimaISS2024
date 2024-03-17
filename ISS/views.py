from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona
from django.contrib import messages
from django.db.models import Q
import tkinter as tk
from .forms import PersonaForm
# Create your views here.

def index(request):                   
    return render(request, 'app/index.html')

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
    RUTE = request.POST['rut']
    persona = Persona.objects.get(RUT=RUTE)
    persona.ESTADO_ENCUESTA = "1"
    persona.GENERO = request.POST['genero']
    persona.P1 = request.POST['pregunta1']
    persona.P2 = request.POST['pregunta2']
    persona.P3 = request.POST['pregunta3']
    persona.P4 = request.POST['pregunta4']
    persona.P5 = request.POST['pregunta5']
    persona.P6 = request.POST['pregunta6']
    persona.P7 = request.POST['pregunta7']
    persona.P8 = request.POST['pregunta8']
    persona.P9 = request.POST['pregunta9']
    persona.P10 = request.POST['pregunta10']
    persona.P11 = request.POST['pregunta11']
    persona.P12 = request.POST['pregunta12']
    persona.P13 = request.POST['pregunta13']
    persona.P14 = request.POST['pregunta14']
    persona.P15 = request.POST['pregunta15']
    persona.P16 = request.POST['pregunta16']
    persona.P17 = request.POST['pregunta17']
    persona.P18 = request.POST['pregunta18']
    persona.P19 = request.POST['pregunta19']
    persona.P20 = request.POST['pregunta20']
    persona.P21 = request.POST['pregunta21']
    persona.P22 = request.POST['pregunta22']
    persona.P23 = request.POST['pregunta23']
    persona.P_NPS = request.POST['pregunta24']
    persona.save()

    personas = Persona(
          
    )
    

    print(RUTE)
    return render(request, 'app/step7.html')

def step8(request):
    RUT = request.POST['rut']
    print(RUT)
    GENERO = request.POST['genero']  
    if (RUT!='' and  GENERO!='Seleccionar genero'):
                print ("pasa el")
                existe  = Persona.objects.get(RUT = RUT)
                print(existe)    
                print(existe.RUT)
                #Consulta si existen el rut 
                if existe.RUT:     
                                #Cnsulta si existe encuesta
                                if existe.ESTADO_ENCUESTA == None :
                                    return render(request, 'app/step8.html',{'RUT': RUT,'GENERO': GENERO})  
     
                                else:
                                        messages.success(request, "Tu encuesta ya fue respondida con anterioridad")
                                                 
                else:
                      messages.success(request, "Este rut no se encuentra registrado, favor corrobora los datos ingresados")      
    else:
          messages.success(request, "Faltan datos, corrobora los datos ingresados") 
          return render(request, 'app/index.html')
    return render(request, 'app/index.html')