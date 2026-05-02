from django.db import models

# Create your models here.

# 5 more need to be set (remember to migrate and add them to admin/views)

class Slider(models.Model):
    image_src = models.CharField(max_length=200)
    image_width = models.IntegerField()
    image_height = models.IntegerField()
    anchor_url   = models.CharField(max_length=200)
    movie_genre  = models.CharField(max_length=10)
    movie_title  = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5)
    upper_rating = models.CharField(max_length=5)

    def __str__(self):
        return self.movie_title

class Advertisement(models.Model):
    section     = models.CharField(max_length=20)
    img_src     = models.CharField(max_length=200)
    img_width   = models.IntegerField()
    img_height  = models.IntegerField()

    def __str__(self):
        return f"Ad - {self.section}"


class SocialLink(models.Model):
    name         = models.CharField(max_length=50)
    anchor_class = models.CharField(max_length=2)
    icon_class   = models.CharField(max_length=30)
    url          = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Celebrity(models.Model):
    anchor_url     = models.CharField(max_length=200)
    img_width      = models.IntegerField()
    img_height     = models.IntegerField()
    celebrity_url  = models.CharField(max_length=200)
    celebrity_name = models.CharField(max_length=50)
    celebrity_type = models.CharField(max_length=20)

    def __str__(self):
        return self.celebrity_name
    
    class Meta:
        verbose_name_plural = "Celebrities"


class Trailer(models.Model):
    trailer_URL = models.CharField(max_length=200)

    def __str__(self):
        return f"Trailer {self.id}"
    
class TrailerItem(models.Model):
    img_src     = models.CharField(max_length=200)
    img_alt     = models.CharField(max_length=100)
    img_width   = models.IntegerField()
    img_height  = models.IntegerField()
    description = models.CharField(max_length=100)
    duration    = models.CharField(max_length=10)

    def __str__(self):
        return self.description

class News(models.Model):
    section     = models.CharField(max_length=20)
    img_src     = models.CharField(max_length=200)
    img_alt     = models.CharField(max_length=100)
    img_width   = models.IntegerField()
    img_height  = models.IntegerField()
    title       = models.CharField(max_length=100)
    content     = models.CharField(max_length=500)    
    time        = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Tweet(models.Model):
    content     = models.CharField(max_length=200)

    def __str__(self):
        return self.content[:20]


class MovieTheater(models.Model):
    type            = models.CharField(max_length=20)
    img_src         = models.CharField(max_length=200)
    img_width       = models.IntegerField()
    img_height      = models.IntegerField()
    anchor_url      = models.CharField(max_length=200)
    movie_genre     = models.CharField(max_length=10)
    movie_title     = models.CharField(max_length=20)
    lower_rating    = models.CharField(max_length=5)
    upper_rating    = models.CharField(max_length=5)

    def __str__(self):
        return self.movie_title

class MovieTv(models.Model):
    type            = models.CharField(max_length=20)
    img_src         = models.CharField(max_length=200)
    img_width       = models.IntegerField()
    img_height      = models.IntegerField()
    anchor_url      = models.CharField(max_length=200)
    movie_genre     = models.CharField(max_length=10)
    movie_title     = models.CharField(max_length=20)
    lower_rating    = models.CharField(max_length=5)
    upper_rating    = models.CharField(max_length=5)

    def __str__(self):
        return self.movie_title
