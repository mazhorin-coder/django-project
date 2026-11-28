# employees/urls.py
from django.urls import path
from .views import EmployeeDetailView, EmployeeListView, IndexView

app_name = "employees"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("employees/", EmployeeListView.as_view(), name="list"),
    path("employees/<int:pk>/", EmployeeDetailView.as_view(), name="detail"),
]