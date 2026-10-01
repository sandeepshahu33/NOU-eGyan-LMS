from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.cache import cache_control
from mainapp.models import Enquiry,StudentInfo,LoginInfo
from adminapp.models import *
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(req):
    try:
        if req.session['adminid']!=None:
            return render(req,"adminhome.html")
    except KeyError:
        messages.success(req,"Please login first!!")
        return redirect('login')
    # return render(req,"adminhome.html")

def adminlogout(req):
    try:
        if req.session['adminid'] != None:
            del req.session['adminid']
            messages.success(req,"You have logged-out sucessfully")
            return redirect("login")
    except KeyError:
        messages.success(req,"Please login first !!")
        return redirect("login")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewenquiries(req):
    try:
        if req.session['adminid']!=None:
            enq=Enquiry.objects.all()
            return render(req,"viewenquiries.html",{"enq":enq})
    except KeyError:
        messages.success(req,"Please login first!!")
        return redirect('login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deleteenq(req,id):
    try:
        if req.session['adminid']!=None:
            enq=Enquiry.objects.get(id=id)
            enq.delete()
            return redirect('viewenquiries')
    except KeyError:
        messages.success(req,"Please login first!!")
        return redirect('login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studentdata(req):
    try:
        if req.session['adminid']!=None:
            stu=StudentInfo.objects.all()
            return render(req,"studentdata.html",{"students":stu})
    except KeyError:
        messages.success(req,"Please login first!!")
        return redirect('login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewmore(req,rollno):
    try:
        if req.session['adminid']!=None:
            si=StudentInfo.objects.get(rollno=rollno)
            return render(req,"viewmore.html",{"si":si})
    except KeyError:
        messages.success(req,"Please login first!!")
        return redirect('login')
    
# @cache_control(no_cache=True,must_revalidate=True,no_store=True)
# def changepassword(req):
#     return render(req,"changepassword.html")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def changepassword(req):
    try:
        if req.session['adminid']!=None:
            if req.method=="POST":
                oldpassword=req.POST["oldpassword"]
                newpassword=req.POST["newpassword"]
                confirmpassword=req.POST["confirmpassword"]
                if newpassword != confirmpassword:
                    messages.success(req,"Newpassword and confirm password are not matches")
                    return redirect("changepassword")
                else:
                    try:
                        obj=LoginInfo.objects.get(username=req.session['adminid'],password=oldpassword)
                        LoginInfo.objects.filter(username=req.session['adminid']).update(password=newpassword)
                        messages.success(req,"Password is saved successfully")
                        return redirect("adminlogout")
                    except:
                        messages.success(req, "Old password is not matches")
                        return redirect("changepassword")
            return render(req,"changepassword.html")
    except KeyError:
        messages.success(req,"Please login first!!")
        return redirect('login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def addmaterial(req):
    try:
        if req.session['adminid']!=None:
            if req.method=='POST':
                program=req.POST['program']
                branch=req.POST['branch']
                year=req.POST['year']
                subject=req.POST['subject']
                materialtype=req.POST['materialtype']
                filename=req.POST['filename']
                myfile=req.FILES['myfile']
                mat=Material(program=program,branch=branch,year=year,subject=subject,materialtype=materialtype,filename=filename,myfile=myfile)
                mat.save()
                messages.success(req,"Study Material Information is saved")
                return redirect('addmaterial')
            return render(req,"addmaterial.html")
    except KeyError:
        messages.success(req,"Please login first!!")
        return redirect('login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewmaterial(req):
    try:
        if req.session['adminid']!=None:
            mat=Material.objects.all()
            return render(req,"viewmaterial.html",{"mat":mat})
    except KeyError:
        messages.success(req,"Please login first!!")
        return redirect('login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deletemat(req,mid):
    try:
        if req.session['adminid']!=None:
            mat=Material.objects.get(mid=mid)
            mat.delete()
            messages.success(req,"Material information is delated.")
            return redirect('viewmaterial')
        return render(req,"deletemat.html")
    except KeyError:
        messages.success(req,"Please login first!!")
        return redirect('login')




