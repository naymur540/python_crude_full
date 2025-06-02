
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage,name='homepage'),
    path('student/',student_list,name='student'),
    path('studentcreate',student_create,name='studentcreate'),
    path('studentdelete/<int:id>/', student_delete, name='studentdelete'),
    path('studentedit/<int:id>/', student_edit, name='studentedit'),
    path('studentview/<int:id>/', student_view, name='studentview'),


]
