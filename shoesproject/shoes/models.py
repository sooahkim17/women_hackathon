from django.db import models

# Create your models here.
class Shoes(models.Model):
    shoes_title=models.CharField(max_length=300)
    shoes_image=models.URLField(null=True)
    shoes_body=models.TextField(max_length=500)

    def __str__(self):
        return self.shoes_title

    def summary(self):
        return self.shoes_body[:50]


class Suggestions(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(max_length=500)

    def __str__(self):
        return self.title
        
    def __summary(self):
        return self.body[:50]