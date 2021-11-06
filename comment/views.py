from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from comment.models import Comment
from comment import serializers
from account import models

# Create your views here.

class CommentList(ListCreateAPIView):
    serializer_class = serializers.Comment
    queryset = Comment.objects.all()


def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    else:
        title = request.POST['title']
        description = request.POST['description']
        user = models.User.objects.all()[1]
        Comment.objects.create(title=title, description=description, user=user)
        return render(request, 'index.html')
