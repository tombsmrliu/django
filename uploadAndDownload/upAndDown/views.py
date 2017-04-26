from django.shortcuts import render
from .models import UploadFileModel
from django.http import HttpResponse
from .forms import UploadFileForm

# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = UploadFileModel(file=request.FILES['file'])
            instance.save()
            return HttpResponse('上传成功')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form':form})

