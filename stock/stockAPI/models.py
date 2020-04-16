from django.db import models

class stockAPIData(models.Model):

    index = models.AutoField(primary_key=True)
    Id = models.IntegerField()
    title = models.CharField(max_length = 255)
    amount = models.IntegerField()
    unit = models.CharField(max_length = 255)
    price = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
