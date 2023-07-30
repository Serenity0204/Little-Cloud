from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import File
from django.core.paginator import Paginator


def home_view(request):
    return render(request, "home.html")


@login_required(login_url="login")
def files_view(request, file_type=None):
    request.session.set_expiry(900)
    files_list = File.objects.filter(user=request.user)
    if file_type == "img":
        files_list = files_list.filter(file_type="img")
    if file_type == "doc":
        files_list = files_list.filter(file_type="doc")
    if file_type == "txt":
        files_list = files_list.filter(file_type="txt")
    if file_type == "pdf":
        files_list = files_list.filter(file_type="pdf")

    paginator = Paginator(files_list, 4)  # Show 4 files per page.
    page_number = request.GET.get("page")
    files = paginator.get_page(page_number)
    type_map = {
        "img": "All Image",
        None: "All",
        "doc": "All Document",
        "txt": "All Text",
        "pdf": "All PDF",
    }
    username = request.user.username
    context = {"files": files, "type": type_map.get(file_type), "username": username}
    return render(request, "files.html", context)


def login_view(request):
    if request.user.is_authenticated:
        request.session.set_expiry(
            900
        )  # Reset session expiry to 15 minutes (900 seconds)
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        # login if authenticate success
        if user is not None:
            login(request, user)
            request.session.set_expiry(
                900
            )  # Set session expiry to 15 minutes (900 seconds)
            return redirect("home")
        else:
            message = "Incorrect Username or Password Entered"
            messages.error(request, message)
            return render(request, "login.html")
    else:
        return render(request, "login.html")


def register_view(request):
    if request.user.is_authenticated:
        request.session.set_expiry(
            900
        )  # Reset session expiry to 15 minutes (900 seconds)
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        # throw error when user exists
        try:
            user = User.objects.create_user(
                username=username, password=password, email=email
            )
            login(request, user)
            request.session.set_expiry(
                900
            )  # Set session expiry to 15 minutes (900 seconds)
            return redirect("home")
        except IntegrityError:
            messages.error(request, "Username Already Exists")
            return redirect("register")
    else:
        return render(request, "register.html")


def logout_view(request):
    logout(request)
    messages.success(request, "User Logged Out")
    return redirect("login")