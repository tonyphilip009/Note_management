from django.db import models
from django.contrib.auth.models import User

class NoteDb(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField(null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TaskDb(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField(null=True,blank=True)
    due_date=models.DateField()
    status=models.CharField(max_length=50,default="pending")
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title