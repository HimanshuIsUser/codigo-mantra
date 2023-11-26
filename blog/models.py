from django.db import models
import uuid
from login.models import CustomUser,User_profile

class BlogModel(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4,editable=False)
    user = models.ForeignKey(User_profile,null=True,blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='media',null=True,blank=True) 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)



class Blogcomment(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4,editable=False)
    comment = models.TextField()
    user = models.ForeignKey(User_profile, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)