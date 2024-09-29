from django.contrib import admin
from . models import Department, Doctor, Booking

admin.site.register(Department)
admin.site.register(Doctor)
class BookingAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','doctor','booked','time','desc')
admin.site.register(Booking,BookingAdmin)
