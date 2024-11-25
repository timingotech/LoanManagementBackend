from django.contrib import admin
from .models import User, Transaction

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'loan_amount', 'loan_status', 'num_transactions')
    search_fields = ('name',)
    list_filter = ('loan_status',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'amount', 'description')
    search_fields = ('user__name', 'description')
    list_filter = ('date',)
