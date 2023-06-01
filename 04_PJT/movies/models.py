from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_Date = models.DateField()
    스릴러 = '스릴러'
    코미디 = '코미디'
    공포 = '공포'
    로맨스 = '로맨스'
    genre_choices = [
        (스릴러, '스릴러'),
        (코미디, '코미디'),
        (공포, '공포'),
        (로맨스, '로맨스'),
    ]
    genre = models.CharField(max_length=30,
                             choices=genre_choices,
                             default=스릴러,)
    score = models.FloatField()
    poster_url = models.CharField(max_length=300)
    actor_image = models.ImageField(blank=True)
    description = models.TextField()
    