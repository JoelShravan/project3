from django.shortcuts import render, redirect  
from student.forms import StudentForm  
from student.models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.  


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)



@login_required(login_url='login')
def emp(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,'index.html',{'form':form})  

@login_required(login_url='login')
def show(request):  
    students = Student.objects.all()  
    return render(request,"show.html",{'students':students})  

@login_required(login_url='login')
def edit(request, id):  
    students = Student.objects.get(id=id)  
    return render(request,'edit.html', {'student':students})  

@login_required(login_url='login')
def update(request, id):  
    student = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'student': student})  

@login_required(login_url='login')
def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/show")  