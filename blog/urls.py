from django.urls import path
from .views import BlogListView, DetailListView

urlpatterns = [
    path('post/<int:pk>/', DetailListView.as_view(), name = 'post_detail'),
    path('', BlogListView.as_view(), name = 'home'),
]
