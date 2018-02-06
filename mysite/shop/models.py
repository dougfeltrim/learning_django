from django.db import models

class Sell(models.Model):
    sell_name = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    #sell_image = models.ImageField()
    sell_price = models.DecimalField(max_digits=6, decimal_places=2)
    sell_amount = models.IntegerField(default=0)
    sell_description = models.TextField(default="description")

    def __str__(self):
        return self.sell_name
