from django.db import models

# Create your models here.
class Member(models.Model):
    userid= models.CharField(max_length=200, unique=True)
    fullname = models.CharField(max_length=200)
    address = models.TextField()
    dateofbirth = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
def member_exist(self):
    return self.address

def __str__(self):
    return '%s %s' % (self.fullname, self.address)
