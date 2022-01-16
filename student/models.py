from django.db import models  
class Student(models.Model):  
    sid = models.CharField(max_length=10)  
    sname = models.CharField(max_length=100)  
    smark1 = models.CharField(max_length=100,default='0')
    smark2 = models.CharField(max_length=15,default='0')
    smark3 =  models.CharField(max_length=15,default='0')
    scomment = models.CharField(max_length=15,default='Nil')
    class Meta:  
        db_table = "students"  