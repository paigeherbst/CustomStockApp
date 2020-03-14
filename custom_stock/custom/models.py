from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_symbol = models.CharField(max_length=50)
    no_shares = models.IntegerField()
    loss_gain = models.IntegerField()
    yearly_earnings = models.IntegerField()


class Investor(models.Model):

    investor = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

class Bond(models.Model):

    bond_symbol = models.CharField(max_length=50)
    quantity_of_bonds = models.IntegerField()
    loss_gainb = models.IntegerField()
    yearly_earningsb = models.IntegerField()