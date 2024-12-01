# Generated by Django 5.1.2 on 2024-11-25 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
        ('Products', '0002_items_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='order',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_cost',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_method',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.URLField()),
                ('quantity', models.PositiveIntegerField()),
                ('size', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Cart.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.items')),
            ],
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
