from django.db import models

from user_authentication.models import UserProfileModel

import base64

class UserGeneratedPasswordModel(models.Model):

    CATHERORIES = [
        ('Sport','Sport'),
        ('Social media','Social media'),
        ('Programming and IT','Programming and IT'),
        ('Coocking','Coocking'),
        ('Art / Drawing','Art / Drawing'),
        ('Math','Math'),
        ('Language','Language'),
        ('Science','Science'),
        ('Robotics','Robotics'),
        ('Dancing','Dancing'),
        ('Dancing','Dancing'),
        ('Music / Singing','Music / Singing'),
        ('Video games' , 'Video games'),
        ('Yoga / Mediatation','Yoga / Mediatation'),
        ('Martial arts','Martial arts'),
        ('Design','Design'),
        ('School / University','School / University'),

    ]
    userID = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30,choices=CATHERORIES)
    password = models.CharField(max_length=45)
    creation_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.password =  base64.b64encode(self.password.encode('ascii')).decode('ascii')
        super(UserGeneratedPasswordModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"User:{self.userID.user.username},cat:{self.category}"