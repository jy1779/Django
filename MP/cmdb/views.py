from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect
from collections import namedtuple
# Create your views here.
from .db import select_all,insert,delete,update,authentication
def login(request):
    error = ""
    if request.method == "POST":
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if authentication(user,pwd) :
            return redirect('/home')
        else:
            error = "账号或密码错误"
    return render(request,'login.html',{'error':error})
def index(request):
    return render(request,'index.html')
def host_manage(request):
    return render(request,'host_manage.html')
def home(request):
    return render(request,'home.html')
def user_manage(request):
    User=namedtuple("User", ("id", "owner", "user", "password","remarks"))
    user_id = select_all()[0]
    user_owner = select_all()[1]
    user_user = select_all()[2]
    user_password = select_all()[3]
    user_remarks = select_all()[4]
    users = []
    for item in zip(user_id, user_owner, user_user, user_password,user_remarks):
        user = User(*item)
        users.append(user)
    return render(request,'user_manage.html',{"users":users})
def add_user(request):
    owner = request.POST.get("owner",None)
    user = request.POST.get("user",None)
    password = request.POST.get("password",None)
    remarks = request.POST.get("remarks",None)
    insert(owner,user,password,remarks)
    return  redirect('/user_manage')

def del_user(request):
    user_id = request.POST.get("user_id")
    if user_id:
        delete(user_id)
        return redirect('/user_manage')
    else:
        return redirect('/user_manage')
def Upd_user(request):
    upd_id = request.POST.get("upd_id",None)
    upd_owner = request.POST.get("upd_owner",None)
    upd_user = request.POST.get("upd_user",None)
    upd_password = request.POST.get("upd_password",None)
    upd_remarks = request.POST.get("upd_remarks",None)
    update(upd_id,upd_owner,upd_user,upd_password,upd_remarks)
    return redirect('/user_manage')