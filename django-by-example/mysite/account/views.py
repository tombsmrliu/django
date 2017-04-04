from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section':'dashboard'})





def user_login(request):

    # 先判断是不是POST方法提交请求
    if request.method == 'POST':
        form = LoginForm(request.POST)

        # 在获得表单，并判断表单是否可用
        if form.is_valid():
            cd = form.cleaned_data

            # 取得表单数据，并根据表单数据认证用户
            user = authenticate(username=cd['username'], password=cd['password'])

            # 如果认证成功，这说名用户存在
            if user: # 排除User认证失败的情况
                # 在判断用户是不是被禁用账号了

                if user.is_active:
                    login(request, user)
                    return HttpResponse('登陆成功!')
                else:
                    return HttpResponse('用户被禁用!')
            else:
                return HttpResponse('验证失败！')

        else:
            return HttpResponse('验证失败！')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form':form})
