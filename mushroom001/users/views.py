from django.contrib.auth import logout as dj_logout, authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View


from .forms import LoginForm, SignupForm
from .models import UserInfo


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})


class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', locals())

    def post(self, request):
        register_form = SignupForm(request.POST)
        message = ""
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            work_id = register_form.cleaned_data.get('work_id')
            # gender = register_form.cleaned_data.get('gender')
            if password1 != password2:
                message = "两次密码输入不一致！！！"
                return render(request, 'signup.html', locals())
            if UserInfo.objects.filter(username=username):
                message = "该用户名已经被注册了！！！"
                return render(request, 'signup.html', locals())
            if UserInfo.objects.filter(work_id=work_id):
                message = "该工号已经被注册了！！！"
                return render(request, 'signup.html', locals())
            if UserInfo.objects.filter(email=email):
                message = "该邮箱已经被注册了！！！"
                return render(request, 'signup.html', locals())

            newUser = UserInfo()
            newUser.username = username
            newUser.email = email
            newUser.password = make_password(password1)
            newUser.work_id = work_id
            newUser.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, 'signup.html', locals())


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login.html', locals())

    def post(self, request):
        login_form = LoginForm(request.POST)
        message = ''
        if login_form.is_valid():
            user_name = login_form.cleaned_data.get('username')
            pass_word = login_form.cleaned_data.get('password')
            user = authenticate(username=user_name, password=pass_word)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
                # return HttpResponseRedirect(request.POST.get('redirect_to', reverse('index')))
                # return HttpResponse(request.POST.get('redirect_to'))
            else:
                message = "请注意检查用户名或密码是否有错误..."
                return render(request, 'login.html', locals())
        else:
            message += "请重新登录！！！"
            return render(request, 'login.html', locals())


class LogoutView(View):
    def get(self, request):
        # login_form = LoginForm()
        message = ["success", "登出成功..."]
        request.session.flush()
        return render(request, 'base.html', locals())
