from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()

# Create your models here.
class Member(models.Model):
    mid = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to="Member")
    phone = models.CharField(max_length=10, null=True, blank=True)
    
@receiver(post_save, sender=User)
def create_user_member(sender, instance, created, **kwargs):
    if created:
        print("create")
        Member.objects.create(user=instance)
       

class Promotion(models.Model):
    TYPE_PROMO = (
        ('N', 'Normally'),
        ('P', 'Promotion(1 Free 1)'),
    )
    pid= models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    content = models.CharField(max_length=500, null=True, blank=True)
    image_promotion = models.ImageField(upload_to='Promotion')
    type_promotion = models.CharField(max_length=1, choices=TYPE_PROMO)
    start_date = models.DateField(null=True, blank=True)
    end_date= models.DateField( null=True, blank=True)

class Interest(models.Model):
    iid = models.AutoField(primary_key=True)
    pid = models.ForeignKey(Promotion ,on_delete=models.CASCADE)
    mid = models.ForeignKey(Member , on_delete=models.CASCADE , related_name='matcher')
    status = models.BooleanField(default=False)
    matching = models.ForeignKey(Member , on_delete=models.CASCADE, related_name='matching', null=True, blank=True)
