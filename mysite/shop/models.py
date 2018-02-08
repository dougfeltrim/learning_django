from django.db import models

class Sell(models.Model):
    sell_name = models.CharField(max_length=200)
    sell_price = models.IntegerField(default=0)
    sell_description = models.TextField(default="description")
    sell_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.sell_name

    def __str__(self):
        return self.sell_price

    def __str__(self):
        return self.sell_amount

    def __str__(self):
        return self.sell_description
