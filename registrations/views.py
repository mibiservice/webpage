from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def pricing(request):
    return render(request, 'price.html')

def terms(request):
    return render(request, 'terms.html')

def refund_policy(request):
    return render(request, 'refund_policy.html')

def forms(request):
    return render(request, 'forms.html')

@csrf_exempt
def success(request):
    return render(request, 'success.html')

def price_worker(request):
    if request.method == 'POST':
        if request.POST.get('terms') == 'terms_and_conditions':
            print('hello')
            print(request.POST.get('terms'))
            amount = 1200
            order_currency = 'INR' 
            client=razorpay.Client(auth=('rzp_live_qn1mOPoha8nwg6','ePVRjPHnMNSsrEM8vk14AGVg'))
            payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        else:
            messages.success(request, 'Please accept the terms and conditions. ')
    return render(request, 'price_worker.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def partners(request):
    return render(request, 'partners.html')

def index(request):
    return render(request, 'index.html')

def join_us(request):
    return render(request, 'join_us.html')

def register_recruiter(request):
    form = RecruiterForm()
    context = {'form':form}
    if request.method == 'POST':
        if(request.POST.get("conditions")=="on"):
            recruiter=Recruiter.objects.all()
            a=recruiter.filter(email=request.POST.get('email')).count()
            if(a==0):
                if(len(request.POST.get('phone_number'))>10):
                    messages.success(request, f'phone number has to be of 10 digits')
                form = RecruiterForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    username = form.cleaned_data.get('name')
                    context = {'form':form, 'name': username}
                    messages.success(request, 'Account was created for ' + username)
                    return redirect('reg_recruiter')
            else:
                messages.success(request, f'Email already exists')
        else:
            messages.success(request, f'Please accept the terms and conditions')
    return render(request, 'recruiter1.html', context)

    

def register_partner(request):
    form = PartnerForm()
    context = {'form':form}
    if request.method == 'POST':
        if(request.POST.get("conditions")=="on"):
            form = PartnerForm(request.POST)
        
            
            if form.is_valid():
                
                name = request.POST.get('name')
                gender = request.POST.get('gender')
            
                phone_number = request.POST.get('phone_number')
                if(len(request.POST.get('phone_number'))>10):
                    messages.success(request, f'phone number has to be of 10 digits')
                email = request.POST.get('email')
                adress_line1 = request.POST.get('adress_line1')
                state = request.POST.get('state')
                city = request.POST.get('city')
                Do_you_have = request.POST.get('Do_you_have')
                print(name,gender,phone_number,email,adress_line1,state,city,Do_you_have)
                user=Partner.objects.create(name=name ,gender=gender,phone_number=phone_number,email=email,adress_line1=adress_line1,state=state,city=city,Do_you_have=Do_you_have)
                user.save()  
                username = form.cleaned_data.get('name')
                context = {'form':form, 'name': username}   
                messages.success(request, 'Account was created for ' + username)
                return redirect('reg_partner')
            else:
                messages.success(request, f'invalid credentials')  
        else:          
            messages.success(request, f'Please accept the terms and conditions')
            
    return render(request, 'partner1.html', context)

def register_worker(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        username = request.POST.get('Name')
        context = {'form':form, 'name': username}
        Name = request.POST.get('Name')
        Phone_Number = request.POST.get('Phone_Number')
        if(len(Phone_Number)>10):
            messages.success(request, f'phone number has to be of 10 digits')
        else:
            Email = request.POST.get('Email')
            Address_line1 = request.POST.get('Address_line1')
            State = request.POST.get('State')
            City = request.POST.get('City')
            Categories0 = request.POST.get('Categories0')
            Categories1 = request.POST.get('Categories1')
            Categories2 = request.POST.get('Categories2')
            Categories3 = request.POST.get('Categories3')
            Categories4 = request.POST.get('Categories4')
            Categories5 = request.POST.get('Categories5')
            Categories6 = request.POST.get('Categories6')
            Categories7 = request.POST.get('Categories7')
            var=None
            if(request.POST.get("conditions")=="on"):
                if(Categories7=="other"):
                    var=request.POST.get('other_job')
                    print('other_job'==var)
                Categories_list=[Categories0,Categories1,Categories2,Categories3,Categories4,Categories5,Categories6,Categories7,var]
                
                edu_level = request.POST.get('Education_Level')
                Minimum_Expected_Salary = request.POST.get('Minimum_Expected_Salary')
                Date_of_Birth = request.POST.get('Date_of_Birth')
                Preferred_Work_Location1 = request.POST.get('Preferred_Work_Location1')
                Preferred_Work_Location2 = request.POST.get('Preferred_Work_Location2')
                Preferred_Work_Location3 = request.POST.get('Preferred_Work_Location3')
                Preferred_Work_Location4 = request.POST.get('Preferred_Work_Location4')
                Previous_Work_Experience = request.POST.get('Previous_Work_Experience')
                Preferred_Work_Location_list=[Preferred_Work_Location1,Preferred_Work_Location2,Preferred_Work_Location3,Preferred_Work_Location4]
                cat_list=''
                for c in Categories_list:
                    if(c==None or c=="other"):
                        continue
                    else:
                        cat_list=cat_list+c+','
                work_loc =''  
                for p in Preferred_Work_Location_list:
                    if(p==None):
                        continue
                    else:
                        work_loc=work_loc+p+','
                NewWorker = Worker_model.objects.create(Name = Name, Phone_Number = Phone_Number, Email = Email, Address_line1 = Address_line1, State = State, City = City,Categories=cat_list, Education_Level = edu_level, Minimum_Expected_Salary = Minimum_Expected_Salary, Date_of_Birth = Date_of_Birth,Preferred_Work_Location=work_loc, Previous_Work_Experience = Previous_Work_Experience)
                NewWorker.save()
                messages.success(request, 'Account was created for ' + username)
                return redirect('price_worker')
            else:
                messages.success(request, f'Please accept the terms and conditions')

    else:
        form = WorkerForm()
        username = request.POST.get('Name')
        context = {'form':form, 'name': username}
    return render(request, 'worker1.html', context)
