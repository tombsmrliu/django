from django.shortcuts import render, get_object_or_404
from .forms import LoginForm, UserRegistrationForm, ProfileEditForm, UserEditForm
from .models import Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.decorators.http import require_POST


# Create your views here.

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
                    next_url = request.POST['next']
                    if next_url == 'None':
                        return HttpResponseRedirect(reverse('minilibrary:topic_list'))
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    messages.error(request, '用户被禁用!')
            else:
                messages.error(request, '验证失败!')

        else:
            messages.error(request, '验证失败!')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form':form, 'next':request.GET.get('next')})




def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        print('Hello1')
        if user_form.is_valid():
            print('Hello2')
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            print('Hello')
            return render(request, 'account/registration_done.html', {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/registration.html', {'user_form':user_form})



@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)

        try:
            profile_form = ProfileEditForm(instance=request.user.profile,
                                        data=request.POST,
                                        files=request.FILES)
        except Profile.DoesNotExist:
            Profile.objects.create(user=request.user)
            profile_form = ProfileEditForm(instance=request.user.profile,
                                        data=request.POST,
                                        files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, '更新成功!')
            # return render(request, 'account/edit_done.html')
        else:
            messages.error(request, '更新失败!')
    else:
        user_form = UserEditForm(instance=request.user)
        try:
            profile_form = ProfileEditForm(instance=request.user.profile)
        except Profile.DoesNotExist:
            Profile.objects.create(user=request.user)
            profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form':user_form, 'profile_form':profile_form})






@login_required
def user_detail(request, username):
    print('Hello,World username is:')
    print(username)
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section':'people', 'user':user})



@login_required
def personal_center(request):
    return render(request, 'account/personal_center.html')
