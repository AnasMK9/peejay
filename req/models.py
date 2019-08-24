from django.db import models
import datetime
from django.utils.timezone import now
# Create your models here.


class reqT(models.Model):
    request_id = models.CharField(max_length=20, primary_key=True)
    req = models.CharField(max_length=30)

    def __str__(self):
        return self.req
'''
    reqchoice = [
        ('1','استخراج رخصة قيادة جديدة'),   18.15 دينار رسوم معاملة لأول مرة ،( 5 ) دنانير رسوم فحص أو إعادة فحص نظري ، (10) دنانير رسوم فحص أو إعادة فحص عملي ، (29.90) رسوم إصدار رخصة لأول م 
        ('2','استخراج رخصة قيادة بدل فاقد'),
        ('3','استخراج رخصة قيادة بدل تالف'),
        ('4','تجديد رخصة قيادة'),
        ('5','استخراج رخصة مركبة بدل فاقد'),
        ('6','استخراج رخصة مركبة بدل تالف')
        ('7','استخراج لوحة مركبة بدل فاقد')
        '8','استخراج لوحة مركبة بدل تالف')
'9','الاحتفاظ برقم مركبة خصوصية')
'10','الإستعلام عن رسوم نقل ملكية مركبة')
'11','نقل ملكية مركبة')
'12','تسجيل شكوى')
'13' , 'تجديد رخصة مركبة')




    ]
    '''

class allReqs(models.Model):
    req_id = models.CharField(max_length = 10)
    NID = models.CharField( max_length=10)
    price = models.IntegerField()
    complete = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    expDate = models.DateTimeField(default = now)
    reqtype = models.IntegerField()


class req1(models.Model):
    req_id = models.CharField(max_length=10)
    NID = models.CharField( max_length=10)
    NID2 = models.CharField( max_length=10)
    ltype = models.IntegerField()
    complete = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    price = models.IntegerField()
    active = models.BooleanField(default=False)
    expDate = models.DateTimeField(default = now)
    reqtype = models.IntegerField()

