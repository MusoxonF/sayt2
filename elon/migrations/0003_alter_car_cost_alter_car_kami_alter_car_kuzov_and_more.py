# Generated by Django 5.0.1 on 2024-01-08 20:23

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elon', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='cost',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='USD'),
        ),
        migrations.AlterField(
            model_name='car',
            name='kami',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Car_kami', to='elon.kami'),
        ),
        migrations.AlterField(
            model_name='car',
            name='kuzov',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Car_kuzov', to='elon.kuzov'),
        ),
        migrations.AlterField(
            model_name='car',
            name='manzil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Car_location', to='elon.locations'),
        ),
        migrations.AlterField(
            model_name='car',
            name='modeli',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Car_model', to='elon.car_model'),
        ),
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ManyToManyField(null=True, related_name='Car_photo', to='elon.image'),
        ),
        migrations.AlterField(
            model_name='car',
            name='uzatish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Car_qutisi', to='elon.uzatish'),
        ),
        migrations.AlterField(
            model_name='car',
            name='uzatma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Car_qutisi', to='elon.uzatma'),
        ),
        migrations.AlterField(
            model_name='car',
            name='yoqilgi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Car_yoqilgisi', to='elon.yoqilgi'),
        ),
    ]
