from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import ExpenseIncome
from .serializers import ExpenseIncomeSerializer, RegisterSerializer
from .permissions import IsOwnerOrAdmin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# To handles user registration (POST only)
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ViewSet to manage ExpenseIncome records
class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
    

    # Admins can view all records; users  can see only their own
    def get_queryset(self):
        if self.request.user.is_staff:
            return ExpenseIncome.objects.all()
        return ExpenseIncome.objects.filter(user=self.request.user)
    

    # Automatically assign current user to the record
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

