from django.db import models

# Create your models here.

class Student_info(models.Model):
        courses = [
            ("SF", "Software Engineering"),
            ('AI', "Artificial Intelligence"),
            ("ME", "Blockchain Technology"),
            ("BI", "business intelligence")
        ]
    
        name = models.CharField(max_length=255, null=False)
        student_id = models.CharField(max_length=30, null=True, unique=True)
        # in here  course = models.CharField(max_length=255, null=False, choices=courses) you can only select item from the courses array
        course = models.CharField(max_length=255, null=False, choices=courses)
        email = models.EmailField(max_length=400, null=False, unique=True)
        phone_number = models.BigIntegerField(max_length=20, null=True)
        
        def __str__(self):
            return f"{self.name} - {self.student_id} - {self.course} - {self.email} - {self.phone_number}"
        


class Attendance(models.Model):
    studentId = models.CharField(max_length=30, null=True, unique=True)
    date = models.DateTimeField(null=False)
    studentName = models.CharField(max_length=200)
    
    def __str__(self):
            return f'{self.studentName} - {self.date} - {self.studentId}'
        
