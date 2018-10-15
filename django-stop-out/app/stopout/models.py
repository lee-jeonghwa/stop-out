from django.db import models


class School(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=20)

    friends = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        return self.name
