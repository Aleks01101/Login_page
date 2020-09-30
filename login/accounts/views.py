from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, RegisterForm


def UserLoginRegister(request):
    login_form = UserLoginForm(request.POST or None)
    form = RegisterForm(request.POST or None)
    # next = request.GET.get('next')
    if request.method == "POST":
        # login_form = UserLoginForm(request.POST or None)
        # form = RegisterForm(request.POST or None)
        if request.POST.get('submit') == 'sign_in':
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username,password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        return HttpResponse('Authenticated successfully')
                    else:
                        return HttpResponse('Disabled account')
                else:
                    return HttpResponse('Invalid login')

        elif request.POST.get('submit') == 'sign_up':
            if form.is_valid():
                user = form.save(commit=False)
                password = form.cleaned_data.get('password')
                user.set_password(password)
                user.save()
                new_user = authenticate(username = user.username, password = password)
                login(request,new_user)
                return HttpResponse('You are in!')

    context = {
        'login_form' : login_form,
        'form' : form

    }
    return render(request,'loginn.html',context)


    # else:
    #     login_form = UserLoginForm()
    #     form = RegisterForm()
            
     


        
        # elif request.POST.get('submit') == 'sign_up':

        #     form = RegisterForm(request.POST or None)
        #     if form.is_valid():
        #         user = form.save(commit=False)
        #         password = form.cleaned_data.get('password')
        #         user.set_password(password)
        #         user.save()
        #         new_user = authenticate(username = user.username, password = password)
        #         login(request,new_user)
        #     context = {
        #         'form': form
        #     }
        #     return render(request,'logform/login.html',context)
    
        
        



