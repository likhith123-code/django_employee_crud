from django.contrib import admin
from .models import Employee


# Customize the Employee Model in Admin
class EmpModelAdmin(admin.ModelAdmin):
    list_display=("name","age","city","department","id")
    list_display_links=("name",) # Atleast one should be there to open the entire data
    list_editable=("age","city","department")
    search_fields = ("city",) # Must be a tuple

# Register your models here.
admin.site.register(Employee,EmpModelAdmin)
