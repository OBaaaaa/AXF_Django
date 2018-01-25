from django.db import models

# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=30)
    img = models.CharField(max_length=200)
    trackid = models.CharField(max_length=30)

    class Meta:
        abstract=True


class Axf_wheel(Home):

    class Meta:
        db_table = 'axf_wheel'


class Axf_nav(Home):

    class Meta:
        db_table = 'axf_nav'


class Axf_mustbuy(Home):

    class Meta:
        db_table = 'axf_mustbuy'


class Axf_shop(Home):

    class Meta:
        db_table = 'axf_shop'

# trackid,name,img,categoryid,brandname,img1,childcid1,productid1,longname1,price1,marketprice1,img2,childcid2,productid2,longname2,price2,marketprice2,img3,childcid3,productid3,longname3,price3,marketprice3
class Axf_mainshow(Home):
    categoryid = models.CharField(max_length=100)
    brandname= models.CharField(max_length=100)
    img1= models.CharField(max_length=200)
    childcid1= models.CharField(max_length=100)
    productid1= models.CharField(max_length=100)
    longname1= models.CharField(max_length=100)
    price1= models.CharField(max_length=100)
    marketprice1= models.CharField(max_length=100)
    img2= models.CharField(max_length=200)
    childcid2= models.CharField(max_length=100)
    productid2= models.CharField(max_length=100)
    longname2= models.CharField(max_length=100)
    price2= models.CharField(max_length=100)
    marketprice2= models.CharField(max_length=100)
    img3= models.CharField(max_length=200)
    childcid3= models.CharField(max_length=100)
    productid3= models.CharField(max_length=100)
    longname3= models.CharField(max_length=100)
    price3= models.CharField(max_length=100)
    marketprice3= models.CharField(max_length=100)

    class Meta:
        db_table ='axf_mainshow'

# productid,productimg,productname,productlongname,isxf,pmdesc,specifics,price,marketprice,categoryid,childcid,childcidname,dealerid,storenums,productnum
class Axf_goods(models.Model):
    productid = models.CharField(max_length=100)
    productimg= models.CharField(max_length=100)
    productname= models.CharField(max_length=100)
    productlongname= models.CharField(max_length=100)
    isxf= models.BooleanField()
    pmdesc= models.CharField(max_length=100)
    specifics= models.CharField(max_length=100)
    price= models.CharField(max_length=100)
    marketprice= models.CharField(max_length=100)
    categoryid= models.CharField(max_length=100)
    childcid= models.CharField(max_length=100)
    childcidname= models.CharField(max_length=100)
    dealerid= models.CharField(max_length=100)
    storenums= models.CharField(max_length=100)
    productnum= models.CharField(max_length=100)

    class Meta:
        db_table ='axf_goods'


class Axf_foodtypes(models.Model):
    typeid = models.CharField(max_length=100)
    typename= models.CharField(max_length=100)
    childtypenames= models.CharField(max_length=200)
    typesort= models.CharField(max_length=100)

    class Meta:
        db_table ='axf_foodtypes'


class User(models.Model):
    u_username = models.CharField(max_length=16,unique=True)
    u_password = models.CharField(max_length=32)
    u_sex = models.NullBooleanField(default=False)
    u_phone = models.CharField(max_length=32)
    u_email = models.CharField(max_length=32)
    u_level = models.IntegerField(default=1)
    u_icon = models.ImageField(upload_to='static/uploadfiles/icon')

class Order(models.Model):
    user = models.ForeignKey(User)
    order_time = models.TimeField(auto_now=True)
    order_status = models.IntegerField(default=0)


class Cart(models.Model):
    cart_num = models.IntegerField(default=1)
    cart_user = models.ForeignKey(User)
    cart_goods = models.ForeignKey(Axf_goods)
    cart_order = models.ForeignKey(Order,default=None,null=True,blank=True)
    cart_check = models.BooleanField(default=True)
    cart_belong = models.BooleanField(default=False)


