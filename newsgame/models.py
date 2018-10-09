from django.db import models



class Entity(models.Model):
    name = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.name


class QNA(models.Model):
    question = models.CharField(unique=True, max_length=500)
    answer = models.CharField(max_length=500)
    entity = models.ManyToManyField(Entity, blank=True)

    def __str__(self):
        return self.question


class Quiz(models.Model):
    name = models.CharField(unique=True, max_length=500)
    qna = models.ManyToManyField(QNA, blank=True)

    def __str__(self):
        return self.name