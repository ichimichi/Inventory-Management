from django.contrib import admin

# Register your models here.
from app.models import Employee, Item, Transaction, TransactionDetails

class TransactionDetailsInline(admin.TabularInline):
    model = TransactionDetails
    extra = 3

class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Transaction Details', {'fields': ['type']}),
        ('Date Information', {'fields':['date']}),
        ('Employee Details', {'fields':['employee']}),
    ]
    inlines = [TransactionDetailsInline]


admin.site.register(Employee)
admin.site.register(Item)
admin.site.register(Transaction, TransactionAdmin)




