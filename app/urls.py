from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
  path('', views.PostList.as_view(), name='home'),
  path('<slug:slug>/', views.DetailView.as_view(), name='post_detail'),

]