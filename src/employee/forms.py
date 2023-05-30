from django import forms
from .models import Employee

class FeedbackForm(forms.Form):
    name = forms.CharField(label = "Enter Name", max_length=20)
    email = forms.EmailField(label="Enter Email",max_length=50)
    description = forms.CharField(label = "Enter Description", widget=forms.Textarea)

    # Adding the class
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

# Create form from the class
# When we populate the data we can directly do form.save() for this kind of forms
# if form.is_valid():
#             form.save()
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields= ['name','age','city']
