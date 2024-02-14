from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.contrib import messages

from django.contrib.auth import get_user_model


# user table--------------------------------------------------------------------
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, username, first_name, password=None):
#         if not email:
#             raise ValueError("email is required")
#         if not username:
#             raise ValueError("Your user name is required")
#         if not first_name:
#             raise ValueError("Your First Name is required")
#         # if not last_name:
#         #     raise ValueError("Your Last Name is required")
#         # if not id:
#         #     raise ValueError("Your Middle Name is required")
        
        

#         user=self.model(
#             email=self.normalize_email(email),
#             username=username,
#             first_name=first_name,
#             # last_name=last_name,
#             # middle_name=middle_name,
#             # phone=phone,
#             # id=id,
#             # course=course,
            
            
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self, email, username, password=None):
#         user=self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#             # first_name=first_name,
#             # last_name=last_name,

#         )
#         user.is_admin=True
#         user.is_staff=True
        
#         user.is_superuser=True
#         user.save(using=self._db)
#         return user





class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

class MyStudents(AbstractBaseUser):

    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    # first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="username", max_length=100, unique=True)
    # id=models.CharField(verbose_name="id", max_length=100, unique=True, primary_key=True)
    # last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class MyStaff(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    # first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="username", max_length=100, unique=True)
    # id=models.CharField(verbose_name="id", max_length=100, unique=False, primary_key=True)
    # last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
class Patient(models.Model):
    user_type = [
    ("NHIF", "NHIF"),
    ("Cash payment", "Cash payment"),
]

    Patient_Id = models.CharField(max_length=100, primary_key=True)
    NHIF_Number = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Payment = models.CharField(max_length=40, choices=user_type)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
class Patientinfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    Symptoms = models.TextField()
    Problem = models.TextField()
    Treatment = models.TextField()
    Medicine = models.TextField()

    def __str__(self):
        return self.user.username

class StaffContactinfo(models.Model):
    region = [
    ("Arusha", "Arusha"),
    ("Dodoma", "Dodoma"),
    ("Mwanza", "Mwanza"),
    ("Iringa", "Iringa"),
    ("Tabora", "Tabora"),
]
    user_type = [
    ("Doctor", "Doctor"),
    ("Nurse", "Nurse"),
]
    professional = [
    ("Eye", "Eye"),
    ("Teeth", "Teeth"),
    ("Other", "Other"),
]
    level = [
    ("Certificate", "Certificate"),
    ("Diploma", "Diploma"),
    ("Bachelor", "Bachelor"),
    ("Master", "Master"),
    ("Phd", "Phd"),
    ("Other", "Other"),
]

    user = models.ForeignKey(MyStaff, on_delete=models.CASCADE)
    User_type = models.CharField(max_length=40, choices=user_type)
    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Level_Of_Education = models.CharField(max_length=40, choices=level)
    Professional = models.CharField(max_length=40, choices=professional)
    Region = models.CharField(max_length=40, choices=region)
    Phone = models.CharField(max_length=100)
    # Form4_Certificate = models.FileField(upload_to="home/")
    # Form6_Certificate = models.FileField(upload_to="home/")
    # Univercity_Certificate = models.FileField(upload_to="home/")
    # Profile_Image =models.ImageField(upload_to="home/")
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
