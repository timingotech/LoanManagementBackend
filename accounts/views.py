from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import LoanApplicationSerializer, UserSerializer
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
import datetime
from rest_framework.permissions import IsAuthenticated

# Register View
class RegisterView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            if not username or not email or not password:
                return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

            if User.objects.filter(username=username).exists():
                return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

            if User.objects.filter(email=email).exists():
                return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(username=username, email=email, password=password)
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
def login_view(request):
    if request.method == "OPTIONS":
        response = JsonResponse({"detail": "Preflight OK"})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({"message": "Login successful"}, status=200)
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=400)
        

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]  # Only allow authenticated users

    def get(self, request):
        user_profile = request.user.profile  # Get the user's profile
        data = {
            'username': request.user.username,
            'balance': user_profile.balance,
            'loan_amount': user_profile.loan_amount,
            'loan_status': user_profile.loan_status,
            'avatar': user_profile.avatar.url if user_profile.avatar else None,
            'transactions': [
                {"date": "2024-11-20", "amount": 500.00, "description": "Groceries"},
                {"date": "2024-11-18", "amount": 100.00, "description": "Transportation"},
            ],
        }
        return Response(data)
        
class LoanApplicationView(APIView):
    def post(self, request):
        serializer = LoanApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Application submitted successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)