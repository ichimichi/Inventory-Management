from django.db import models

# Create your models here.
DEPARTMENT_TYPE = (
    ('CSE', 'Computer Science Engineering'),
    ('ECE', 'Electronic Communication Engineering'),
    ('EEE', 'Electronical Electronic Engineering'),
    ('CE', 'Civil Engineering'),
    ('ME', 'Mechanical Engineering'),
    ('WH', 'Ware House')
)

TRANSACTION_TYPE = (
   ('I', 'Incoming'),
   ('O', 'Outoing')
)

class Department(models.Model):
    name = models.CharField(choices=DEPARTMENT_TYPE, max_length=128, primary_key=True)

    def num_emp(self):
        return Employee.objects.filter(department = self.name).count()
    num_emp.short_description = 'Number of Employees'

    def __str__(self):
        return str(self.name)


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.IntegerField(default=0)
    department = models.ForeignKey(Department, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.first_name)+' '+str(self.last_name)


class Item(models.Model):
    name = models.CharField(max_length=64)
    brand = models.CharField(max_length=64)

    @property
    def quantity(self):
        in_sum = 0
        out_sum = 0
        for t in TransactionDetails.objects.filter(transaction__type='O', item=self.id):
            out_sum += t.quantity
        for t in TransactionDetails.objects.filter(transaction__type='I', item=self.id):
            in_sum += t.quantity
        return in_sum-out_sum

    def __str__(self):
        return str(self.brand)+' '+str(self.name)


class Transaction(models.Model):
    department = models.ForeignKey(Department, on_delete= models.DO_NOTHING)
    type = models.CharField(choices=TRANSACTION_TYPE, max_length=128)
    date = models.DateTimeField()


class TransactionDetails(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete= models.DO_NOTHING)

    quantity = models.IntegerField(default=1)



