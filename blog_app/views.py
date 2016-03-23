# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.core.mail import send_mail

from models import Blog

MY_RESUME = {
    "my_name":"李波",
    "my_job":"软件工程师",
    "my_resume":"屌丝程序员，努力奋斗中",
    "address":"北京市昌平区沙河镇",
    "phone_number":"13671276405",
    "email":"sitemayerlee@163.com",
    "year": 2016,
    "company": "GkTek"
}

CONTACT_US_INFO = {
    "name":"",
    "email":"",
    "subject":"",
    "message":""
}

def getcontactinfo(request):
    CONTACT_US_INFO["name"] = request.POST["Name"]
    CONTACT_US_INFO["email"] = request.POST["Email"]
    CONTACT_US_INFO["subject"] = request.POST["Subject"]
    CONTACT_US_INFO["message"] = request.POST["Message"]

def packagemsg():
    msg = "from:" + CONTACT_US_INFO["email"] + "\n"
    msg += "name:" + CONTACT_US_INFO["name"] + "\n"
    msg += "message:" + CONTACT_US_INFO["message"] + "\n"
    return msg

def sendemail():
    send_mail(
        CONTACT_US_INFO["subject"],
        packagemsg(),
        MY_RESUME["email"],
        [ MY_RESUME["email"] ],
        fail_silently=False
    )

# Create your views here.
def index(request):
    if request.POST:
        getcontactinfo(request)
        sendemail()

    t = loader.get_template("index.html")
    d = MY_RESUME.copy()
    d["title"] = "吉克科技"
    d["text1"] = "谢谢关注"
    d["text2"] = "thanks for you attation"
    return HttpResponse(t.render(d))

def product(request):
    if request.POST:
        getcontactinfo(request)
        sendemail()

    t = loader.get_template("product.html")
    d = MY_RESUME.copy()
    d["title"] = "项目合作"
    d["text1"] = "谢谢关注"
    d["text2"] = "thanks for you attation"
    return HttpResponse(t.render(d))

def product_detail(request):
    pass

def blog(request):
    if request.POST:
        getcontactinfo(request)
        sendemail()

    t = loader.get_template("blog.html")
    d = MY_RESUME.copy()
    d["title"] = "博客园地"
    d["text1"] = "谢谢关注"
    d["text2"] = "thanks for you attation"
    d["blog_list"] = Blog.objects.all().order_by("date")

    return HttpResponse(t.render(d))

def blog_detail(request, blog_index):
    if request.POST:
        getcontactinfo(request)
        sendemail()
    else:
        blog = Blog.objects.get(index = blog_index)

    t = loader.get_template("blog_detail.html")
    d = MY_RESUME.copy()
    d["title"] = "项目合作"
    d["text1"] = "谢谢关注"
    d["text2"] = "thanks for you attation"
    d["blog"] = blog
    return HttpResponse(t.render(d))

def about_us(request):
    if request.POST:
        getcontactinfo(request)
        sendemail()

    t = loader.get_template("about_us.html")
    d = MY_RESUME.copy()
    d["user_img"] = "images/user.jpg"
    d["title"] = "博客园地"
    d["text1"] = "谢谢关注"
    d["text2"] = "thanks for you attation"
    d["blog_list"] = Blog.objects.all().order_by("date")

    return HttpResponse(t.render(d))
