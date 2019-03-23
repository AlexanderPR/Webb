from django.contrib import admin
from .models import Person, Stock_history

class PersonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person, PersonAdmin)

class StockHistoryRegister(admin.ModelAdmin):
    pass
admin.site.register(Stock_history, StockHistoryRegister)