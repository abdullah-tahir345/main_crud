from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RegStu

def home(request):
    student_data = RegStu.objects.all()
    context = {'student_data':student_data}
    return render(request,'crud/home.html', context)

def add_student(request):
    
    if request.method == "POST":
        name = request.POST.get('std_name')
        roll = request.POST.get('std_roll')
        phone = request.POST.get('std_phone')
        email = request.POST.get('std_email')
        address = request.POST.get('std_address')
        
        s = RegStu()
        s.name = name
        s.roll = roll
        s.phone = phone
        s.email = email
        s.address = address
        
        s.save()
        return redirect('home')
        
    
    context = {}
    return render(request, 'crud/add_student.html', context)

def delete_student(request, std_id):
    std = RegStu.objects.get(pk=std_id)
    std.delete()
    
    return redirect('home')

def update_student(request, std_id):
    std = RegStu.objects.get(pk=std_id)
    context = {'std':std}
    return render(request, 'crud/update_student.html', context)

def do_update_student(request, std_id):
    name = request.POST.get('std_name')
    roll = request.POST.get('std_roll')
    phone = request.POST.get('std_phone')
    email = request.POST.get('std_email')
    address = request.POST.get('std_address')
    
    s = RegStu.objects.get(pk=std_id)
    s.name = name
    s.roll = roll
    s.phone = phone
    s.email = email
    s.address = address
    
    s.save()
    return redirect('home')