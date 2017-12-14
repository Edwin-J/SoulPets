from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Pet(models.Model) :
    title = models.CharField(max_length = 20)
    kind = models.CharField(max_length = 10)
    price = models.IntegerField()
    info = models.TextField(max_length = 300, default = "정보를 300자 이내로 작성하여 주세요.")
    imgs = models.ImageField()

    def __str__(self)   :
        return self.title
