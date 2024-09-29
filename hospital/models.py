from django.db import models

class Department(models.Model):
    dep_name=models.TextField(max_length=50)
    dep_desc=models.TextField(max_length=200)
    def __str__(self):
        return self.dep_name
class Doctor(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_dep=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctores/')
    def __str__(self):
        return self.doc_name
class Booking(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=12)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    booked=models.DateField()
    time=models.TimeField()
    desc=models.TextField(max_length=500)
    def __str__(self):
        return self.name
