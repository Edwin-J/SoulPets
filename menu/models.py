from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Pet(models.Model) :
    title = models.CharField(max_length = 20)
    kind = models.CharField(max_length = 10)
    price = models.IntegerField()
    info = models.TextField(null = True, blank = True)
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    hits = models.IntegerField(null = True, blank = True, default = 0)
    imgs = models.ImageField()

    def publish(self) :
        self.published_date = timezone.now()
        self.save()

    def __str__(self)   :
        return self.title

class Comment(models.Model) :
    post = models.ForeignKey(Pet, related_name="comments")
    writer = models.ForeignKey(User)
    text = models.TextField(null = True, blank = True)
    created_date = models.DateTimeField(default=timezone.now)
    approve_comment = models.BooleanField(default=False)

    def approve(self) :
        self.approved_comment = True
        self.save()

    def __str__(self) :
        return self.text
