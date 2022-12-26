"""templatesDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from templatesApp import views
from rest_framework.routers import DefaultRouter
from django.urls import include




router=DefaultRouter()
router.register('profesor',views.ProfesorViewSets)
router.register('Alumnos',views.AlumnosViewSets)
router.register('Apoderado',views.ApoderadosViewSets)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('profesores/',views.profesor_list),
    path('profesores/<int:pk>',views.Profesor_detail),
    path('apoderados/',views.apoderado_list),
    path('apoderados/<int:pk>',views.apoderados_detail),
    path('alumnos/',views.alumnos_list),
    path('alumnos/<int:pk>',views.alumnos_detail),
    path('',include(router.urls)),

    
]
   