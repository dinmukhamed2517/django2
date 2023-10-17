from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from api.forms import ProblemForm, UserLoginForm
from api.models import Problem


def problem_create(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.reported_by = request.user
            problem.save()
            return redirect('problem_list')
    else:
        form = ProblemForm()
    return render(request, 'problem_create.html', {'form': form})


def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'problem_list.html', {'problems': problems})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('problems/')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})
