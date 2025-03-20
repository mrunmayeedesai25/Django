from django.db import models

# Create your models here.
 
# One to One 
class Studinfo(models.Model):
    studid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    rollno = models.IntegerField()
    gitlink = models.URLField()

class college(models.Model):
    studid = models.OneToOneField(Studinfo,on_delete=models.CASCADE)
    Qualification = models.CharField(max_length=50)

# one to many 

class Subject(models.Model): 
    Subjectcode = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=30) 
    credits = models.IntegerField() 

class Teacher(models.Model): 
    TeacherID = models.IntegerField(primary_key=True) 
    subjectcode=models.ForeignKey( 
                Subject,  
                on_delete=models.CASCADE 
                  ) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50) 

# many to many 

# class Teacher(models.Model): 
#     TeacherID = models.IntegerField(primary_key=True) 
#     Qualification = models.CharField(max_length=50) 
#     email = models.EmailField(max_length=50) 

# class Subject(models.Model): 
#     Subjectcode = models.IntegerField(primary_key = True) 
#     name = models.CharField(max_length=30) 
#     credits = models.IntegerField() 
#     teacher = models.ManyToManyField(Teacher) 

# Create your models here.

class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)

class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)


class Customer(models.Model): 
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Vehicle(models.Model): 
    name = models.CharField(max_length=255) 
    customer = models.ForeignKey( 
        Customer, 
        on_delete=models.CASCADE, 
        related_name='Vehicle' 
    ) 

class Person(models.Model): 
    first_name = models.CharField(max_length=20) 
    last_name = models.CharField(max_length=20) 

# class Logger(models.Model):
#     fn= models.CharField(max_length=200,required=False)
#     ln= models.CharField(max_length=200)

class Booking(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000) 

    def __str__(self):
        return self.first_name
    


class Employees(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name
