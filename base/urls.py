from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',TaskList.as_view(),name='tasks'),
    path('task-detail/<int:pk>/',TaskDetail.as_view(),name='TaskDetails'),
    path('task-create/',TaskCreate.as_view(),name='TaskCreate'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='TaskUpdate'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='TaskDelete'),

    path('login/',LoginUser.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
]