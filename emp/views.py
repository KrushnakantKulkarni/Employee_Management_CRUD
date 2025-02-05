from django.shortcuts import render,HttpResponse,redirect
from emp import models
from emp.models import Employee
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def allemplyoees(request):
    emp = Employee.objects.all()
    return render(request,"emp/allemplyoees.html",{"allemployees":emp})

def singleemployee(request):
    return render(request,"emp/singlemployee.html")


def register(request):
    context={}
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        if uname=="" or upass=="" :
            context['errormsg']="field cannot be empty"
            return render(request,'emp/register.html',context)
        else :
            try:
                u=User.objects.create(username=uname,password=upass)
                u.set_password(upass)
                u.save()
                context["success"]="user created successfully pls login "
                return render(request,'emp/login.html',context)
            except Exception:
                context['errormsg']="username already exist"
                return render(request,'emp/register.html',context)
    else:
        return render(request,"emp/register.html")

def user_login(request):
    context = {}

    if request.method == "POST":
        uname = request.POST.get('uname', '').strip()
        upass = request.POST.get('upass', '').strip()

        if not uname or not upass:
            context['errormsg'] = "Fields cannot be empty"
            return render(request, 'emp/login.html', context)

        user = authenticate(username=uname, password=upass)
        if user is not None:
            login(request, user)
            return redirect('allemplyoees')  # Use the URL name from `urls.py`
        else:
            context['errormsg'] = "Invalid username or password"
            return render(request, 'emp/login.html', context)

    return render(request, "emp/login.html")

def user_logout(request):
    logout(request)
    return redirect ('/home')            

def addemployee(request):
    if request.method == "POST":
        employee_id = request.POST.get('employeeid')
        employee_name = request.POST.get('employeename')
        employee_email = request.POST.get('employeeemail')
        employee_address = request.POST.get('employeeaddress')
        employee_phone = request.POST.get('employeephone')

        # creating an object of the Employee model and saving it
        e = Employee(
            employee_id=employee_id,
            employee_name=employee_name,
            email=employee_email,
            address=employee_address,
            phone=employee_phone
        )
        e.save()
        return redirect("/allemplyoees")

    return render(request, "emp/addemployee.html")

def deleteemployee(request,empid):
    e = Employee.objects.get(pk = empid)
    e.delete()
    return redirect("allemplyoees")
 
def updateemployee(request, empid):
    e = get_object_or_404(Employee, pk=empid)  
    return render(request, "emp/updateemployee.html", {"singleemployee": e})  # FIXED VARIABLE NAME

def doupdateemployee(request, empid):
    if request.method == "POST":
        updateemployeeid       = request.POST.get('employeeid')
        updateemployeename     = request.POST.get('employeename')
        updateemployeeemail    = request.POST.get('employeeemail')
        updateemployeeaddress  = request.POST.get('employeeaddress')
        updateemployeephone    = request.POST.get('employeephone')

        # Fetch the employee safely
        emp = get_object_or_404(Employee, pk=empid)
        
        # Ensure the fields match the model exactly
        emp.employee_id = updateemployeeid
        emp.employee_name = updateemployeename
        emp.email = updateemployeeemail
        emp.address = updateemployeeaddress
        emp.phone = updateemployeephone

        emp.save()
        return redirect("allemplyoees")  # Ensure 'allemployees' is in urls.py

    return redirect("allemplyoees")  # Safety return
