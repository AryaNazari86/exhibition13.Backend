from django.shortcuts import render
from article import models


# Create your views here.
def home(request):
    return render(request, 'index.html', {'articles': models.Article.objects.all()})


def members(request):
    return render(request, 'members.html')
