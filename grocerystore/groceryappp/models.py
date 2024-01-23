from django.db import models
# Create your tests here.
class Grocery(models.Model):
    type=(('oil','Oil'),('grains','Grains'),('cosmetics','Cosmetics'))
    name=models.CharField(max_length=50)
    type=models.CharField(choices=type,max_length=50)
    quantity=models.IntegerField()
    rate=models.FloatField()
    amount=models.IntegerField()