from django.shortcuts import render
from .serializers import profesorSerializar
from .serializers import apoderadoSerializar
from .serializers import AlumnosSerializar
from .models import Profesor
from .models import Apoderado
from .models import Alumnos
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.decorators import	api_view
from django.shortcuts import redirect
from rest_framework import generics,mixins
from rest_framework import viewsets
# Create your views here.

@api_view(['GET','POST'])
def profesor_list(request):
    if request.method=='GET':
        profesor=Profesor.objects.all()
        serializer=profesorSerializar(profesor,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=profesorSerializar(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def Profesor_detail(request,pk):
    try:
        profesor=Profesor.objects.get(pk=pk)
    except Profesor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer= profesorSerializar(profesor)
        return Response(serializer.data)
    
    if request.method =='PUT':
        serializer=profesorSerializar(Profesor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        profesor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def apoderado_list(request):
    if request.method=='GET':
        apoderados=Apoderado.objects.all()
        serializer=apoderadoSerializar(apoderados,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=apoderadoSerializar(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def apoderados_detail(request,pk):
    try:
        apoderados=Apoderado.objects.get(pk=pk)
    except Apoderado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer= apoderadoSerializar(apoderados)
        return Response(serializer.data)
    
    if request.method =='PUT':
        serializer=apoderadoSerializar(Apoderado,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        apoderados.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET','POST'])
def alumnos_list(request):
    if request.method=='GET':
        alumnos=Alumnos.objects.all()
        serializer=AlumnosSerializar(alumnos,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=AlumnosSerializar(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','DELETE'])
def alumnos_detail(request,pk):
    try:
        alumnos=Alumnos.objects.get(pk=pk)
    except Alumnos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer= AlumnosSerializar(alumnos)
        return Response(serializer.data)
    
    if request.method =='PUT':
        serializer=AlumnosSerializar(Alumnos,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        alumnos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    



class ProfesorList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Profesor.objects.all()
    serializer_class = profesorSerializar

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
class ProfesorDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Profesor.objects.all()
    serializer_class = profesorSerializar

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)










class ProfesorLista(generics.ListCreateAPIView):
    queryset=Profesor.objects.all()
    serializer_class=profesorSerializar

class ProfesorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Profesor.objects.all()
    serializer_class=profesorSerializar



class ProfesorViewSets(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class=profesorSerializar


class AlumnosViewSets(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    serializer_class=AlumnosSerializar



class ApoderadosViewSets(viewsets.ModelViewSet):
    queryset = Apoderado.objects.all()
    serializer_class=apoderadoSerializar


