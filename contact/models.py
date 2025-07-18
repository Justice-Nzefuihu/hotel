from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    Contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname