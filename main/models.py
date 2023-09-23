from django.db import models
from django.contrib.auth.models import User
import uuid

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length = 255)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)