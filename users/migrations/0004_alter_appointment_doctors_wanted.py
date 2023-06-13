# Generated by Django 4.1.7 on 2023-06-06 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_is_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctors_wanted',
            field=models.CharField(choices=[('ENT', 'ENT'), ('orthopedic', 'Orthopedic'), ('physician', 'Physician'), ('cardiologist', 'Cardiologist')], max_length=50),
        ),
    ]
