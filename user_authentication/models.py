from django.db import models
from django.contrib.auth.models import User


class UserProfileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.user.username}"
