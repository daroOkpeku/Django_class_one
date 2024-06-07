from django.contrib import admin
from .models import Student_info
from .models import Attendance
# Register your models here.


class AttendanceAdmin(admin.ModelAdmin):
    search_fields = ['studentId', 'studentName', 'date', 'date']
    

class StudentAdmin(admin.ModelAdmin):
    # this allows the admin to do full scale search in the database and also view all the items in the database table
    search_fields = ['name', 'student_id', 'course', 'email', 'phone_number']

admin.site.register(Student_info, StudentAdmin)
admin.site.register(Attendance, AttendanceAdmin)