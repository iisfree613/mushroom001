from django.db import models
from users.models import UserInfo


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="产品类型")
    desc = models.TextField(verbose_name="产品类型描述")

    class Meta:
        verbose_name = "产品类型"  # 类型
        verbose_name_plural = verbose_name
        db_table = "product_category"

    def __str__(self):
        return self.name


class Product(models.Model):
    """"
    产品信息
    """
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='产品类型')
    name = models.CharField(max_length=128, verbose_name='产品名称', unique=True)
    desc = models.TextField(verbose_name='产品描述')
    model = models.CharField(max_length=10, default='', verbose_name='产品型号')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='产品价格')
    image = models.ImageField(max_length=100, upload_to='images/%Y/%m', default='/images/default.jpg',
                              verbose_name='产品图片')
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '产品信息'
        verbose_name_plural = verbose_name
        db_table = 'product_info'


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "订单产品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.product} * {self.quantity}"


class Cart(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    item = models.ManyToManyField(Item, through="CartItem")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.user}的购物车"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name = "购物车详细"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.cart} - {self.item} * {self.quantity}"


class Order(models.Model):
    """
    订单详细信息
    """
    order_s = (
        (0, "报价中"),
        (1, "已下单"),
        (2, "已发货"),
        (3, "配送中"),
        (4, "退单"),
        (5, "完成"),
    )
    pay_s = (
        (0, "待支付"),
        (1, "未付清"),
        (2, "已支付"),
    )
    send_s = (
        (0, "备货中"),
        (1, "已发送"),
    )
    created = models.DateField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateField(auto_now=True, verbose_name='更新时间')
    order_id = models.CharField(max_length=128, default='', verbose_name='订单编号', unique=True)
    generator = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='制单人')
    to_user = models.CharField(max_length=32, verbose_name='收货人')
    # products = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, verbose_name='订单产品')
    item = models.ManyToManyField(Item, through="OrderItem")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="订单总价")
    order_status = models.SmallIntegerField(choices=order_s, default='报价中', verbose_name='订单状态')
    order_pay = models.SmallIntegerField(choices=pay_s, default='待支付', verbose_name='支付状态')
    order_send_status = models.SmallIntegerField(choices=send_s, default='备货中', verbose_name='发货状态')
    order_send_way = models.CharField(max_length=10, verbose_name='发货方式')
    order_send_nu = models.CharField(max_length=10, verbose_name='快递单号')

    class Meta:
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name


class OrderItem(models.Model):
    """
    关于订单的单品产品及数量
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0, verbose_name="产品数量")

    class Meta:
        verbose_name = "订单详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.order} - {self.item} * {self.quantity}"
