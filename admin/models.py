from django.db import models
from django.db.models import PositiveIntegerField

A = "Débutante enthousiaste"
B = "Débutante avancée"
C = "Apprenante initiatique"
D = "Experte créative"

PASS = "PASS"
FAIL = "FAIL"

GRADE = (
    (A, "Débutante enthousiaste"),
    (B, "Débutante avancée"),
    (C, "Apprenante initiatique"),
    (D, "Experte créative")

)

REMARKS = (
    (PASS, "PASS"),
    (FAIL, "FAIL")
)


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
        if self.role.first_name and self.role.last_name:
            full_name = self.role.first_name + " " + self.role.self_name
        return full_name

class TeacherProfile(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=50)
    image= models.FileField(upload_to="teachers/images", null=True, blanck=True)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.teacher.email

class Courses(models.Model):
    course_name = models.CharField(max_length=150)
    course_code = models.CharField(max_length=150)
    faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.course_name


class Shifts(models.Model):
    shift = models.CharField(max_length=150)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.shift

class GPA(models.Model):
    gpa_for = models.CharField(max_length=150)
    gpa = models.CharField(max_length=150)
    grade = models.FloatField(8,2)
    mark_from = models.IntegerField()
    mark_to = models.IntegerField()
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.grade


class Academics(models.Model):
    academic_year = models.CharField(max_length=150)
    academic_status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.academic_year

class Subjects(models.Model):
    subject_name = models.CharField(max_length=150)
    subject_code = models.CharField(max_length=150)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    subject_unite = models.IntegerField()
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.subject_name
    
    def get_total_unite(self):
        tot = 0
        total = Subjects.objects.all()
        for i in total:
            tot +=i
        return i

class Session(models.Model):
    session = models.CharField(max_length=150, unique=True)
    is_current_session = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.session

class Semester(models.Model):
    semester_name = models.CharField(max_length=150)
    is_current_semester = models.BooleanField(default=False)
    semester_code = models.CharField(max_length=100)
    semester_duration = models.CharField(max_length=100)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    next_semester_begins = models.DateField(auto_now=False, auto_now_add=False, blank = True, null=True)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.semester_name

class Levels(models.Model):
    level = models.CharField(max_length=150)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    level_description = models.TextField()
    level_status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.level

class Classes(models.Model):
    class_name = models.CharField(max_length=150)
    class_code = models.ForeignKey(Courses, on_delete=models.CASCADE)
    class_status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.class_name


class Students(models.Model):
    role = models.OneToOneField(User_Roles, on_delete=models.CASCADE)
    level = models.ForeignKey(Levels, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        if self.role.first_name and self.role.last_name:
            full_name = self.role.first_name + " " + self.role.self_name
        return full_name

class Roll(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=150)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.roll_no



class TakenSubjects(object):
    student = models.ForeignKey(User_Roles, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    ca = models.PositiveIntegerField(blank=True, null=True, default=0)
    exam = models.PositiveIntegerField(blank=True, null=True, default=0)
    total = models.PositiveIntegerField(blank=True, null=True, default=0)
    grade = models.CharField(choices=GRADE,max_length=5, blank=True, null=True)
    remarks = models.CharField(choices=REMARKS,max_length=5, blank=True, null=True)
    
    def get_total(self, ca, exam):
        total = int(ca) + int(exam)
        if total >= 70:
            grade = D
        elif total >= 60:
            grade = C
        elif total >= 50:
            grade = B
        elif total >= 40 : 
            grade = A
