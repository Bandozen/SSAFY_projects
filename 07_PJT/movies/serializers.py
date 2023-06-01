from rest_framework import serializers
from .models import Actor, Movie, Review

# movietitle 적용하기'
class MovieTitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)
        
# review detail 전용        
class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = "__all__"

# review list 전용
class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ("title", "content")
        read_only_fields = ('movie',)
        
# movie안에 actorname적용하기
class ActorNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = ('name',)
        
# movie detail 전용        
class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewListSerializer(many=True, read_only=True)
    actors = ActorNameSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = "__all__"
        
# movie list전용
class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title', 'overview',)

# actor detail전용
class ActorSerializer(serializers.ModelSerializer):
    movies = MovieTitleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = "__all__"

# actor list전용
class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = ('id', 'name')