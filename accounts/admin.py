from django.contrib import admin
from .models import User, Transaction, LoanApplication, UserProfile

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'loan_amount', 'loan_status', 'num_transactions')
    search_fields = ('user',)
    list_filter = ('loan_status',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'amount', 'description')
    search_fields = ('user__name', 'description')
    list_filter = ('date',)

@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'marital_status', 'job_title', 'average_income', 'created_at')
    search_fields = ('id_number', 'job_title', 'account_number')
    list_filter = ('marital_status',)