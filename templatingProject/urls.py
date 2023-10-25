"""
URL configuration for templatingProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from tmp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tmp/', include('tmp.urls')),
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/update/<int:pk>/', views.student_update, name='student_update'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('students/table/', views.student_table, name='student_table'),
    path('students/id-cards/', views.generate_id_cards, name='generate_id_cards'),
    path('attendance/record/', views.record_attendance, name='record_attendance'),
    path('attendance/list/', views.attendance_list, name='attendance_list'),  # Define the URL pattern for the attendance list
]


