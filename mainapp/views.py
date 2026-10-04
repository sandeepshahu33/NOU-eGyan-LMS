from django.shortcuts import render,redirect
import datetime
from django.contrib import messages
from .models import Enquiry,StudentInfo,LoginInfo

# Create your views here.

# def index(req):
#     return render(req,'index.html')

def index(req):
    return render(req,'home.html')
    # return render(req,'index.html')
    # return render(req,'contactus1.html')
'''
def courses(req):
    return render(req,"courses.html")

def services(req):
    return render(req,"services.html")

def contactus1(req):
    return render(req,"contactus1.html")
def login1(req):
    return render(req,"login1.html")
def registration1(req):
    return render(req,"registration1.html")
def enquery(req):
    return render(req,"enquery.html")

'''
def contactus(req):
    if req.method == "POST":
        name=req.POST["name"]
        gender=req.POST["gender"]
        address=req.POST["address"]
        contactno=req.POST["contactno"]
        emailaddress=req.POST["emailaddress"]
        enquirytext=req.POST["enquirytext"]
        posteddate=datetime.datetime.today().strftime("%d/%m/%Y")
        enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,posteddate=posteddate)
        enq.save()
        messages.success(req,'Your enquiry is submitted successfully')
        return redirect("contactus")
    return render(req,'contactus.html')

def registration(req):
    if req.method=="POST":
        rollno=req.POST['rollno']
        name=req.POST['name']
        fname=req.POST['fname']
        mname=req.POST['mname']
        mname=req.POST['mname']
        gender=req.POST['gender']
        address=req.POST['address']
        program=req.POST['program']
        branch=req.POST['branch']
        year=req.POST['year']
        contactno=req.POST['contactno']
        emailaddress=req.POST['emailaddress']
        password=req.POST['password']
        regdate=datetime.datetime.today().strftime("%d/%m/%Y")
        usertype='student'
        stu=StudentInfo(rollno=rollno,name=name,fname=fname,mname=mname,gender=gender,address=address,program=program,branch=branch,year=year,contactno=contactno,emailaddress=emailaddress,regdate=regdate)
        log=LoginInfo(username=rollno,password=password,usertype=usertype)
        stu.save()
        log.save()
        messages.success(req,"Student registration is done .") 
        return redirect('registration')
    return render(req,"registration.html")
def login(req):
    if req.method=="POST":
        username=req.POST['username']
        password=req.POST['password']
        try:
            obj=LoginInfo.objects.get(username=username,password=password)
            if obj.usertype=="student":
                messages.success(req,"Welcome Student")
                req.session["studentid"]=username
                return redirect('studenthome')
            elif obj.usertype=='admin':
                req.session["adminid"]=username
                # messages.success(req,"Welcome Admin")
                return redirect("adminhome")
            return redirect("login")
        except Exception :
            messages.success(req,"Invalid User")
            return redirect("login")

    return render(req,"login.html")


