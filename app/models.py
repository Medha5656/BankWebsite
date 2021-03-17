from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class Customer(models.Model):
	fname=models.CharField(max_length=15)
	lname=models.CharField(max_length=15)
	Email=models.EmailField(max_length=40)
	balance=models.FloatField(validators=[MinValueValidator(1.00)])

	def __str__(self):
		return self.fname

class Transaction(models.Model):
	trans_from=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="trans_from")
	trans_to=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="trans_to")
	ammount=models.FloatField(validators=[MinValueValidator(1.00)])
	time=models.DateTimeField(auto_now_add=True)