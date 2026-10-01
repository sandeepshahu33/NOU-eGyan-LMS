from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.cache import cache_control
from mainapp.models import StudentInfo,LoginInfo
from adminapp.models import Material
import datetime
from studentapp.models import *

# Create your views here.

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studenthome(req):
    try:
        if req.session['studentid'] != None:
            stu=StudentInfo.objects.get(rollno=req.session['studentid'])
            return render(req,"studenthome.html" ,{"stu":stu})
    except KeyError:
        messages.success(req,"Please Login first")
        return redirect('login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studentlogout(req):
    try:
        if req.session['studentid'] != None:
            del req.session['studentid']
            messages.success(req,"You have logged out successfully!!")
            return redirect('login')
    except KeyError:
        messages.success(req,"Please Login first")
        return redirect('login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def changepwd(req):
    try:
        if req.session['studentid']!=None:
            if req.method=="POST":
                oldpassword=req.POST["oldpassword"]
                newpassword=req.POST["newpassword"]
                confirmpassword=req.POST["confirmpassword"]
                if newpassword != confirmpassword:
                    messages.success(req,"Newpassword and confirm password are not matches")
                    return redirect("changepwd")
                else:
                    try:
                        obj=LoginInfo.objects.get(username=req.session['studentid'],password=oldpassword)
                        LoginInfo.objects.filter(username=req.session['studentid']).update(password=newpassword)
                        messages.success(req,"Password is saved successfully")
                        return redirect("studentlogout")
                    except:
                        messages.success(req, "Old password is not matches")
                        return redirect("changepwd")
            return render(req,"changepwd.html")
    except KeyError:
        messages.success(req,"Please login first!!")
        return redirect('login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewmat(req):
    try:
        if req.session['studentid'] != None:
            stu=StudentInfo.objects.get(rollno=req.session['studentid'])
            smat=Material.objects.filter(program=stu.program,branch=stu.branch,year=stu.year)
            return render(req,"viewmat.html" ,{"stu":stu,"smat":smat})
    except KeyError:
        messages.success(req,"Please Login first")
        return redirect('login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def giveresponse(req):
    try:
        if req.session['studentid'] != None:
            stu=StudentInfo.objects.get(rollno=req.session['studentid'])
            if req.method=='POST':
                responsetype=req.POST['responsetype']
                responsetext=req.POST['responsetext']
                name=stu.name
                branch=stu.branch
                year=stu.year
                program=stu.program
                posteddate=datetime.datetime.today().strftime('%d/%m/%Y')
                res=Response(responsetype=responsetype,responsetext=responsetext,name=name,branch=branch,year=year,program=program,posteddate=posteddate)
                res.save()
                messages.success(req,"Your response is submitted successfully!!")
                return redirect('giveresponse')
            return render(req,"giveresponse.html",{"stu":stu})
    except KeyError:
        messages.success(req,"Please Login first")
        return redirect('login')



