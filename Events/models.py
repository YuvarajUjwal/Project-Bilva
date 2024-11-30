from django.db import models

# Create your models here.

class Tags(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

class Galeries(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.tag.category

class Enquire(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField(null=True)

class Feedbacks(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField(null=True)