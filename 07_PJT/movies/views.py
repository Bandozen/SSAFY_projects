from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Actor, Movie, Review
from .serializers import ActorSerializer, MovieSerializer, ReviewSerializer, ActorListSerializer, MovieListSerializer, ReviewListSerializer

# Create your views here.

# actor_list함수
@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)

#actor_detail함수
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk = actor_pk)
    serializers = ActorSerializer(actor)
    return Response(serializers.data)

# movie_list함수
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# movie_detail함수
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)

# review_list함수
@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

# review_detail함수
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = Review.objects.get(pk = review_pk)
    if request.method == "GET":
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        review.delete()
        context = {
            "delete" : f"리뷰 {review_pk}번 글이 삭제되었습니다!"
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)
        
    elif request.method == "PUT":
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
# create_review함수
@api_view(['POST'])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie = movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)