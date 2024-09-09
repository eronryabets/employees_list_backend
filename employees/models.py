from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    position = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    years_worked = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    facebook_link = models.URLField(blank=True, null=True)
    avatar_link = models.URLField(blank=True, null=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.date_of_birth}'
