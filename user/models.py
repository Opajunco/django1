from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.

class Org(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    imglogo = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
    imgorg = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def __str__(self) -> str:
        return "{}".format(self.name)
        # return super().__str__()


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    
# #this method to generate profile when user is created
# @receiver(post_save, sender=User)
# def create_user_employee(sender, instance, created, **kwargs):
#     if created:
#         Employee.objects.create(user=instance)
        
# #this method to update profile when user is updated
# @receiver(post_save, sender=User)
# def save_user_employee(sender, instance, **kwargs):
#     instance.employee.save()
    



#class User(AbstractUser):
#     # image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
 #     id_org = models.ForeignKey(Org, null=False, blank=False, on_delete=models.CASCADE, default=1)
    
    
    # def get_image(self):
    #     if self.image:
    #         return '{}{}'.format(MEDIA_URL, self.image)
    #     return '{}{}'.format(STATIC_URL, 'img/empty.png')
    
