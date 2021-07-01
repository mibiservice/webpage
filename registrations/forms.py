from django.forms import ModelForm
from django import forms
from multiselectfield import MultiSelectField
from .models import *


class RecruiterForm(ModelForm):
	class Meta:
		model = Recruiter
		fields = '__all__'
class PartnerForm(ModelForm):
	class Meta:
		model = Partner
		fields = '__all__'


CATEGORY = [
            ('Construction', 'Construction'),
            ('Mining', 'Mining'),
            ('Manufacturing', 'Manufacturing'),
            ('Agriculture', 'Agriculture'),
            ('Handy Man', 'Handy Man'),
            ('Transport', 'Transport'),
            ('Textile', 'Textile'),
            ('Other', 'Other'),

]

WORK_LOC = [
            ('SC:Same city','SC:Same city' ),
            ('SS:Same State','SS:Same State' ),
            ('TC:Tier 1 cities(Mumbai,Punjab etc)', 'TC:Tier 1 cities(Mumbai,Punjab etc)'),
            ('AL:All over India','AL:All over India' ),
    ] 

GENDER = [
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Prefer not to say', 'Prefer not to say'),
    ] 
    
CATEGORY1 = [
            ('Digital shop', 'Digital shop'),
            ('Other shop', 'Other shop'),
            ('Individual with no shop', 'Individual with no shop'),
    ] 

Education_Level = [
            ('NA:None', 'NA: None'),
            ('PE: Till 8th', 'PE: Till 8th'),
            ('SE:Till 10th', 'SE:Till 10th'),
            ('SS:Till 12th', 'SS:Till 12th'),
            ('PG:Post Graduation', 'PG:Post Graduation'),
    ] 

class PartnerForm(forms.Form):
    
    name = forms.CharField(max_length=200)
    gender = forms.CharField(label='gender', widget=forms.RadioSelect(choices=GENDER))
 
    phone_number = forms.CharField(max_length=15)
    email = forms.CharField(max_length=100)
    
    adress_line1 = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    Do_you_have = forms.CharField(label='Do_you_have', widget=forms.RadioSelect(choices=CATEGORY1))


class WorkerForm(forms.Form):  
    Name = forms.CharField(max_length=100)
    Phone_Number = forms.CharField(max_length = 10)
    Email = forms.EmailField()
    Address_line1 = forms.CharField(max_length=100)
    State = forms.CharField(max_length=100)
    City = forms.CharField(max_length=100)
    Categories = forms.CharField(max_length=50)
    Education_Level = forms.CharField(widget = forms.RadioSelect(choices = Education_Level))
    Minimum_Expected_Salary = forms.CharField(max_length=100)
    Date_of_Birth = forms.CharField(max_length=50)
    Preferred_Work_Location = forms.CharField(max_length=50)
    Previous_Work_Experience = models.CharField(max_length=1000)

class Worker1Form(ModelForm):
	class Meta:
		model = Worker_model
		fields = '__all__'
    
class RecruiterPaymentForm(forms.Form):
    name = forms.CharField(max_length=100, required = True)
    amount = forms.IntegerField(required = True)


