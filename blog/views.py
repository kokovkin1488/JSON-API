from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import *
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class AllView(APIView):
    def get(self, request):
        return Response('get all')


class PostCreate(APIView):
    @staticmethod
    def get(request):
        user_ip = request.META.get('REMOTE_ADDR')
        user_login = request.GET.get('login', False)
        post_title = request.GET.get('title', False)
        post_text = request.GET.get('text', False)

        if not user_login or not post_title or not post_text:
            response = {"error": "One of the parameters 'login' or 'post_title' or 'post_text' in the request is empty"}
            response_status = status.HTTP_422_UNPROCESSABLE_ENTITY
        else:
            user = User.objects.get_or_create(login=user_login)
            Post.objects.create(user=user[0], title=post_title, text=post_text, ip=user_ip)
            response_status = status.HTTP_200_OK
            response = "200 OK"
        return Response(response, status=response_status)


class RatingSet(APIView):
    @staticmethod
    def get(request):
        # user_ip = request.META.get('REMOTE_ADDR')
        post_id = int(request.GET.get('post_id', False))
        user_id = int(request.GET.get('user_id', False))
        value = int(request.GET.get('value', False))

        if post_id == '' or user_id == '' or value == '':
            response = {"error": "One of the parameters 'post_id' or 'user_id' or 'value' in the request is empty"}
            response_status = status.HTTP_422_UNPROCESSABLE_ENTITY

        elif isinstance(post_id, int) and isinstance(user_id, int) and isinstance(value, int):
            if (not value > 5) and (not value < 1):
                try:
                    user = User.objects.get(id=user_id)
                    post = Post.objects.get(id=post_id)
                    Rating.objects.create(user=user, post=post, rating=value)
                    average_value = post.rating_set.aggregate(Avg('rating'))
                    response = {"average value": round(average_value['rating__avg'], 2)}
                    response_status = status.HTTP_200_OK
                except ObjectDoesNotExist:
                    response = {"error": "Either the user or post doesn't exist."}
                    response_status = status.HTTP_404_NOT_FOUND
                    return Response(response, response_status)
            else:
                response = {"error": "Value must be in the range of 0 to 5"}
                response_status = status.HTTP_422_UNPROCESSABLE_ENTITY

        else:
            response = {"error": "Unknown error in the request"}
            response_status = status.HTTP_422_UNPROCESSABLE_ENTITY
        return Response(response, status=response_status)


class GetTopPosts(APIView):
    @staticmethod
    def get(request):

        return Response()
