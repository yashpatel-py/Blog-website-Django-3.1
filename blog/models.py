from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    cat = models.CharField(max_length=400)
    slug = models.CharField(max_length=400)
    views = models.IntegerField(default=0)
    disp = models.TextField()
    timestamp = models.DateTimeField(blank=True)
    thumbnail = models.ImageField(upload_to="blog/thumbnails", default="")

    def __str__(self):
        return self.title + ' by ' + self.author
    