from django.db import models


class User_Roles(AbstractUser):
    roles = ((1,"Admin")), ((2,"Teacher")), ((3,"Student"))
    user_roles = models.CharField(max_length= 50, default=1, choices=roles)

    def __str__(self):
        fullname = self.first_name +" "+ self.last_name
        return fullname

class Institute(models.Model):
    name = models.CharField(max_length=50)
    establish = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=255)
    website = models.CharField(max_length=150)
    mobile = models.CharField(max_length=150)
    telephone = models.CharField(max_length=150)
    adress = models.TextField()
    logo = models.FileField(upload_to="institute/images", null=True, blank=True)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    
class Admin(models.Model):
    role = models.OneToOneField(User_Roles, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

class Gender(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Classes(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=150)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=150)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Faculties(models.Model):
    faculty_name = models.CharField(max_length=100)
    faculty_code = models.CharField(max_length=150)
    faculty_status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.faculty_name

class Departments(models.Model):
    department_name = models.CharField(max_length=100)
    department_code = models.CharField(max_length=150)
    department_status = models.BooleanField(default=False)
    department_description = models.TextField()
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.department_name

class Teachers(models.Model):
    role = models.OneToOneField(User_Roles, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.role