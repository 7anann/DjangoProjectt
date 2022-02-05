from django.db import models


# Create your models here.
class myuser(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    profile_picture = models.ImageField()
    country = models.CharField(max_length=20, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    fb_account = models.URLField(blank=True)

    def __str__(self):
        return self.Email
