# Generated by Django 5.1.6 on 2025-03-02 07:00

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sotuv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('jami_summa', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('tolandi', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('qarz', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('bolim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bolim')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.mahsulot')),
                ('mijoz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.mijoz')),
            ],
        ),
    ]
