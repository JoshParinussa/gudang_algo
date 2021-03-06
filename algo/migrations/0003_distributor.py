# Generated by Django 3.0.5 on 2020-08-10 06:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('algo', '0002_product_productcategory_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('kode', models.CharField(blank=True, db_index=True, max_length=32, null=True)),
                ('company_name', models.CharField(blank=True, db_index=True, max_length=128, null=True, verbose_name='nama perusahaan')),
                ('address', models.CharField(blank=True, db_index=True, max_length=128, null=True, verbose_name='alamat')),
                ('contact_person', models.CharField(blank=True, db_index=True, max_length=128, null=True, verbose_name='nama kontak')),
                ('office_phone', models.CharField(blank=True, max_length=128, null=True, verbose_name='no telp kantor')),
                ('phone', models.CharField(blank=True, max_length=128, null=True, verbose_name='no HP')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
