from django.shortcuts import render,redirect,HttpResponse
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from blog.models import *
from django.core.mail import send_mail
from django.conf import settings
import threading
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def mailfunc(sub,title,email):
    from_email = settings.EMAIL_HOST_USER
    send_mail(sub,title,from_email,email)

def blog_website(request):
    data = BlogModel.objects.all()
    paginator = Paginator(data,4)
    page_number = request.GET.get("page")
    ServiceDataFinal = paginator.get_page(page_number)

    return render(request,"index.html",context={"data":ServiceDataFinal})

def login_page(request):
    return render(request,"login.html")


def register_page(request):
    return render(request,"register.html")


def forget_page(request):
    return render(request,"forget.html")

def contact(request):
    return render(request,"contact.html")


@api_view(["POST"])
def contactus(request):
    try:
        print(request.POST)
        data = request.data
        first_name = data["first_name"]
        last_name = data["last_name"]
        email = data["email"]
        text = data["text"]
        subject = data["subject"]
        t = threading.Thread(target=mailfunc,args=[subject,f"{first_name} {last_name}, {email} want to talk with you,{text}",["himanshub166@gmail.com"]])
        t.start()
        return Response({"status":200,"message":"Thank you"},status=200)
    except Exception as error:
        return HttpResponse(str(error))

def view_blog(request,pk):
    data = BlogModel.objects.filter(id = pk).values()
    comment = Blogcomment.objects.filter(blog = pk)
    return render(request,"view.html",{"data":data,"comment":comment})


def sendmail_func(request):
    email = request.POST.get("email")
    blog = BlogModel.objects.get(id = request.POST.get("id"))
    print(email)
    print(request.POST.get("id "))
    t = threading.Thread(target=mailfunc,args=[f"{blog.title}",blog.content,[email]])
    t.start()
    return redirect("/")


def blogcomment(request):
    if request.method=="POST":
        post = request.POST
        comment = post.get("comment")
        user = User_profile.objects.get(user = request.user)
        blog = BlogModel.objects.get(id=post.get("blog"))
        postcomment = Blogcomment(comment=comment,blog=blog,user=user)
        postcomment.save()
    return redirect("/")


def search(request):
    data = BlogModel.objects.filter(Q(title__icontains=request.POST.get("search")))
    paginator = Paginator(data,4)
    page_number = request.GET.get("page")
    ServiceDataFinal = paginator.get_page(page_number)

    return render(request,"index.html",context={"data":ServiceDataFinal})