from django.urls import path
from .views import RegisterView, login_view, DashboardView, LoanApplicationView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),  
    path('dashboard/<int:user_id>/', DashboardView.as_view(), name='dashboard'),
    path('apply/', LoanApplicationView.as_view(), name='loan-application'),

]
