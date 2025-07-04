from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseIncomeViewSet, RegisterView


# Registering viewsets with DRF's router
router = DefaultRouter()
router.register('expenses', ExpenseIncomeViewSet, basename='expenses')


# Auth and API URLs
urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('', include(router.urls)),
]
