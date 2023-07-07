from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from .models import Users, Books
from .serializers import UsersSerializer, BooksSerializer


# Create your views here.

def users_list(request):
    queryset = Users.objects.all()
    # return HttpResponse("<h1>Hello world</h1>")
    return render(request, 'listing.html', {'users': queryset})

#REST
@api_view(['GET'])
def users_list_api_view(request):
    queryset = Users.objects.all()
    serializer = UsersSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_detail(request, id):
    # try:
    #     user = Users.objects.get(id=id)
    #     serializer = UsersSerializer(user)
    #     return Response(serializer.data)
    # except Users.DoesNotExist:
    #     return Response('такого обьекта нет')

    user = get_object_or_404(Users, id=id)
    serializer = UsersSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def create_users(request):
    serializer = UsersSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)

@api_view(['DELETE'])
def delete_users(request, id):
    user = get_object_or_404(Users, id=id)
    user.delete()
    return Response(status=204)

@api_view(['PUT','PATCH'])
def update_users(request, id):
    user = get_object_or_404(Users, id=id)
    partial = True if request.method == "PATCH" else False
    serializer = UsersSerializer(instance=user, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


#APIView
class BooksListAPIView(APIView):
    def get(self, request):
        queryset = Books.objects.all()
        serializer = BooksSerializer(queryset, many=True)
        return Response(serializer.data)


class BooksDetailAPIView(APIView):
    def get(self, request, id):
        book = get_object_or_404(Books, id=id)
        serializer = BooksSerializer(book)
        return Response(serializer.data)

class BooksCreateAPIView(APIView):
    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class BooksDeleteAPIView(APIView):
    def delete(self, request, id):
        books = get_object_or_404(Books, id=id)
        books.delete()
        return Response(status=204)

class BooksUpdateAPIView(APIView):
    def put(self, request, id):
        book = get_object_or_404(Books, id=id)
        serializer = BooksSerializer(book, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    def patch(self, request, id):
        book = get_object_or_404(Books,id=id)
        serializer = BooksSerializer(book, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


