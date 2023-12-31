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
from shoop_books.views import users_list, users_list_api_view, user_detail, create_users, delete_users, update_users, \
    BooksListAPIView, BooksDetailAPIView, BooksCreateAPIView, BooksDeleteAPIView, BooksUpdateAPIView
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
    path('api/listing/', users_list_api_view),
    path('api/usersdetail_shoop/<int:id>/', user_detail),
    path('api/usersdetail_shoop/create/', create_users),
    path('api/usersdetail_shoop/delete/<int:id>/', delete_users),
    path('api/usersdetail_shoop/update/<int:id>/', update_users),
    path('api/books_list/', BooksListAPIView.as_view()),
    path('api/books_detail/<int:id>/', BooksDetailAPIView.as_view()),
    path('api/books_create/', BooksCreateAPIView.as_view()),
    path('api/books_delete/<int:id>/', BooksDeleteAPIView.as_view()),
    path('api/books_update/<int:id>/', BooksUpdateAPIView.as_view()),

]
