from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(null=True)
    marks = models.FloatField()
    course = models.CharField(max_length=100)
    admsnType= models.CharField(max_length=20)

    def __str__(self):
        return self.name