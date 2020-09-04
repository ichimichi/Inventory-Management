from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import TransactionDetails, Transaction, Item, Department, DEPARTMENT_TYPE

def index(request):
  return HttpResponse("Hello, welcome to the inventory management project.")

def department(request, department_id):
  transactions = Transaction.objects.filter(department = department_id)
  output = ', '.join([str(str(t.date) + t.type) for t in transactions])
  return HttpResponse(output)

def inventory(request, department_id):
  num_items = Item.objects.count()
  counts = [0]*num_items
  items = []
  transactions = Transaction.objects.filter(department = department_id)
  t_details = [TransactionDetails.objects.filter(transaction=t) for t in transactions]
  for t in t_details:
    for t_ in t:
      counts[t_.item_id-1] += t_.quantity

  inv = {}
  for i, count in enumerate(counts):
    name = ' '.join([x for x in Item.objects.filter(id=i+1).values_list('brand','name')[0]])
    inv[name] = count
  return render(request, 'app/inventory.html', {'d': inv, 'name': dict(DEPARTMENT_TYPE)[department_id]})

def employee(request, department_id):
  return HttpResponse("You're looking for employee {}".format(department_id))