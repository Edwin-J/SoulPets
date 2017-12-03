from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Pet(models.Model) :
    title = models.CharField(max_length = 20)
    writer = models.ForeignKey(User)
    date = models.DateTimeField(default = timezone.now)
    kind = models.CharField(max_length = 10)
    price = models.IntegerField()
    image = models.ImageField()
    
    def __str__(self)   :
        return self.title
