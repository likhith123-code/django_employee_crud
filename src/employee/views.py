from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee, Feedback as FeedbackClass
from .forms import FeedbackForm

# Create your views here.
def HomePage(request):
    employees = Employee.objects.all()
    data ={
        "employees":employees
    }
    return render(request,"HomePage.html",data)

def AddEmployee(request):
    if (request.method == 'POST'):
        # Get the data
        emp_name = request.POST.get("emp_name")
        emp_age = request.POST.get("emp_age")
        emp_city = request.POST.get("emp_city")
        emp_department = request.POST.get("emp_department")
        # Create Model Object
        employee = Employee(name = emp_name, age = emp_age, department =emp_department, city = emp_city)
        # Save the Object
        employee.save()
        return redirect("/employee/home/")
    # Default request would be GET
    return render(request,"AddEmployee.html",{})

def deleteEmployee(request,emp_id):
    employee = Employee.objects.get(id=emp_id)
    print(employee.name)
    employee.delete()
    return redirect("/employee/home")

def editEmployee(request,emp_id):
    if(request.method == 'POST'):
        print("Got Here")
        existing = Employee.objects.get(id = emp_id)
        existing.name = request.POST.get("emp_name")
        existing.age =  request.POST.get("emp_age")
        existing.department = request.POST.get("emp_department")
        existing.city = request.POST.get("emp_city")
        existing.save()
        return redirect("/employee/home")
    # Default is GET so this code executes
    employee = Employee.objects.get(id=emp_id)
    return render(request,"EditEmployee.html",{
        "emp_id":emp_id,
        "employee":employee
    })

# Form created using the Django default forms
def Feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST) # bind the data
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            description = form.cleaned_data["description"]
            feedback = FeedbackClass(name=name, email = email, description = description)
            feedback.save()
            return redirect("/employee/home/")
    else:
        form = FeedbackForm()
        return render(request,"Feedback.html",{'form':form})