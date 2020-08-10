# Generated by Django 3.0.5 on 2020-08-10 05:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('algo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(db_index=True, max_length=128, verbose_name='nama kategori')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=128, verbose_name='nama satuan')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=128, verbose_name='nama produk')),
                ('barcode', models.CharField(max_length=128, unique=True)),
                ('stock', models.BigIntegerField(blank=True, null=True, verbose_name='stok')),
                ('minimal_stock', models.BigIntegerField(blank=True, null=True, verbose_name='batas minimal')),
                ('purchase_price', models.DecimalField(decimal_places=0, max_digits=9, null=True, verbose_name='harga beli')),
                ('selling_price', models.DecimalField(decimal_places=0, max_digits=9, null=True, verbose_name='eceran')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Active'), (1, 'Inactive')], db_index=True, default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='algo.ProductCategory', verbose_name='kategori')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='algo.Supplier')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='algo.Unit', verbose_name='satuan')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
