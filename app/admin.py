from django.contrib import admin

# Register your models here.

from app.models import Employee, Item, Transaction, TransactionDetails, Department


class TransactionDetailsInline(admin.TabularInline):
    model = TransactionDetails
    extra = 1

class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Transaction Details', {'fields': ['type']}),
        ('Date Information', {'fields':['date']}),
        ('Department Details', {'fields':['department']}),
    ]
    inlines = [TransactionDetailsInline]
    list_display = ['date', 'type', 'department']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'department']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['brand', 'name', 'quantity']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'num_emp']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Transaction, TransactionAdmin)




