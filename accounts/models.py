from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    loan_status = models.CharField(max_length=20, default='pending', blank=True, null=True)
    num_transactions = models.IntegerField(default=0, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"Transaction {self.id} for {self.user.name}"


class LoanApplication(models.Model):
    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ]

    id_number = models.CharField(max_length=50, verbose_name="National Identity Number (NIN)")
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES)
    job_title = models.CharField(max_length=100)
    average_income = models.DecimalField(max_digits=10, decimal_places=2)
    account_number = models.CharField(max_length=20)
    identification = models.CharField(max_length=100, verbose_name="Means of Identification")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan Application: {self.id_number} - {self.job_title}"