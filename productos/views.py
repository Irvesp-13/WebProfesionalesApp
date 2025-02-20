import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto
from .forms import productoForm

# Metodo que evalue el JSON
def lista_productos(request):
    # Obtener todas las instancias del objeto de la base de datos
    productos = Producto.objects.all()

    # Construir una variable en fomrato de diccionario porque el JSONResponse lo requiere
    data = [
        {
            # Onjeto Producto construido al arie
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]


    # Devolver la respuesta en JSON
    return JsonResponse(data, safe=False)

# Funcion para mandar a la vista de formulario
def agregar_producto(request):
    # Averiguar si estamos teniendo una respuesta de formulario
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar') # Redirige a la lista de productos
    # Pintar un formulario vacio
    else:
        form = productoForm()
    return render(request, 'agregar.html', {'form': form})

# Funcion que registre sin recargar la pagina (sin hacer render)

def registrar_producto(request):
    # Checar que estemos manejando un POST
    if request.method == 'POST':
        try:
            # Intentar obtener los datos del body del request
            data = json.loads(request.body) # Hace que el parametro devuelva un JSON
            producto = Producto.objects.create(
                # Basicamente es un constructor
                nombre = data['nombre'],
                precio = data['precio'],
                imagen = data['imagen']
            ) #La funcion CREATE directamente ingresa el modelo a la base de datos
            return JsonResponse({'mensaje':'Registro exitoso','id':producto.id}, status=201)
        except Exception as e:
            return JsonResponse({'error':str(e)}, status=400)
    return JsonResponse({'error':'Metodo no soportado'}, status=405)