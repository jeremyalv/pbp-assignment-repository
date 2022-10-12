from cmath import isfinite
import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from todolist.forms import TaskForm
from django.views.decorators.csrf import csrf_exempt



@login_required(login_url='/todolist/login/')
def show_todolist(request):
    context = {
        'username': request.user.get_username(),
    }

    return render(request, 'todolist.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat!')
            return redirect('todolist:login')
        
    context = {'form' : form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist'))
            # response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau password salah!')
    
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/todolist/login/')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    # response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date = datetime.datetime.today()
        description = request.POST.get('description')
        form = TaskForm(request.POST)

        Task.objects.create(
            user = request.user,
            title = title,
            description = description,
            date = date,
            is_finished = False,
        )

        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    else:
        form = TaskForm()
        messages.info(request, 'Input salah')
    
    context = {'form' : form}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
@csrf_exempt
def create_task_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.today()

        Task.objects.create(
            user = request.user,
            title = title,
            description = description,
            date = date,
            is_finished = False,
        )

        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    else:
        messages.info(request, "INPUT SALAH")

    return (request, 'show_todolist.html')
    
    

@login_required(login_url='/todolist/login')
def delete_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.delete()

    return HttpResponseRedirect(reverse("todolist:show_todolist"))

@login_required(login_url='/todolist/login/')
@csrf_exempt
def delete_task_ajax(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.delete()

    return HttpResponseRedirect(reverse("todolist:show_todolist"))

@login_required(login_url='/todolist/login')
def toggle_task_status(request, id):
    task = Task.objects.get(id=int(id), user=request.user)
    task.is_finished = not task.is_finished
    task.save(update_fields=['is_finished'])

    return HttpResponseRedirect(reverse("todolist:show_todolist"))

@login_required(login_url='/todolist/login')
def get_json(request):
    data = Task.objects.filter(user=request.user)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

