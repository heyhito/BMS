from django.db import models

# Create your models here.
class Book_Messages(models.Model):
    name = models.CharField(max_length=16,null=True)
    price = models.IntegerField(default=1)
    data = models.DateField()
    press = models.CharField(max_length=16,null=True)
    def __str__(self):
        return self.name