from rest_framework.response import Response
from rest_framework.decorators import api_view
# from base.models import Item
from .serializers import Origen1Serializer, Origen2Serializer



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
