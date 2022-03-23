# Create your models here.
from django.db import models
from django.utils import timezone  # django工具包提供的时间模块
import datetime  # python内置的时间模块


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):  # 打印对象时会打应以下内容
        return self.question_text

    # 是否在当前发布的问卷
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):  # 打印对象时会打应以下内容
        return self.choice_text
