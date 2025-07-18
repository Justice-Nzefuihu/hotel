from django.db import models

# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=255)
    bed = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255)
    room_size = models.IntegerField()
    room_view = models.CharField(max_length=255)
    recommend = models.TextField()
    price = models.CharField(max_length=255)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self) -> str:
        return self.name