from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=15)
    description = models.TextField(max_length=300)


    def __str__(self):
        return self.first_name