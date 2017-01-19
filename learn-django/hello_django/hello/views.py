from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse

# Create your views here.
def hello(request):
    user_list = User.objects.all()
    return render(request, 'table.html', {'user_list':user_list})

def test(request, id, key):
    print(id)
    print(key)
    return render(request, "table.html")
