from django.db import models

# Create your models here.


class Product(models.Model):
	pid=models.IntegerField()
	name=models.CharField(max_length=30)
	des=models.CharField(max_length=345)
	rating=models.IntegerField()
	img=models.CharField(max_length=300)
	price=models.CharField(max_length=300)
	category=models.CharField(max_length=300)
	specify=models.CharField(max_length=300)

	class Meta:
		db_table="products1"



class Cart(models.Model):
	pid=models.IntegerField()
	name=models.CharField(max_length=30)
	des=models.CharField(max_length=345)
	rating=models.IntegerField()
	img=models.CharField(max_length=300)
	price=models.CharField(max_length=300)
	category=models.CharField(max_length=300)
	specify=models.CharField(max_length=300)
	quantity=models.CharField(max_length=30,default='1')
	userid=models.CharField(max_length=300)

	class Meta:
		db_table="CartTable"



class  MySiteUser(models.Model):
	firstname=models.CharField(max_length=300)
	lastname=models.CharField(max_length=300)
	email=models.CharField(max_length=300)
	password=models.CharField(max_length=300)
	country=models.CharField(max_length=300)
	address=models.CharField(max_length=300)
	town=models.CharField(max_length=300)
	zipcode=models.CharField(max_length=300)
	phone=models.CharField(max_length=300)
	comment=models.CharField(max_length=300)

	class Meta:
		db_table="myuser"


class Reviews(models.Model):

	pid=models.CharField(max_length=300)
	userid=models.CharField(max_length=300)
	des=models.CharField(max_length=300)
	rating=models.CharField(max_length=300)
	class Meta:
		db_table="reviews"


	

	


