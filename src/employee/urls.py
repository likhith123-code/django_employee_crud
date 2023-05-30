from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('home/',HomePage),
    path("addEmployee/",AddEmployee),
    path("deleteEmployee/<int:emp_id>",deleteEmployee),
    path("editEmployee/<int:emp_id>",editEmployee),
    path("feedback/",Feedback)
]
