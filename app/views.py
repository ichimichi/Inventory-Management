from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import TransactionDetails, Transaction, Item, Department, DEPARTMENT_TYPE

def index(request):
  return render(request, 'app/index.html', {})

def department(request, department_id):
  transactions = Transaction.objects.filter(department = department_id)[:5]
  transactions = [(t.date, t.type) for t in transactions]
  return render(request, 'app/department.html', {'transactions': transactions, 'name': dict(DEPARTMENT_TYPE)[department_id]})

def inventory(request, department_id):
  items = [e.id for e in Item.objects.all()]
  names = [' '.join([e.brand,e.name]) for e in Item.objects.all()]
  inv = {}
  for item, name in zip(items,names):
    inv[name] = TransactionDetails.objects.filter(transaction__department=department_id, transaction__type='O', item__id=item).aggregate(Sum('quantity'))['quantity__sum']
  return render(request, 'app/inventory.html', {'d': inv, 'name': dict(DEPARTMENT_TYPE)[department_id]})

def employee(request, department_id):
  return HttpResponse("You're looking for employee {}".format(department_id))