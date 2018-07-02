from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=50)
    # name = models.CharField(max_length=50)
    password = models.CharField(max_length=80)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=1,null=True)
    pic = models.CharField(max_length=100,null=True)
    # 0 表示正常 1 表示禁用
    status = models.IntegerField(default=0)
    addtime = models.DateTimeField(auto_now_add=True)


# 会员地址
class Address(models.Model):
    uid =  models.ForeignKey(to="Users", to_field="id")
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=20)
    xiangxi = models.CharField(max_length=50)
    status = models.IntegerField(default=0)


# 商品分类模型
class Types(models.Model):
    '''
        无限分类
            types 
                id name pid path 
                1  国家  0   0,
                2  品牌  1   0,1,
                3  本田  2   0,1,2,
                4  丰田  3   0,1,2,3,
    '''
    name = models.CharField(max_length=20)
    pid = models.IntegerField()
    path = models.CharField(max_length=50)

# 商品模型
class Goods(models.Model):
    # 一对多
    typeid = models.ForeignKey(to='Types',to_field='id')
    title = models.CharField(max_length=255)
    descr = models.CharField(max_length=255,null=True)
    info = models.TextField(null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    pics = models.CharField(max_length=100)
    # 0为新发布 1为下架
    status = models.IntegerField(default=0)
    store = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    addtime = models.DateTimeField(auto_now_add=True)


# 订单模型
class Orders(models.Model):
    uid = models.ForeignKey(to="Users", to_field="id")
    addressid = models.ForeignKey(to="Address", to_field="id")
    totalprice = models.FloatField()
    totalnum = models.IntegerField()
    status = models.IntegerField(default=0)
    addtime = models.DateTimeField(auto_now_add=True,null=True)

# 订单详情
class OrderInfo(models.Model):
    orderid = models.ForeignKey(to="Orders", to_field="id")
    gid = models.ForeignKey(to="Goods", to_field="id")
    num = models.IntegerField()

# 城市三级联动
class Citys(models.Model):
    # id name upid 
    name = models.CharField(max_length=100)
    upid = models.IntegerField()

    # myhome_citys
    class Meta():
        db_table = 'citys'
