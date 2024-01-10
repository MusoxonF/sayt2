# Generated by Django 5.0.1 on 2024-01-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elon', '0008_alter_car_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='address',
            field=models.CharField(choices=[('andijon', 'Andijon'), ('buxoro', 'Buxoro'), ("farg'ona", "Farg'ona"), ('jizzax', 'Jizzax'), ('xorazm', 'Xorazm'), ('namangan', 'Namangan'), ('navoiy', 'Navoiy'), ('qashqadaryo', 'Qashqadaryo'), ("qoraqalpog'iston respublikasi", "Qoraqalpog'iston Respublikasi"), ('samarqand', 'Samarqand'), ('sirdaryo', 'Sirdaryo'), ('surxondaryo', 'Surxondaryo'), ('toshkent', 'Toshkent')], max_length=30),
        ),
    ]