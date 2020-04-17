from django.db import models

class stockAPIData(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 255)
    amount = models.IntegerField()
    unit = models.CharField(max_length = 255)
    price = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
