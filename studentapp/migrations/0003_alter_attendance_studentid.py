# Generated by Django 5.0.6 on 2024-06-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_alter_student_info_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='studentId',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]