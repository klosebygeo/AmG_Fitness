from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Enrollment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # FullName = models.CharField(max_length=25)
    Email = models.EmailField()
    Gender = models.CharField(max_length=25)
    PhoneNumber = models.CharField(max_length=12)
    SelectMembershipplan = models.CharField(max_length=100)
    SelectTrainer = models.CharField(max_length=55)
    Address = models.CharField(max_length=300, null=True)
    paymentStatus = models.CharField(max_length=55, blank=True, null=True)
    Price = models.IntegerField(max_length=55, blank=True, null=True)
    DueDate = models.DateTimeField(blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Trainer(models.Model):
    name = models.CharField(max_length=55)
    gender = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class MembershipPlan(models.Model):
    plan = models.CharField(max_length=185, null=False)
    price = models.IntegerField(null=False)

    def __str__(self):
        return str(self.id)
