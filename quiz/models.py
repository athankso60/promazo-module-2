
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

class Quiz(models.Model):
    quiz_title = models.CharField(max_length=50)
    quiz_difficulty = models.IntegerField(default=0)
    quiz_description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    class Meta:
        ordering = ['created', ]
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.quiz_title


class Question(models.Model):
    quiz_foreign_key = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=50)
    question_text = models.CharField(max_length=100)
    is_multi_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.question_title


class Answer(models.Model):
    question_foreign_key = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_title = models.CharField(max_length=50)
    answer_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    number_of_points = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text

