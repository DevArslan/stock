from django.db import models




class stockAPIData(models.Model):

    index = models.AutoField(primary_key=True)
    Id = models.IntegerField()
    title = models.CharField(max_length = 255)
    amount = models.IntegerField()
    unit = models.CharField(max_length = 255)
    price = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)

class resourcesData(models.Model):
    resources = models.ForeignKey(stockAPIData, on_delete=models.SET_NULL, blank = True, null = True, related_name='stock', verbose_name = "resources")
    # total_count = stockAPIData.objects.count()
    # 'self', on_delete=models.SET_NULL, blank = True, null = True, related_name='stock')