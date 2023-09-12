# Generated by Django 4.2.2 on 2023-07-14 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Kategori')),
                ('image', models.ImageField(max_length=200, upload_to='category', verbose_name='Kategori Resmi')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Ürün Adı')),
                ('text', models.TextField(verbose_name='Ürün Açıklaması')),
                ('image', models.ImageField(max_length=200, upload_to='card', verbose_name='Ürün Resmi')),
                ('price', models.FloatField(verbose_name='Fiyat')),
                ('date_now', models.DateField(verbose_name='Ürün Çıkış Tarihi')),
                ('isactive', models.BooleanField(verbose_name='Aktif Kart')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.category', verbose_name='Kategori')),
            ],
        ),
    ]
