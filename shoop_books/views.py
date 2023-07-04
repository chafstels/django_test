from django.http import HttpResponse
from django.shortcuts import render

from .models import Users


# Create your views here.

def users_list(request):
    queryset = Users.objects.all()
    print((queryset))
    # return HttpResponse("<h1>Hello world</h1>")
    return render(request, 'listing.html', {'users': queryset})