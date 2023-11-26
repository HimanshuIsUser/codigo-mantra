from django.urls import path
from .views import *

urlpatterns = [
    path("",blog_website,name="bloglist"),
    path("login-page/",login_page,name="login_page"),
    path("register-page/",register_page,name="register_page"),
    path("forget-page/",forget_page,name="forget_page"),
    path("contact",contact,name="contact"),
    path("contactus/",contactus,name="contactus"),
    path("view/<pk>",view_blog,name="view_blog"),
    path("sendmail/",sendmail_func,name="send_mail"),
    path("comment/",blogcomment,name = "comment"),
    path("search/",search,name = "search"),
]