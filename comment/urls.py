from django.urls import path
from comment.views import CommentList, contact

urlpatterns = [
    path('CommentList/', CommentList.as_view()),
    path('', contact, name='contact')
]