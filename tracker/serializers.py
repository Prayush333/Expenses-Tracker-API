from rest_framework import serializers
from .models import ExpenseIncome
from django.contrib.auth.models import User


# Serializer for Expense/Income records
class ExpenseIncomeSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = ExpenseIncome
        fields = [
            'id', 'title', 'description', 'amount', 'transaction_type',
            'tax', 'tax_type', 'total', 'created_at', 'updated_at'
        ]
        read_only_fields = ['user', 'created_at', 'updated_at', 'total']
     
    # Method to calculate total field value
    def get_total(self, obj):
        return obj.total


# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

      # Create method to save new user with hashed password
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
