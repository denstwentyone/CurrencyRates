from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class CurrencyRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False, unique=True)
    rate = models.FloatField()

    def __str__(self):
        return str(self.date)
