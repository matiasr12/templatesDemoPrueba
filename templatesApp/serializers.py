from rest_framework import serializers
from templatesApp.models import Profesor, Apoderado, Alumnos

class profesorSerializar(serializers.ModelSerializer):
    class Meta:
        model= Profesor
        fields='__all__'


class apoderadoSerializar(serializers.ModelSerializer):
    class Meta:
        model= Apoderado
        fields='__all__'

class AlumnosSerializar(serializers.ModelSerializer):
    class Meta:
        model= Alumnos
        fields='__all__'

