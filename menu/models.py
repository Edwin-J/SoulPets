from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Pet(models.Model) :
    title = models.CharField(max_length = 20)
    kind = models.CharField(max_length = 10)
    price = models.IntegerField(max_length = 10)
    info = models.TextField(max_length = 300, default = "정보를 300자 이내로 작성하여 주세요.")
    imgs = models.ImageField()
    hits = models.IntegerField(null = True, blank = True)

    def __str__(self)   :
        return self.title

class Comment(models.Model) :
    post = models.ForeignKey(Pet, related_name="comments")
    writer = models.ForeignKey(User)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return self.text
