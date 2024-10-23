from django.db import models

class Movie(models.Model):

    title=models.CharField(max_length=200)

    genre=models.CharField(max_length=200)

    year=models.PositiveBigIntegerField()

    runtime=models.PositiveBigIntegerField()

    language=models.CharField(max_length=200)

    rating=models.PositiveBigIntegerField()

    def __str__(self):
        return self.title
