from django.shortcuts import render,redirect
from .forms import RegisterForm,UserUpdateForm,TaskForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from .models import TaskModel
# Create your views here.
def signUp(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account Created Successfully..')
                
                form.save(commit=True)
                # print(form.cleaned_data)
                form = RegisterForm()
        else:
            form = RegisterForm()
        return render(request,"signUp.html",{'form':form})
    else:
        return redirect('profile')
def home(req):
    return render(req,'home.html')
def profile(request):
    if request.user.is_authenticated:
        if request.session.get('password_updated'):
            del request.session['password_updated']
            return render(request, 'profile.html', {'user': request.user, 'password_updated': True})
        if request.session.get('profile_updated'):
            del request.session['profile_updated']
            return render(request, 'profile.html', {'user': request.user, 'profile_updated': True})
        return render(request, 'profile.html', {'user': request.user, 'password_updated': False})
    else:
        return redirect('login')


def loginView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')  
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')
def logoutView(request):
    logout(request)
    return redirect('login')

def changePassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                request.session['password_updated'] = True
                return redirect('profile')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'changePassword.html', {'form': form})
    else:
        return redirect('login')

def setPassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                request.session['password_updated'] = True
                return redirect('profile')
        else:
            form = SetPasswordForm(request.user)
        return render(request, 'setPassword.html', {'form': form})
    else:
        return redirect('login')

def userUpdate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                # messages.success(request, 'Your profile information was successfully updated!')
                request.session['profile_updated'] = True
                return redirect('profile')
        else:
            form = UserUpdateForm(instance=request.user)
        return render(request, 'userUpdate.html', {'form': form})
    else:
        return redirect('login')

def addTask(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('showTasks')
        else:
            form = TaskForm()
        return render(request, 'addTask.html', {'form': form})
    else:
        return redirect('login')
def showTasks(request):
    if request.user.is_authenticated:
        # tasks = TaskModel.objects.all()
        incomplete_tasks = TaskModel.objects.filter(is_completed=False)
        return render(request, 'showTasks.html', {'tasks': incomplete_tasks})
    else:
        return redirect('login')

def deleteTask(request, task_id):
    if request.user.is_authenticated:
        task = TaskModel.objects.get(pk=task_id)
        task.delete()
        return redirect('showTasks')
    else:
        return redirect('login')

def editTask(request, task_id):
    if request.user.is_authenticated:
        task = TaskModel.objects.get(pk=task_id)
        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('showTasks')
        else:
            form = TaskForm(instance=task)
        return render(request, 'editTask.html', {'form': form})
    else:
        return redirect('login')
    
def completeTask(request, task_id):
    if request.user.is_authenticated:
        task = TaskModel.objects.get(pk=task_id)
        task.is_completed = True
        task.save()
        return redirect('completedTasks')
    else:
        return redirect('login')
    
def completedTasks(request):
    if request.user.is_authenticated:
        completedTasks = TaskModel.objects.filter(is_completed=True)
        return render(request, 'completedTasks.html', {'completed_tasks': completedTasks})
    else:
        return redirect('login')


def deleteCompletedTask(request, task_id):
    if request.user.is_authenticated:
        task = TaskModel.objects.get(pk=task_id)
        task.delete()
        return redirect('completedTasks')
    else:
        return redirect('login')