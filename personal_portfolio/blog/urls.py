from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings # gets settings from settings.py file
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]

