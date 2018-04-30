from django.db import models

# Create your models here.

class My(models.Model):
    image_name = models.CharField(max_length=9999, default="")


class Gmy(models.Model):
    gif_name = models.CharField(max_length=9999, default="")


class Time(models.Model):
    update_time = models.CharField(max_length=9999, default="")


class UploadFileModel(models.Model):
    file = models.ImageField(null=True, upload_to='%Y-%m-%d/')

