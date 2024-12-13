from django.db import models

class Properity(models.Model):

    place=models.CharField(max_length=100)

    price=models.PositiveIntegerField()

    category=(
        ("House","House"),
        ("Flat","Flat"),
        ("Apartment","Apartment"),
        ("Villa","Villa"),
        ("Plot","Plot")
    )

    category_option=models.CharField(max_length=100,choices=category,default="House")

    bedroom_count=models.PositiveIntegerField()

    squarefootage=models.PositiveIntegerField()

    def __str__(self):
        return self.place









