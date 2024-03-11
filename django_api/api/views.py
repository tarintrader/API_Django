from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from base.models import Item
from .serializers import Origen1Serializer, Origen2Serializer


def index(request):
    html_content = """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>API Inicio</title>
        </head>
        <body>
            <h1>Bienvenid@ a la API</h1>
            <p>
                La API Web recibe solicitudes de préstamo de distintos orígenes (Origen1 y Origen2).<br>
                Las solicitudes vendrán dadas en formato JSON con distintas estructuras, las
                cuales se normalizan y almacenan en una base de datos SQLite.
            </p>
            <h2>Estructuras de los JSON recibidos:</h2>
            <h3><a href="/Origen1">Origen1</a></h3>
            <ul>
                <li><strong>nombre:</strong> Nombre de la persona solicitante</li>
                <li><strong>apellidos:</strong> Apellidos de la persona solicitante, separados por un espacio</li>
                <li><strong>fechaNacimiento:</strong> Fecha de nacimiento de la persona solicitante. En formato dd/MM/yyyy (27/02/2024, por ejemplo)</li>
                <li><strong>cantidad:</strong> Cantidad solicitada para el préstamo</li>
            </ul>
            <h3><a href="/Origen2">Origen2</a></h3>
            <ul>
                <li><strong>nombreCompleto:</strong> Nombre y apellidos de la persona solicitante</li>
                <li><strong>fechaNacimiento:</strong> Fecha de nacimiento de la persona solicitante. En formato yyyy/MM/dd (2024/02/27, por ejemplo)</li>
                <li><strong>cantidadSolicitada:</strong> Cantidad solicitada para el préstamo</li>
            </ul>
        </body>
        </html>
        """
    return HttpResponse(html_content)

@api_view(['POST'])
def add1(request):
    mapped_data = {
        'name': request.data.get('nombre'),
        'surnames': request.data.get('apellidos'),
        'birthdate': request.data.get('fechaNacimiento'),
        'amount': request.data.get('cantidad')
    }
    serializer = Origen1Serializer(data=mapped_data)
    if serializer.is_valid():
        full_name = f"{serializer.validated_data['name']} {serializer.validated_data['surnames']}"
        serializer.save(full_name=full_name)
        return Response(serializer.data, status=201)
    else:
        print(serializer.errors)  # Print validation errors
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def add2(request):
    mapped_data = {
        'full_name': request.data.get('nombreCompleto'),
        'birthdate': request.data.get('fechaNacimiento'),
        'amount': request.data.get('cantidadSolicitada')
    }
    serializer = Origen2Serializer(data=mapped_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        print(serializer.errors)  # Print validation errors
        return Response(serializer.errors, status=400)
