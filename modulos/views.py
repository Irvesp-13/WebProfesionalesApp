from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Modulo
from .forms import moduloForm

# Metodo que evalue el JSON
def lista_modulos(request):
    # Obtener todas las instancias del objeto de la base de datos
    modulos = Modulo.objects.all()

    # Construir una variable en fomrato de diccionario porque el JSONResponse lo requiere
    data = [
        {
            # Onjeto Modulo construido al arie
            'nombre': m.nombre,
            'imagen': m.imagen
        }
        for m in modulos
    ]


    # Devolver la respuesta en JSON
    return JsonResponse(data, safe=False)

# Funcion para mandar a la vista de formulario
def registrar_modulo(request):
    # Averiguar si estamos teniendo una respuesta de formulario
    if request.method == 'POST':
        form = moduloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar') # Redirige a la lista de modulos
    # Pintar un formulario vacio
    else:
        form = moduloForm()
    return render(request, 'registrar.html', {'form': form})

def json_modulo(request):
    # Obtener todas las instancias del objeto de la base de datos
    modulos = Modulo.objects.all()

    # Pasar los datos a la plantilla
    return render(request, 'vistaJson.html', {'modulos': modulos})