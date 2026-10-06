from django.db import models
from django.contrib import admin
class vehicle_DB(models.Model):
    VEh_No=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    VehName=models.CharField(max_length=20)
    DoB=models.DateField()
    Email=models.EmailField()
    Address=models.TextField()
    Mobile=models.IntegerField()
class Vehicle_DBAdmin(admin.ModelAdmin):
    list_display=["VEh_No","name","VehName","DoB","Email","Address","Mobile"]
