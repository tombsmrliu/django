from django.shortcuts import render, get_object_or_404
from .forms import LoginForm, UserRegistrationForm, ProfileEditForm, UserEditForm
from .models import Profile, Contact
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from actions.utils import create_action
from actions.models import Action


# Create your views here.

@login_required
def dashboard(request):
    actions = Action.objects.exclude(user=request.user)
    following_ids = request.user.following.values_list('id', flat=True)
    if following_ids:
        actions = actions.filter(user_id__in=following_ids).select_related('user', 'user__profile').prefetch_related('target')

    actions=actions[:10]
    print(actions)
    return render(request, 'account/dashboard.html', {'section':'dashboard', 'actions':actions})



def user_login(request):
    # if request.user.is_authenticated:
        # if next:
            # HttpResponseRedirect(next)
        # return HttpResponseRedirect(reverse('account:dashboard'))

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
                        return HttpResponseRedirect(reverse('account:dashboard'))
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponse('用户被禁用!')
            else:
                return HttpResponse('验证失败！')

        else:
            return HttpResponse('验证失败！')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form':form, 'next':request.GET.get('next')})




def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            create_action(new_user, '创建了新账户')
            new_user.save()
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
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/list.html', {'section':'people', 'users':users})


@login_required
def user_detail(request, username):
    print('Hello,World username is:')
    print(username)
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section':'people', 'user':user})



@login_required
@require_POST
def user_follow(request):
    print('Hello')
    user_id = request.POST['id']
    action = request.POST['action']
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)

            # 个人觉得这里有漏洞，如果用户已经关注了这个人，但是通过修改表单中的值恶意传过来'follow'呢？
            # 个人认为应该在后台判断请求的用户是不是在关注列表里，然后进行操作，而不是在模板中判断，然后传值。
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
                create_action(request.user, '关注了', user)
                messages.success(request, '关注成功!')
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
                messages.success(request, '取关成功!')
        except User.DoesNotExist:
            messages.error('用户不存在!')
    # 坑，方法别忘了加括号
    return HttpResponseRedirect(user.get_absolute_url())

