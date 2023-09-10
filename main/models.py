from django.db import models
import uuid

class Item(models.Model):
    name = models.CharField(max_length = 255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length = 255)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)