from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display = ['username','user_type']
    
admin.site.register(CustomUser,UserModel)

# Register Course and session year model
admin.site.register(Course)
admin.site.register(Session_Year)

# Register Student Model
admin.site.register(Student)

# Register Staff Model
admin.site.register(Staff)

# Register subject Model
admin.site.register(Subject)

# Register Staff_Notification Model
admin.site.register(Staff_Notification)

# Register Student_Notification Model
admin.site.register(Student_Notification)

# Register Staff_Leave Model
admin.site.register(Staff_Leave)

# Register Student_Leave Model
admin.site.register(Student_Leave)

# Register Staff_Feedback Model
admin.site.register(Staff_Feedback)

# Register Student_Feedback Model
admin.site.register(Student_Feedback)

# Register Attendance Model
admin.site.register(Attendance)

# Register Attendance_Report Model
admin.site.register(Attendance_Report)

# Register StudentResult Model
admin.site.register(StudentResult)



