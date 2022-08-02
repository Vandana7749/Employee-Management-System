from distutils.command.build_scripts import first_line_re
from django.shortcuts import render, HttpResponse
from .models import Employee, department, role
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def All_employee(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)
    return render(request, 'All_employee.html', context)

    
def Add_employee(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        new_emp = Employee(first_name=first_name, last_name=last_name, dept_id = dept, salary = salary, bonus=bonus, role_id = role, phone=phone, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse('Employee Added successfully')
    elif request.method == 'GET':  
        return render(request, 'Add_employee.html')    
    else:
        return HttpResponse('An exception occured')    

def Remove_employee(request, emp_id = 0):
    if emp_id:
        try:
            remove_emp = Employee.objects.get(id=emp_id)
            remove_emp.delete()
            return HttpResponse('Employee Revomed succesfully')
        except:
            return HttpResponse('Please enter a valid emp ID')
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)
    return render(request, 'Remove_employee.html', context)

def Filter_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps':emps
        }
        return render(request, 'All_employee.html', context)

    elif request.method == 'GET':
        return render(request, 'Filter_employee.html')

    else:
        return HttpResponse('An exception occured')    
    