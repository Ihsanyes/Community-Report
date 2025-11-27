from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from .models import CustomUser

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")   # FIXED
        confirm_password = request.POST.get("password2")  # FIXED

        # Required fields check
        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required")
            return redirect("/signup/")

        # Password match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("/signup/")

        # Username exists
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("/signup/")

        # Email exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("/signup/")

        # Create user
        user = CustomUser.objects.create_user(username=username, email=email)
        user.set_password(password)  # No validator issues
        user.save()

        messages.success(request, "Registration successful!")
        return redirect("/login/")

    return render(request, "userapp/signup.html")




def login_view(request):
    if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            if not username or not password:
                messages.error(request, "Both fields are required")
                return redirect("/login/")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/')
            else:
                messages.error(request, "Invalid username or password")
    return render(request, "userapp/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('/login/')

def home(request):
    #oakgdpfokgaodkg
    return render(request, 'userapp/home.html')


