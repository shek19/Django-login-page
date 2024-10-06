from django.shortcuts import render,redirect
#from .forms import *
from django.contrib.auth import authenticate, get_user_model
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import login as auth_login
from django.urls import reverse


User = get_user_model()

def index(request):
    print("We are in app1 index page")
    return render(request, "index.html")
    
def home(request):
    return render(request, 'home.html')

#--------------------------------------------------------------------------------------------------

def registration(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            name=request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            User.objects.create_user(username=email, password=password, first_name=name)
            user = form.save()  # Save the valid form data to the database
            #auth_login(request, user)  
            print("Data saved successfully")
            
            success_url = f"{reverse('success')}?name={name}"  
            return redirect(success_url)
        else:
            print("-----------------------NOT VALID !!!!---------------------------")
    else:
        form = UserRegistration()
        
    return render(request, 'registration.html', {'form': form})

# View for user login
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(f"uname : {email}, pass : {password}")
            myuser = authenticate(username=email, password=password)
            if myuser is not None:
                auth_login(request, myuser) 
                print("Login successful")
                name = myuser.email  
                success_url = f"{reverse('success')}?name={name}"
                return redirect(success_url)
            else:
                print("Invalid credentials")
        else:
            print("Form is not valid")
    else:
        form = UserLoginForm()
        
    return render(request, 'SignIn.html', {'form': form})
    

def success(request):
    name = request.GET.get('name')
    return render(request, 'new_home.html', {'name': name})
    
@login_required
def success_view(request):
    user = request.user
    # Assuming there is a one-to-one relationship between User and student_registration
    student_profile = User.objects.get(user=user)
    context = {
        'name': student_profile.name,
        'course': student_profile.course,
    }
    return render(request, 'new_home.html', context)

def user(request):
    if request.method == 'POST':
        name = request.POST.get('name1', '')
        return render(request, 'user.html', {'name': name})
    else:
        return render(request, 'user_form.html')
    
def user1(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    phone_number = request.POST.get('phone_number', '')
    age = request.POST.get('age', '')
    return render(request, "new_home.html", {'name': name, 'email': email, 'phone_number': phone_number, 'age': age})
