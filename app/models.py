from django.db import models

class User(models.Model):
	User_id=models.AutoField(auto_created=True,primary_key=True)
	UserName=models.CharField(max_length=50)
	Email=models.CharField(max_length=60)
	password=models.CharField(max_length=30)
	class Meta:
		db_table="user"

class Package(models.Model):
	package_id=models.AutoField(auto_created=True,primary_key=True)
	PackageName=models.CharField(max_length=50)
	Description=models.TextField(max_length=600)
	PackageImage=models.ImageField(upload_to="images")
	PackageCost=models.CharField(max_length=50)
	PackageDays=models.CharField(max_length=20,default=2)
	Date=models.DateField()

	class Meta:
		db_table="package"

class Customer(models.Model):
	customer_id=models.AutoField(auto_created=True,primary_key=True)
	customerName=models.CharField(max_length=50)
	customerAddress=models.CharField(max_length=50)

	class Meta:
		db_table="customer"

class Booking(models.Model):
	booking_id=models.AutoField(auto_created=True,primary_key=True)
	customer=models.ForeignKey(Customer	,on_delete=models.CASCADE)
	package=models.ForeignKey(Package,on_delete=models.CASCADE)
	Days=models.CharField(max_length=20)
	Date=models.DateField()

	class Meta:
		db_table="booking"

class Admin(models.Model):
	admin_id=models.AutoField(auto_created=True,primary_key=True)
	admin_name=models.CharField(max_length=50)
	password=models.CharField(max_length=50)

	class Meta:
		db_table="admin"