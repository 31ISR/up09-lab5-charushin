from django.contrib import admin
from django.urls import path
from . import views
from .views import CommunityCreateView

app_name = 'communities'

urlpatterns = [
    path('', views.communities_list, name="list"),
    path('<slug:slug>', views.community_page, name="page"),
    path('new/', CommunityCreateView.as_view(), name='community-new'),
]


