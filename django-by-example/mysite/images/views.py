from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.views.decorators.http import require_POST
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# Create your views here.



@login_required
def image_create(request):
    if request.method == 'POST':

        form = ImageCreateForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, '图片上传成功!')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html', {'form':form})



@login_required
def image_detail(request,id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/image_detail.html',{'image':image})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST['id']
    action = request.POST['action']
    print('get request')
    print(request.path)
    if image_id:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            messages.error(request, '状态更新成功!')
        except:
            messages.error(request, '状态更新失败!')
    return HttpResponseRedirect(reverse('images:detail', args=[image.id, image.slug]))

@login_required
def images_list(request):
    images = Image.objects.all()
    return render(request, 'images/image/image_list.html', {'images':images, 'section':'images'})
