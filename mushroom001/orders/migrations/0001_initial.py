# Generated by Django 3.1.3 on 2020-12-23 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': '产品类型',
                'verbose_name_plural': '产品类型',
                'db_table': 'product_category',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '订单产品',
                'verbose_name_plural': '订单产品',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('order_id', models.CharField(default='', max_length=128, unique=True, verbose_name='订单编号')),
                ('to_user', models.CharField(max_length=32, verbose_name='收货人')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='订单总价')),
                ('order_status', models.SmallIntegerField(choices=[(0, '报价中'), (1, '已下单'), (2, '已发货'), (3, '配送中'), (4, '退单'), (5, '完成')], default='报价中', verbose_name='订单状态')),
                ('order_pay', models.SmallIntegerField(choices=[(0, '待支付'), (1, '未付清'), (2, '已支付')], default='待支付', verbose_name='支付状态')),
                ('order_send_status', models.SmallIntegerField(choices=[(0, '备货中'), (1, '已发送')], default='备货中', verbose_name='发货状态')),
                ('order_send_way', models.CharField(max_length=10, verbose_name='发货方式')),
                ('order_send_nu', models.CharField(max_length=10, verbose_name='快递单号')),
                ('generator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='制单人')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='产品名称')),
                ('desc', models.TextField(verbose_name='产品描述')),
                ('model', models.CharField(default='', max_length=10, verbose_name='产品型号')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='产品价格')),
                ('image', models.ImageField(default='/images/default.jpg', upload_to='images/%Y/%m', verbose_name='产品图片')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.category', verbose_name='产品类型')),
            ],
            options={
                'verbose_name': '产品信息',
                'verbose_name_plural': '产品信息',
                'db_table': 'product_info',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField(default=0, verbose_name='产品数量')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'verbose_name': '订单详情',
                'verbose_name_plural': '订单详情',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(through='orders.OrderItem', to='orders.Item'),
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.product'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.cart')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.item')),
            ],
            options={
                'verbose_name': '购物车详细',
                'verbose_name_plural': '购物车详细',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ManyToManyField(through='orders.CartItem', to='orders.Item'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
