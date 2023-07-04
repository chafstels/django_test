"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from post.views import PostAPIView, PostAPIList
from shoop_books.views import users_list
from university.views import StudentAPIList, StudentAPIUpdate, StudentAPIDetailView, CourseAPIList, CourseAPIUpdate, CourseAPIDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/post/", PostAPIList.as_view()),
    path("api/v1/post/<int:pk>/", PostAPIView.as_view()),
    path('users_list/', users_list),
    path('api/v1/student/', StudentAPIList.as_view()),
    path('api/v1/student/<int:pk>/', StudentAPIUpdate.as_view()),
    path('api/v1/course/', CourseAPIList.as_view()),
    path('api/v1/course/<int:pk>/', CourseAPIDetailView.as_view()),
]
