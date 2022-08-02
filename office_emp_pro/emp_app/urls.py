"""office_emp_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('All_employee', views.All_employee, name='All_employee'),
    path('Add_employee', views.Add_employee, name='Add_employee'),
    path('Remove_employee', views.Remove_employee, name='Remove_employee'),
    path('Remove_employee/<int:emp_id>', views.Remove_employee, name='Remove_employee'),
    path('Filter_employee', views.Filter_employee, name='Filter_employee')
]
