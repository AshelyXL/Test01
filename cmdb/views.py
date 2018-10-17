from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models
# Create your views here.

#创建一个用户信息列表，定义了两个数据
# user_list = [
#     {"user":None,"pwd":None},
# ]

# date_list=[
#     {"year":None,"month":None,"day":None},
# ]


def index(request):
    #return HttpResponse("Hello world!")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        #temp = {"user":username,"pwd":password}
        #user_list.append(temp)
        #添加数据到数据库，
        models.UserInfo.objects.create(user=username, pwd=password)
        #user和pwd分别是models.py中定义的变量
        #username和password是14行的入参
    #从数据库中读取所有数据
    #user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"info": models.UserInfo.objects.all()})
    # render方法接受第三个参数是后台返回给浏览器的数据，它是一个字典，
    # info是自定义的指针名字，user_list中的内容

def date(request):
    if request.method == "POST":
        year = request.POST.get("year", None)
        month = request.POST.get("month", None)
        day = request.POST.get("day", None)
        models.UserDate.objects.create(year=year,month=month,day=day)
    return render(request,"date.html",{"date":models.UserDate.objects.all()})

