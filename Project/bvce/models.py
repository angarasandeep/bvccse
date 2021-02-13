from django.db import models

# Create your models here.
class Year(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Textbook(models.Model):
    image = models.URLField(max_length=500)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=256,blank=True)
    link = models.URLField(max_length=500)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
