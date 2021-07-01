from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
class Recruiter(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=100,primary_key=True)
    company_name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    company_website = models.CharField(max_length=100)
    adress_line1 = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    manpower = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.email

class Partner(models.Model):
    CATEGORY = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Prefer not to say', 'Prefer not to say'),
        ) 
    CATEGORY1 = (
            ('Digital shop', 'Digital shop'),
            ('Other shop', 'Other shop'),
            ('Individual with no shop', 'Individual with no shop'),
            ) 


    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
 
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    adress_line1 = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    Do_you_have = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
class Skills(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name
class Work_Loc(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Worker_model(models.Model):
    Name = models.CharField(max_length=100, null=True)
    Phone_Number = models.CharField(max_length = 10, null=True)
    Email = models.EmailField(default = 'abc@xyz.com', null=True)
    Address_line1 = models.CharField(max_length=100, null=True)
    State = models.CharField(max_length=100, null=True)
    City = models.CharField(max_length=100, null=True)
    #Categories = models.ManyToManyField(Skills, blank=True, null=True)
    Categories = models.CharField(max_length=100, null=True)
    Education_Level = models.CharField(max_length=2, null=True)
    Minimum_Expected_Salary = models.CharField(max_length=100, null=True)
    Date_of_Birth = models.CharField(max_length=50, null=True)
    #Preferred_Work_Location = models.ManyToManyField(Work_Loc, null = True)
    Preferred_Work_Location = models.CharField(max_length=500, null=True)
    Previous_Work_Experience = models.CharField(max_length=1000, null=True)
 

    def _str_(self):
        return self.Name



