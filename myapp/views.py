from django.shortcuts import render, redirect
from django.template import loader  
from django.http import HttpResponse  
from myapp.models import login
from myapp.models import RoomAllocation
from myapp.models import maintenance
from django.contrib import messages
from myapp.models import Guideline
from myapp.models import Notification
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from  django.contrib.auth.models import User 
from django.db import IntegrityError 

def homepage(request):  
   template = loader.get_template('homepage.html')
   return HttpResponse(template.render())        

def studentinfo(request):
    stud = RoomAllocation.objects.all()
    return render(request, 'room_allocation.html', {'stu': stud})

def Insertrecord(request):
    if request.method=="POST":
       	form = request.POST
       	maintenance.objects.create(
			Name = form['Name'],
    		Year = form['Year'],
    		Name_of_block = form['Name_of_block'],
    		Room_number = form['Room_number'],
    		Maintenance_needed = form['Maintenance_needed'],
       	)
       	messages.success(request, "Request applied successfully!...")
        return render(request,'maintenance_service.html')
    else:
            return render(request,'maintenance_service.html')

def rules(request):
    stud = Guideline.objects.all()
    return render(request, 'guidelines.html', {'stu': stud})

def notiff(request):
    stud = Notification.objects.all()
    return render(request, 'notification.html', {'stu': stud})

def setting(request):
    template = loader.get_template('setting.html')
    return HttpResponse(template.render())

def logout(request):
    template = loader.get_template('logout.html')
    return HttpResponse(template.render())

def Register(request):
  if request.method=="POST":
    if request.POST.get('password1')==request.POST.get('password2'):
      try:
        saveuser=User.objects.create_user(request.POST.get('username'),password=request.POST.get('password1'))
        saveuser.save()
        return render(request,'Signup.html',{'form':UserCreationForm(),'info':'The user'+' '+request.POST.get('username')+' successfully registered...!'})
      except IntegrityError:
        return render(request,'Signup.html',{'form':UserCreationForm(),'error':'The user'+' '+request.POST.get('username')+' already exist...!'})
    else:
      return render(request,'Signup.html',{'form':UserCreationForm(),'error':'The Passwords Are Not Matching..!'})  
  else:
    return render(request,'Signup.html',{'form':UserCreationForm})

def UserLogin(request):
  if request.method=="POST":
    loginsuccess=authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
    if loginsuccess is None:
      return render(request,'assignment.html',{'form':AuthenticationForm(),'error':'Invalid Username or Password...!'})
    else:
      login(request,loginsuccess)
      return redirect('homepage')
  else:
    return render(request,'assignment.html',{'form':AuthenticationForm()})
