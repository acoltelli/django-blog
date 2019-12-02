from django.urls import path

from .views import (
    postListView,
    postUpdateView,
    postDetailView,
    postDeleteView,
    postCreateView  # new
)

urlpatterns = [
    path('<int:pk>/edit/',
         postUpdateView.as_view(), name='postEdit'),
    path('<int:pk>/',
        postDetailView.as_view(), name='postDetail'),
    path('<int:pk>/delete/',
         postDeleteView.as_view(), name='postDelete'),
    path('new/', postCreateView.as_view(), name='postNew'),
    path('', postListView.as_view(), name='postList'),
]
