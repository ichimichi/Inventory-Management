from django.db import models

# Create your models here.
class Employee(models.Model):
    # emp_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

class Item(models.Model):
    # item_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)


TRANSACTION_TYPE = (
   ('I', 'Incoming'),
   ('O', 'Outoing')
)

class Transaction(models.Model):
    employee = models.ForeignKey(Employee, on_delete= models.DO_NOTHING)
    type = models.CharField(choices=TRANSACTION_TYPE, max_length=128)
    date = models.DateTimeField()

class TransactionDetails(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete= models.DO_NOTHING)
    quanity = models.IntegerField(default=0)



